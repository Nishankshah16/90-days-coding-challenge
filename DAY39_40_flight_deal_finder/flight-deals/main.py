from data_manager import DataManager
from flight_search import FlightSearch
import time
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

CITY_CODE = "LON"
data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

dest_details = data_manager.get_dest_data()
customer_details = data_manager.get_customer_emails()

customer_emails = [data['email'] for data in customer_details]

if dest_details[0]["iataCode"] == "":
    for data in dest_details:
        data["iataCode"]= flight_search.get_code(data["city"])
        time.sleep(2)
    # print(f"{dest_details}")

    data_manager.dest_data = dest_details
    data_manager.update_dest_code()
        
tommorrow = datetime.now() + timedelta(days = 1)
six_month = datetime.now() + timedelta(days = (6*30))

for data in dest_details:
    print(f"Getting flight for {data['city']}")
    flights = flight_search.check_flight(CITY_CODE, data['iataCode'], tommorrow, six_month)
    # print(flights)
    cheap_flight = find_cheapest_flight(flights)
    print(f"{data['city']}: £{cheap_flight.price}")

    time.sleep(2)

    if cheap_flight.price == 'N/A':
        print(f"No direct flight to {data['city']}. Looking for indirect flights...")
        stop_flights = flight_search.check_flight(CITY_CODE, data['iataCode'], tommorrow, six_month, is_direct=False)
        cheap_flight = find_cheapest_flight(flights)
        print(f"{data['city']}: £{cheap_flight.price}")

    if cheap_flight.price != 'N/A' and cheap_flight.price < data['lowestPrice']:
        print(f"Lower price flight found to {data['city']}!")
        if cheap_flight.stops == 0:
            message = f"Low price alert! Only £ {cheap_flight.price} to fly direct "\
                      f"from {cheap_flight.origin_airport} to {cheap_flight.destination_airport}, "\
                      f"on {cheap_flight.out_date} until {cheap_flight.return_date}."
        else:
            message = f"Low price alert! Only £ {cheap_flight.price} to fly "\
                      f"from {cheap_flight.origin_airport} to {cheap_flight.destination_airport}, "\
                      f"with {cheap_flight.stops} stop(s) "\
                      f"departing on {cheap_flight.out_date} and returning on {cheap_flight.return_date}."
        #### send sms ####
        notification.send_msg(msg_body=message)

        #### send mails ####
        notification.send_mail(customer_emails, message)


