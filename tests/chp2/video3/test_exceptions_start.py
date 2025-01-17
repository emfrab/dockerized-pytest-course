from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 12.11386, -748.56522)
    assert str(exp.value) == 'Invalid latitude, longitude combination'

    with pytest.raises(TypeError) as exp:
        Point(5456, 54.56586, 12.44221)
    assert str(exp.value) == 'Name is not a String'
