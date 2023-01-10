# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import date, datetime, timedelta

from data_manager import DataManager
from flight_search import flight_search, get_iata_city_code

FILE_NAME = "Flight Deals"
TAB_NAME = "prices"
ORIGN_CITY = "PARIS"

# Read the list of destinations
FILE_NAME = "Flight Deals"
TAB_NAME = "prices"
data_manager = DataManager(file_name=FILE_NAME, tab_name=TAB_NAME)
destinations = data_manager.get_tab_data()

origin_city_iata_code = get_iata_city_code(ORIGN_CITY)

for destination in destinations:
    destination_city_iata_code = get_iata_city_code(destination.get("city"))
    row_value = {
        "iataCode": destination_city_iata_code,
        "id": destination.get("id"),
    }
    # Update the city IATA code
    data_manager.update_row(row_value)

    # TODO: For each destination, search flights date_from = tomorrow, date_to = tomorrow + 180
    tomorrow = date.today() + timedelta(days=1)
    tomorrow_plus_six_months = tomorrow + timedelta(days=180)
    print(f"{tomorrow}\n{tomorrow_plus_six_months}")

    # flight_search(
    #     fly_from=origin_city_iata_code,
    #     fly_to=destination_city_iata_code,
    #     date_from=tomorrow.isoformat(),
    #     date_to=tomorrow_plus_six_months.isoformat(),
    # )

# TODO: For each search result, find the min price
# TODO: If min_price less than present_price, update google sheet
# TODO: Send email notification
