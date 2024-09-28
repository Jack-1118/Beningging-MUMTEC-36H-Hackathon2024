import random
import time

class Sensor:
    def __init__(self, min_value=0, max_value=100):
        self.min_value = min_value
        self.max_value = max_value

    def read_temperature(self):
        """Simulate reading temperature from a sensor."""
        time.sleep(0.1)  # Mimic delay in sensor reading
        return round(random.uniform(self.min_value, self.max_value), 2)

    def check_status(self):
        """Simulate checking sensor status."""
        return "OK" if random.random() > 0.1 else "ERROR"

def get_sensor_data(sensor):
    """Mimic a firmware function that reads and processes sensor data."""
    status = sensor.check_status()
    if status == "OK":
        temperature = sensor.read_temperature()
        if not (sensor.min_value <= temperature <= sensor.max_value):
            return "Temperature out of range"
        return f"Sensor Status: {status}, Temperature: {temperature}°C"
    else:
        return "Sensor Error: Unable to read data"
