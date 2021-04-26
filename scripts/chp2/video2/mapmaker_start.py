class Point():
    
    def __init__(self, name, lat, long):
        self._name = name
        self._latitude = lat
        self._longitude = long


    def get_lat_long(self):
        return (self._latitude, self._longitude)