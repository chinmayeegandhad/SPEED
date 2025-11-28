import pytest
from speed import calculate_speed

def test_calculate_speed():
    result = calculate_speed(200, 2)
    expected = 100
    assert result == expected


