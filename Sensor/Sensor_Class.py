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
        if abs(new_temperature - self.current_temperature) >= 5: # if the delta temperature is greater/equal to 5, print new temperature
            self.current_temperature = new_temperature
            if self.callback: # if not None (defined before in set_callback)
                self.callback(self.current_temperature) # call of the callback function

def temperature_change_callback(temperature):
    print(f"Temperature changed: {temperature} degrees")

class User:
    def __init__(self, name):
        self.name = name

    def notify_temperature_change(self, temperature):
        print(f"{self.name} has been notified of temperature change: {temperature} degrees")

if __name__ == "__main__":
    sensor = TemperatureSensor()
    user = User("Sara")
    sensor.set_callback(user.notify_temperature_change)

    # Simulate temperature changes
    for _ in range(20):
        sensor.simulate_temperature_change()