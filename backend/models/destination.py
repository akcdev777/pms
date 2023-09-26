## destination class
## Author: Atanas Chelibashki
## Date: 26/09/2023
## Version 1.0
from random import random


class Destination:

    def __init__(self, name, description=None, flights=None):
        self.destination_id = None
        self.name = name
        self.description = description
        self.flights = flights or []
        self.set_destination_id()

    def set_destination_id(self):
        self.destination_id = random.randint(1, 1000000)

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_flights(self):
        return self.flights

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_flights(self, flights):
        self.flights = flights
