## flight class
## Author: Atanas Chelibashki
## Date: 26/09/2023
## Version 1.0
class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
    def __str__(self):
        return f"{self.flight_number} {self.departure_airport} {self.arrival_airport} {self.departure_time} {self.arrival_time} "

    def get_flight_number(self):
        return self.flight_number

    def get_departure_airport(self):
        return self.departure_airport

    def get_arrival_airport(self):
        return self.arrival_airport

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def set_departure_airport(self, departure_airport):
        self.departure_airport = departure_airport

    def set_arrival_airport(self, arrival_airport):
        self.arrival_airport = arrival_airport

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time