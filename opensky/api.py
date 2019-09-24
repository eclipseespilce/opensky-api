import requests
import math

from .config import Config
from .exceptions import OpenSkyUnreachableError


def get_airplanes_list():
    response = requests.get('https://opensky-network.org/api/states/all')

    if response.status_code != 200:
        raise OpenSkyUnreachableError(f"OpenSky answered with {response.status_code} code")

    airplanes_list = []
    airplanes_info = response.json()
    for airplane_info in airplanes_info["states"]:
        if airplane_info[5] is not None and airplane_info[6] is not None:
            if __close_to_start_point(airplane_info[5], airplane_info[6]):
                airplanes_list.append({
                    'name': airplane_info[1] if airplane_info[1] is not None else 'unnamed',
                    'longitude': airplane_info[5],
                    'latitude': airplane_info[6]
                })

    return airplanes_list


def __close_to_start_point(longitude, latitude):
    lat1, lon1 = latitude, longitude
    lat2, lon2 = Config.OPEN_SKY_START_POINT_LATITUDE, Config.OPEN_SKY_START_POINT_LONGITUDE

    degrees_to_radians = math.pi / 180.0

    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians

    theta1 = lon1 * degrees_to_radians
    theta2 = lon2 * degrees_to_radians

    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
           math.cos(phi1) * math.cos(phi2))
    arc = math.acos(cos)
    distance_between_points = arc * Config.OPEN_SKY_EARTH_RADIUS
    print(distance_between_points)
    return distance_between_points < Config.OPEN_SKY_FLY_DISTANCE_FROM_START_POINT
