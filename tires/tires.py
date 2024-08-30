from abc import ABC, abstractmethod

class Tires(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass