## Booking class
## Author: Atanas Chelibashki
## Date: 26/09/2023
## Version 1.0

from random import random
class Booking:
    def __init__(self, user, destinations=None, flights=None):
        self.booking_id = None
        self.user_id = user.id
        self.destinations = destinations or []
        self.set_booking_id(self)
    def __str__(self):
        return f"{self.booking_id} {self.user} {self.destinations} {self.flights}"

    def set_booking_id(self):
        self.booking_id = random.randint(1, 20000000, 2)

    def add_destination(self, destination):
        self.destinations.append(destination)

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_booking_id(self):
        return self.booking_id

    def get_user(self):
        return self.user

    def get_destinations(self):
        return self.destinations

    def get_flights(self):
        return self.flights

    def set_user(self, user):
        self.user = user
