# HK80

Hong Kong 1980 Grid coordinates conversion library in Python. This library 
provides a simple API for coordinates conversion between Hong Kong 1980 Grid 
and WGS 84. Underlying conversions are performed using [`pyproj`](https://pyproj4.github.io/pyproj).


## Installation

```shell
pip install hk80
```


## Usage

```python
>>> from hk80 import LatLon, HK80
>>> hku = LatLon(22.284034, 114.137814).to_hk80()
>>> (hku.northing, hku.easting)
(816128.2739028323, 832242.6232703187)
>> (hku.x, hku.y)
(832242.6232703187, 816128.2739028323)
>>> hku = HK80(northing=816128, easting=832243).to_wgs84()
>>> (hku.latitude, hku.longitude)
(22.284031525857237, 114.13781766034742)
```


## License

MIT
