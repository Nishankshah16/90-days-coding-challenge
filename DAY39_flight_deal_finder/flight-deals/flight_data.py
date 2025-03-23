class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(flight):
    if flight is None or not flight['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
    first = flight["data"][0]
    low_price = float(first["price"]["grandTotal"])
    origin = first["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(low_price, origin, destination, out_date, return_date)

    for flight in flight['data']:
        price = float(flight["price"]["grandTotal"])
        if price < low_price:
            low_price = price
            origin = first["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = first["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = first["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = first["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            cheapest_flight = FlightData(low_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{low_price}")

    return cheapest_flight

        
