# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import get_sheet_data, update_row
from flight_search import get_iata_city_code

FILE_NAME = "Flight Deals"
TAB_NAME = "prices"
FLY_FROM_IATA_CODE = "PAR"

# Read the list of destinations
google_sheet_name = "Flight Deals"
tab_name = "prices"
destinations = get_sheet_data(FILE_NAME, TAB_NAME)

for destination in destinations:
    row_value = {
        "iataCode": get_iata_city_code(destination.get("city")),
        "id": destination.get("id"),
    }
    # Update the city IATA code
    update_row(FILE_NAME, TAB_NAME, row_value)

    # TODO: For each destination, search flights date_from = tomorrow, date_to = tomorrow + 180

# TODO: For each search result, find the min price
# TODO: If min_price less than present_price, update google sheet
# TODO: Send email notification
