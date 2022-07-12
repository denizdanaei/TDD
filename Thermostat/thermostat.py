class Thermostat:
    def __init__(self, hour: int = None, temperature: int = None) -> None:
        self.hour = None
        self.set_hour(hour)
        self.lock_temperature = False
        self.temperature = None
        self.set_temperature(temperature)

    def set_hour(self, hour: int) -> None:
        self.lock_temperature = False
        if 0 <= hour <= 24:
            self.hour = hour
        else:
            print("Out of bound! Hour must be between 0 and 24. Hour set to Zero.")
            self.hour = 0

    def set_temperature(self, temperature: int) -> None:

        if self.lock_temperature:
            print("Temperature is locked to {}".format(self.get_temperature()))
        elif 15 <= temperature <= 30:
            self.temperature = temperature
        else:
            print("Temperature can only be between 15 and 30. Temperature set to 15.")
            self.temperature = 15

    def get_hour(self) -> int:
        return self.hour

    def get_temperature(self) -> int:
        return self.temperature

    def add_set_point(self, start_hour: int, stop_hour: int, temperature: int) -> None:
        if start_hour <= self.hour <= stop_hour:
            self.set_temperature(temperature)
            self.lock_temperature = True
