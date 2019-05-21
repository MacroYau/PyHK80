from hk80 import coordinates


class LatLon:
    """
    Representation of WGS 84 latitude and longitude.
    """

    def __init__(self, latitude, longitude):
        """
        Constructor with latitude and longitude.

        Parameters
        ----------
        latitude : float
            WGS 84 latitude in decimal degrees.
        longitude : float
            WGS 84 longitude in decimal degrees.
        """
        self.latitude = latitude
        self.longitude = longitude

    @property
    def x(self):
        return self.longitude

    @property
    def y(self):
        return self.longitude

    def __str__(self):
        return "LatLon(latitude=%f, longitude=%f))" % (self.latitude, self.longitude)

    def to_hk80(self):
        """
        Converts to Hong Kong 1980 Grid system coordinates.

        Returns
        -------
        HK80
            Coordinates object with latitude and longitude converted to the 
            Hong Kong 1980 Grid system coordinates.
        """
        northing, easting = coordinates.convert_wgs84_to_hk80(
            latitude=self.latitude,
            longitude=self.longitude
        )
        return HK80(northing, easting)


class HK80:
    """
    Representation of Hong Kong 1980 Grid system northing and easting.
    """

    def __init__(self, northing, easting):
        """
        Constructor with northing and easting.

        Parameters
        ----------
        northing : float
            Hong Kong 1980 Grid system northing (y) in meters.
        easting : float
            Hong Kong 1980 Grid system easting (x) in meters.
        """
        self.northing = northing
        self.easting = easting

    @property
    def x(self):
        return self.easting

    @property
    def y(self):
        return self.northing

    def __str__(self):
        return "HK80(northing=%f, easting=%f)" % (self.northing, self.easting)

    def to_wgs84(self):
        latitude, longitude = coordinates.convert_hk80_to_wgs84(
            northing=self.northing,
            easting=self.easting
        )
        return LatLon(latitude, longitude)
