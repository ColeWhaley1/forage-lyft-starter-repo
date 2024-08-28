from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    # It is not specified how you determine when a battery needs service
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if self.current_date > service_threshold_date:
            return True
        return False