class Sensor:
    def __init__(self):
        self.current_temperature = 0
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def simulate_temperature_change(self):
        # Simulazione dei cambiamenti di temperatura
        pass

import random
class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__()  # do i need to defy here again set_callback, or if i dont write anything it talkes it as in Sensor?

    def simulate_temperature_change(self):
        new_temperature = random.uniform(-10, 40)  # Simulating temperature changes
        if abs(new_temperature - self.current_temperature) >= 5:  # if the delta temperature is greater/equal to 5, print new temperature
            self.current_temperature = new_temperature
            if self.callback:  # if not None (defined before in set_callback)
                self.callback(self.current_temperature)  # call of the callback function

    def new_temperature(self, temperature):
        print("Temperature has changed of more than 5 degrees. New Temperature:", temperature)


if __name__ == "__main__":
    temperature_sensor = TemperatureSensor()
    temperature_sensor.set_callback(temperature_sensor.new_temperature)

    for _ in range(20):
        temperature_sensor.simulate_temperature_change()