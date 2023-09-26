## trip class
## Author: Atanas Chelibashki
## Date: 26/09/2023
## Version 1.0

class Trip:
    def __init__(self, trip_id, user, destinations=None):
        self.trip_id = trip_id
        self.user = user
        self.destinations = destinations or []

    def add_destination(self, destination):
        self.destinations.append(destination)

    # Add other methods as needed
