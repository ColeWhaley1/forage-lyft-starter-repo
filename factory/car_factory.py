from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigans import Carrigans
from tires.octoprimes import Octoprimes


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigans([0, 0, 0, 0])
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigans([0, 0, 0, 0])
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigans([0, 0, 0, 0])
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_rorsach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = Octoprimes([0, 0, 0, 0])
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = Octoprimes([0, 0, 0, 0])
        return Car(engine, battery, tires)