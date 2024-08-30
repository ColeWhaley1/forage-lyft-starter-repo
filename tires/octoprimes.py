
from tires.tires import Tires

class Octoprimes(Tires):

    def __init__(self, wear):
        self.wear = wear

    def needs_service(self) -> bool:
        return sum(self.wear) >= 3