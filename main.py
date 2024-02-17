from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(Vehicle):
    def __init__(self, max_speed, current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.engine_started = False
    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            return "Car started"
        else:
            return "Car is alrrady running"
    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            return "Car stopped"
        else:
            return "Car iis already stopped"

class SportCar(Car):
    def __init__(self,max_speed, current_speed):
        super().__init__(max_speed, current_speed)
    def start_engine(self):
        parent_start = super().start_engine()
        return f"{parent_start} max speed: {self.max_speed}"
    def stop_engine(self):
        parent_stop = super().stop_engine()
        self.current_speed = 0
        return f"{parent_stop} current speed: {self.current_speed}"




