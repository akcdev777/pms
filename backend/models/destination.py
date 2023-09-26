## destination class
## Author: Atanas Chelibashki
## Date: 26/09/2023
## Version 1.0
class Destination:
    def __init__(self, name, description, flights=None):
        self.name = name
        self.description = description
        self.flights = flights or []

    def add_flight(self, flight):
        self.flights.append(flight)

    # Add other methods as needed
