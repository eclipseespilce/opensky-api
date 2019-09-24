from mock import patch
import pytest

from opensky.api import __close_to_start_point, get_airplanes_list
from opensky.exceptions import OpenSkyUnreachableError
from opensky.config import Config

def test_open_sky_service_unreachable_should_raise_exception():
    class MockResponse:
        def __init__(self, data, status_code):
            self.data = data
            self.status_code = status_code

    with patch('requests.get') as mock:
        mock.return_value = MockResponse('', 502)
        with pytest.raises(OpenSkyUnreachableError):
            get_airplanes_list()


def test_further_than_distance_from_start_point():
    assert __close_to_start_point(-Config.OPEN_SKY_START_POINT_LONGITUDE,
                                  -Config.OPEN_SKY_START_POINT_LATITUDE) is False


def test_closer_than_distance_from_start_point():
    assert __close_to_start_point(Config.OPEN_SKY_START_POINT_LONGITUDE,
                                  Config.OPEN_SKY_START_POINT_LATITUDE) is True
