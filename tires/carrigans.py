
from tires.tires import Tires

class Carrigans(Tires):

    def __init__(self, wear):
        self.wear = wear

    def needs_service(self) -> bool:
        for tire_wear in self.wear:
            if tire_wear >= 0.9:
                return True
        return False