
class Point():
    def __init__(self, name, latitude, longitude):
        if not isinstance(name, str):
            raise TypeError('Name is not a String')
        self._name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination")

        self._latitude = latitude
        self._longitude = longitude

    def get_lat_long(self):
        return (self.latitude, self.longitude)
