import pytest
from firmware import Sensor, get_sensor_data

# Mocking sensor behavior
class MockSensor:
    def __init__(self, temperature=25.5, status="OK", min_value=0, max_value=100):
        self.temperature = temperature
        self.status = status
        self.min_value = min_value
        self.max_value = max_value

    def read_temperature(self):
        return self.temperature

    def check_status(self):
        return self.status

def test_sensor_read_success():
    """Test sensor reads successfully when status is OK."""
    mock_sensor = MockSensor(temperature=22.5, status="OK")
    result = get_sensor_data(mock_sensor)
    assert "Sensor Status: OK" in result
    assert "Temperature: 22.5°C" in result

def test_sensor_read_error():
    """Test sensor read fails when status is ERROR."""
    mock_sensor = MockSensor(status="ERROR")
    result = get_sensor_data(mock_sensor)
    assert result == "Sensor Error: Unable to read data"

def test_sensor_temperature_out_of_range():
    """Test sensor returns out-of-range temperature."""
    mock_sensor = MockSensor(temperature=150, status="OK")  # Out of range
    result = get_sensor_data(mock_sensor)
    assert result == "Temperature out of range"

def test_sensor_temperature_out_of_range_fail():
    """Failing test: expecting valid temperature but get out-of-range."""
    mock_sensor = MockSensor(temperature=150, status="OK")  # Intentionally out of range
    result = get_sensor_data(mock_sensor)
    # This assertion will fail, because 150 is out of range, but we are expecting a valid result
    assert "Sensor Status: OK" in result
