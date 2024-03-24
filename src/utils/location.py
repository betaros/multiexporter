import reverse_geocode


class Location:
    def __init__(self):
        self.lat = 53.9288531
        self.lon = 12.3409471
        self.location = "Laage"

    def set_position(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude
        coordinates = ((self.lat, self.lon),)

        self.location = reverse_geocode.search(coordinates)[0]['city']
        print(self.location)

    def get_position(self):
        return self.lat, self.lon, self.location
