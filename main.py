class Car:
    def __init__(self, brand, model, production_year, color, horse_power):
        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.color = color
        self.horse_power = horse_power
        self.is_sport_car = False

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_production_year(self):
        return self.production_year

    def get_color(self):
        return self.color

    def get_horse_power(self):
        return self.horse_power

    def is_sporty(self):
        return self.is_sport_car

    def set_color(self, new_color):
        if new_color != self.color:
            self.color = new_color
            return True
        else:
            return False

    def set_sporty(self, is_sport_car):
        self.is_sport_car = is_sport_car

    def change_color(self, new_color):
        if new_color != self.color:
            self.color = new_color
            return True
        else:
            return False

    def increase_horse_power(self, hp):
        if hp > 0:
            self.horse_power += hp
            return True
        else:
            return False

