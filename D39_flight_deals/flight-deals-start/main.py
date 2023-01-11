# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import asyncio
from datetime import date, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


async def cheap_flight_scanner(
    file_name: str, tab_name: str, departure_city: str, email_to: str
) -> None:
    """Scan for cheapest flights"""
    data_manager = DataManager(file_name=file_name, tab_name=tab_name)
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    destinations = await data_manager.get_tab_data()
    departure_iata_city_code = await flight_search.get_iata_city_code(departure_city)

    # Get city IATA codes
    async with asyncio.TaskGroup() as tg:
        iata_codes = [
            tg.create_task(flight_search.get_iata_city_code(destination.get("city")))
            for destination in destinations
        ]

    # Update the dictionnary
    destinations = [
        dict(destination, iataCode=iata_codes[index].result())
        for (index, destination) in enumerate(destinations)
    ]

    # Update the Google Sheet with the codes
    async with asyncio.TaskGroup() as tg:
        _ = [
            tg.create_task(
                data_manager.update_row(
                    {
                        "iataCode": destination.get("iataCode"),
                        "id": destination.get("id"),
                    }
                )
            )
            for destination in destinations
        ]

    tomorrow = date.today() + timedelta(days=1)
    tomorrow_plus_six_months = tomorrow + timedelta(days=180)

    # Search flights to destination
    async with asyncio.TaskGroup() as tg:
        searches = [
            tg.create_task(
                flight_search.search(
                    fly_from=departure_iata_city_code,
                    fly_to=destination.get("iataCode"),
                    date_from=tomorrow.isoformat(),
                    date_to=tomorrow_plus_six_months.isoformat(),
                    nights_in_dst_from=destination.get("minNights", 1),
                    nights_in_dst_to=destination.get("maxNights", 1),
                )
            )
            for destination in destinations
        ]

    tab_data = []
    emails_text = []
    for index, search in enumerate(searches):
        print(f"Scanning flights to {destinations[index].get('city')}")
        flights = search.result()

        if len(flights) > 0:
            cheapest_flight = flights[0]
            if cheapest_flight.get("price") < destinations[index].get(
                "lowestPrice", 1000
            ):
                departure_date = cheapest_flight.get("route")[0].get("local_departure")
                return_date = cheapest_flight.get("route")[-1].get("local_arrival")

                # Store text email
                emails_text.append(notification_manager.format_email(cheapest_flight))

                # Store flight details
                tab_data.append(
                    {
                        "id": destinations[index].get("id"),
                        "lowestPrice": cheapest_flight.get("price"),
                        "departureDate": departure_date,
                        "returnDate": return_date,
                    }
                )
    print(tab_data)
    print(emails_text)

    # Send emails & update google sheet
    async with asyncio.TaskGroup() as tg:
        _ = [
            tg.create_task(
                notification_manager.send_async_email(
                    recipient_email=email_to,
                    subject=email_text.get("subject"),
                    body=email_text.get("message"),
                )
            )
            for email_text in emails_text
        ]

        # Update google sheet with flights data
        _ = [
            tg.create_task(data_manager.update_row(row_value)) for row_value in tab_data
        ]

        #     await notification_manager.send_async_email(
        #     recipient_email=email_to,
        #     subject=email_text.get("subject"),
        #     body=email_text.get("message"),
        # )

        # for destination in updated_destinations:
        #     print(f"Scanning flights to {destination.get('city')}")

        # # For each destination, search flights date_from = tomorrow, date_to = tomorrow + 180
        # tomorrow = date.today() + timedelta(days=1)
        # tomorrow_plus_six_months = tomorrow + timedelta(days=180)

        # flights = flight_search.search(
        #     fly_from=departure_iata_city_code,
        #     fly_to=destination.get("iataCode"),
        #     date_from=tomorrow.isoformat(),
        #     date_to=tomorrow_plus_six_months.isoformat(),
        #     nights_in_dst_from=destination.get("minNights", 1),
        #     nights_in_dst_to=destination.get("maxNights", 1),
        # )

        # If min_price less than present_price, update google sheet
        # if len(flights) > 0:
        #     cheapest_flight = flights[0]
        #     if cheapest_flight.get("price") < destination.get("lowestPrice", 1000):
        #         departure_date = cheapest_flight.get("route")[0].get("local_departure")
        #         return_date = cheapest_flight.get("route")[-1].get("local_arrival")

        #         # Send email
        #         email_text = notification_manager.format_email(cheapest_flight)
        #         notification_manager.send_email(
        #             recipient_email=email_to,
        #             subject=email_text.get("subject"),
        #             body=email_text.get("message"),
        #         )

        #         # Update google sheet
        #         row_value["lowestPrice"] = cheapest_flight.get("price")
        #         row_value["departureDate"] = departure_date
        #         row_value["returnDate"] = return_date
        #         await data_manager.update_row(row_value)


if __name__ == "__main__":
    import os

    from dotenv import load_dotenv

    load_dotenv()
    FILE_NAME = "Flight Deals"
    TAB_NAME = "prices"
    ORIGN_CITY = "Pointe à pitre"
    EMAIL_TO = os.environ.get("EMAIL_RECIPIENT")

    async def main():
        await cheap_flight_scanner(
            file_name=FILE_NAME,
            tab_name=TAB_NAME,
            departure_city=ORIGN_CITY.replace(" ", "-"),
            email_to=EMAIL_TO,
        )

    asyncio.run(main())
