import unittest
from datetime import datetime, date, time

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 20000

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):

        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_engine_should_not_be_serviced_equals_threshold(self):

        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 20000

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):

        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_engine_should_not_be_serviced_equals_threshold(self):

        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)

        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):

        warning_light_on = False

        engine = SternmanEngine(warning_light_on)

        self.assertFalse(engine.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):

        last_service_date = date(2022, 1, 1)
        mock_current_date = date(2024, 1, 2)

        battery = SpindlerBattery(last_service_date, mock_current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):

        last_service_date = date(2024, 1, 1)
        mock_current_date = date(2024, 1, 2)

        battery = SpindlerBattery(last_service_date, mock_current_date)

        self.assertFalse(battery.needs_service())

    def test_battery_should_not_be_serviced_equals_threshold(self):

        last_service_date = date(2022, 1, 1)
        mock_current_date = date(2024, 1, 1)

        battery = SpindlerBattery(last_service_date, mock_current_date)

        self.assertFalse(battery.needs_service())

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):

        last_service_date = date(2020, 1, 1)
        mock_current_date = date(2024, 1, 2)

        battery = NubbinBattery(last_service_date, mock_current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):

        last_service_date = date(2024, 1, 1)
        mock_current_date = date(2024, 1, 2)

        battery = NubbinBattery(last_service_date, mock_current_date)

        self.assertFalse(battery.needs_service())

    def test_battery_should_not_be_serviced_equals_threshold(self):

        last_service_date = date(2020, 1, 1)
        mock_current_date = date(2024, 1, 1)

        battery = NubbinBattery(last_service_date, mock_current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
