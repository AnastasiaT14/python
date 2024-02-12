
class Heart:
    def __init__(self, output):
        self.output = output

    def health_status(self):
        return "High blood pressure" if self.output > 70\
            else "Feeling good"


class Brain:
    def __init__(self, load):
        self.load = load

    def brain_state(self):
        return "Tired" if self.load > 90 \
            else "Rested"
class Leg:
    def __init__(self, speed):
        self.speed = speed

    def motion_status(self):
            if self.speed > 10:
                return "Running"
            elif 0 < self.speed <= 10:
                return "Walking"
            else:
                return "Standing"

class Person:
    def __init__(self, heart_output, brain_load, leg_speed):
                self.heart = Heart(heart_output)
                self.brain = Brain(brain_load)
                self.leg = Leg(leg_speed)


person_instance = Person(heart_output=75, brain_load=85, leg_speed=8)

