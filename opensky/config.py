import os


class Config:
    OPEN_SKY_START_POINT_LONGITUDE = float(os.environ.get('OPEN_SKY_MIDDLE_POINT_LONGITUDE', 13.41053))
    OPEN_SKY_START_POINT_LATITUDE = float(os.environ.get('OPEN_SKY_MIDDLE_POINT_LATITUDE', 52.52437))
    OPEN_SKY_FLY_DISTANCE_FROM_START_POINT = int(os.environ.get('OPEN_SKY_FLY_DISTANCE_FROM_START_POINT', 260))
    OPEN_SKY_EARTH_RADIUS = int(os.environ.get('OPEN_SKY_EARTH_RADIUS', 6371))
