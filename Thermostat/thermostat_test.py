import unittest

from Thermostat.thermostat import Thermostat


class ThermostatTest(unittest.TestCase):

    def test_get_hour(self):
        # arrange
        thermostat = Thermostat(14, 20)
        # act and assert
        self.assertEqual(thermostat.get_hour(), 14)

    def test_get_temperature(self):
        # arrange
        thermostat = Thermostat(14, 20)
        # act and assert
        self.assertEqual(thermostat.get_temperature(), 20)

    def test_set_hour(self):
        # arrange
        thermostat = Thermostat(14, 20)
        thermostat.set_hour(15)
        # act and assert
        self.assertEqual(thermostat.get_hour(), 15)
        # arrange
        thermostat.set_hour(245)
        # act and assert
        self.assertEqual(thermostat.get_hour(), 0)

    def test_set_temperature(self):
        # arrange
        thermostat = Thermostat(14, 20)
        thermostat.set_temperature(15)
        # act and assert
        self.assertEqual(thermostat.get_temperature(), 15)
        # arrange
        thermostat.set_temperature(245)
        # act and assert
        self.assertEqual(thermostat.get_temperature(), 15)

    # def test_get_current_required_temperature(self):

    def test_set_point(self):
        # arrange
        thermostat = Thermostat(14, 20)
        thermostat.set_hour(17)
        thermostat.add_set_point(start_hour=15, stop_hour=20, temperature=21)
        # act and assert
        self.assertEqual(thermostat.get_temperature(), 21)
        # arrange
        thermostat.set_temperature(18)
        # act and assert
        self.assertEqual(thermostat.get_temperature(), 21)


if __name__ == '__main__':
    unittest.main()
