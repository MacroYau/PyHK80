import pyproj

# Definitions from https://epsg.io/2326
HK80_PROJ = pyproj.Proj("+proj=tmerc +lat_0=22.31213333333334 +lon_0=114.1785555555556 +k=1 +x_0=836694.05 +y_0=819069.8 +ellps=intl +towgs84=-162.619,-276.959,-161.764,0.067753,-2.24365,-1.15883,-1.09425 +units=m +no_defs ")
HK80_BOUND_N_MIN = 799130.01
HK80_BOUND_N_MAX = 848940.16
HK80_BOUND_E_MIN = 793259.70
HK80_BOUND_E_MAX = 870525.78
HK80_WGS84_LAT_MIN = 22.13
HK80_WGS84_LAT_MAX = 22.58
HK80_WGS84_LNG_MIN = 113.76
HK80_WGS84_LNG_MAX = 114.51

# Definition from https://epsg.io/4326
WGS84_PROJ = pyproj.Proj("+proj=longlat +datum=WGS84 +no_defs ")


def convert_hk80_to_wgs84(northing, easting):
    """
    Converts a set of geographical coordinates using the Hong Kong 1980 Grid
    system to the WGS 84 latitude and longitude.

    Parameters
    ----------
    northing : float
        Northing in meters.
    easting : float
        Easting in meters.

    Raises
    ------
    ValueError
        If the northing or easting value is out of the projection range of the
        Hong Kong 1980 Grid system.

    Returns
    -------
    tuple
        Decimal WGS 84 coordinates in the `(latitude, longitude)` format.
    """
    if (HK80_BOUND_N_MIN <= northing <= HK80_BOUND_N_MAX) and \
       (HK80_BOUND_E_MIN <= easting <= HK80_BOUND_E_MAX):
        return _convert_coordinates(HK80_PROJ, WGS84_PROJ, (easting, northing))
    else:
        raise ValueError("Northing or easting value is out of range")


def convert_wgs84_to_hk80(latitude, longitude):
    """
    Converts a set of WGS 84 latitude and longitude coordinates to the Hong Kong
    1980 Grid system representation.

    Parameters
    ----------
    latitude : float
        Latitude in decimal format. Positive values refer to latitudes to the
        north of the equator, negative otherwise. 
    longitude : float
        Longitude in decimal format. Positive values refer to longitudes to the
        east of the prime meridian.

    Raises
    ------
    ValueError
        If the northing or easting value is out of the projection range of the
        Hong Kong 1980 Grid system.

    Returns
    -------
    tuple
        Hong Kong 1980 Grid system coordinates in the `(northing, easting)`
        format.
    """
    if (HK80_WGS84_LAT_MIN <= latitude <= HK80_WGS84_LAT_MAX) and \
       (HK80_WGS84_LNG_MIN <= longitude <= HK80_WGS84_LNG_MAX):
        return _convert_coordinates(WGS84_PROJ, HK80_PROJ, (longitude, latitude))
    else:
        raise ValueError("Latitude or longitude value is out of range")


def _convert_coordinates(in_proj, out_proj, coordinates):
    x, y = pyproj.transform(in_proj, out_proj, coordinates[0], coordinates[1])
    return (y, x)
