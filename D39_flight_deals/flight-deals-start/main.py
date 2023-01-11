# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import date, datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


def cheap_flight_scanner(
    file_name: str, tab_name: str, origin_city: str, email_to: str
) -> None:
    """Scan for cheapest flights"""
    data_manager = DataManager(file_name=file_name, tab_name=tab_name)
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    destinations = data_manager.get_tab_data()
    origin_city_iata_code = flight_search.get_iata_city_code(origin_city)

    for destination in destinations:
        print(f"Scanning flights to {destination.get('city')}")
        destination_city_iata_code = flight_search.get_iata_city_code(
            destination.get("city")
        )
        row_value = {
            "iataCode": destination_city_iata_code,
            "id": destination.get("id"),
        }
        # Update the city IATA code
        data_manager.update_row(row_value)

        # TODO: For each destination, search flights date_from = tomorrow, date_to = tomorrow + 180
        tomorrow = date.today() + timedelta(days=1)
        tomorrow_plus_six_months = tomorrow + timedelta(days=180)
        # print(f"{tomorrow}\n{tomorrow_plus_six_months}")

        flights = flight_search.search(
            fly_from=origin_city_iata_code,
            fly_to=destination_city_iata_code,
            date_from=tomorrow.isoformat(),
            date_to=tomorrow_plus_six_months.isoformat(),
            nights_in_dst_from=destination.get("minNights", 1),
            nights_in_dst_to=destination.get("maxNights", 1),
        )

        # If min_price less than present_price, update google sheet
        if len(flights) > 0:
            cheapest_flight = flights[0]
            if cheapest_flight.get("price") < destination.get("lowestPrice"):
                departure_date = cheapest_flight.get("route")[0].get("local_departure")
                return_date = cheapest_flight.get("route")[-1].get("local_arrival")

                # Send email
                email_text = notification_manager.format_email(cheapest_flight)
                notification_manager.send_email(
                    recipient_email=email_to,
                    subject=email_text.get("subject"),
                    message=email_text.get("message"),
                )

                # Update google sheet
                row_value["lowestPrice"] = cheapest_flight.get("price")
                row_value["departureDate"] = departure_date
                row_value["returnDate"] = return_date
                data_manager.update_row(row_value)


if __name__ == "__main__":
    import os

    from dotenv import load_dotenv

    load_dotenv()
    FILE_NAME = "Flight Deals"
    TAB_NAME = "prices"
    ORIGN_CITY = "PARIS"
    EMAIL_TO = os.environ.get("EMAIL_RECIPIENT")

    cheap_flight_scanner(
        file_name=FILE_NAME,
        tab_name=TAB_NAME,
        origin_city=ORIGN_CITY,
        email_to=EMAIL_TO,
    )
