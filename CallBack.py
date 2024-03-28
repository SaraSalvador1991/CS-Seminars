import random

class TemperatureSensor:
    def __init__(self):
        self.current_temperature = 0
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def get_temperature(self):
        return self.current_temperature

    def simulate_temperature_change(self):
        new_temperature = random.uniform(-10, 40)  # Simulating temperature changes
        if abs(new_temperature - self.current_temperature) >= 5:
            self.current_temperature = new_temperature
            if self.callback:
                self.callback(self.current_temperature)

def temperature_change_callback(temperature):
    print(f"Temperature changed: {temperature} degrees")

if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.set_callback(temperature_change_callback)

    # Simulate temperature changes
    for _ in range(20):
        sensor.simulate_temperature_change()
