import random
class Thermometer:
    def __init__(self):
        self.is_on = False
        self.current_temperature = 34.0

    def measure_temp(self):
        if self.is_on:
            self.current_temperature = round(random.uniform(34.0,42.0),1)
        else:
            print("Cannot measure temperature when thermometer is off.")
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False

    def display_temp(self):
        if self.is_on:
            if self.current_temperature >= 37.0 and self.current_temperature < 41.0:
                print(f"Temperature: {self.current_temperature} (fever)")
            elif self.current_temperature >= 41.0:
                print((f"Temperature: {self.current_temperature} (CRITICAL TEMPERATURE!!!)"))
            else:
                print(f"Temperature: {self.current_temperature}")
        elif not self.is_on:
            print("Thermometer turned off.")