## Booking class
## Author: Atanas Chelibashki
## Date: 26/09/2023
## Version 1.0
class Booking:
    def __init__(self, booking_id, user, destinations=None, flights=None):
        self.booking_id = booking_id
        self.user = user
        self.destinations = destinations or []
        self.flights = flights or []

    def __str__(self):
        return f"{self.booking_id} {self.user} {self.destinations} {self.flights}"

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

    def set_booking_id(self, booking_id):
        self.booking_id = booking_id

    def set_user(self, user):
        self.user = user
