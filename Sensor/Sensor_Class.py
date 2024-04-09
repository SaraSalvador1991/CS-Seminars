import random

class TemperatureSensor:
    def __init__(self):
        self.current_temperature = 0
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def simulate_temperature_change(self):
        new_temperature = random.uniform(-10, 40)  # Simulating temperature changes
        if abs(new_temperature - self.current_temperature) >= 5: # if the delta temperature is greater/equal to 5, print new temperature
            self.current_temperature = new_temperature
            if self.callback: # if not None (defined before in set_callback)
                self.callback(self.current_temperature) # call of the callback function


class User:
    def __init__(self, name):
        self.name = name

    def notify_temperature_change(self, temperature):
        print(f"The user {self.name} has been notified of temperature change: {temperature} degrees")

if __name__ == "__main__":
    sensor = TemperatureSensor()
    user = User("Sara")
    sensor.set_callback(user.notify_temperature_change) # here we set the callback function for sensor.
    # when the temperature changes of more (equal) than 5 degrees and simulate_temperature_change is called,
    # it activates notify_temperature_change to notify user of the change of temperature

    # Simulate temperature changes
    for _ in range(20):
        sensor.simulate_temperature_change()

