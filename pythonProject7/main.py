import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()
    def get_car(self):
        self.car = Auto(brand_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
           if self.satiety > 100:
               self.satiety = 100
               return


    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clear_home(self):
        pass
    def to_repair(self):
        pass
    def indexes_day(self, day):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move....')
            return False
class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {'Java': {'salary': 50, "gladness_less": 10},
            'C++': {'salary': 80, "gladness_less": 5},
            'Python': {'salary': 30, "gladness_less": 8},
            'Rust': {'salary': 60, "gladness_less": 6}}




brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 15},
                'Lada': {'fuel': 70, 'strength': 20, 'consumption': 8},
                'Volvo': {'fuel': 90, 'strength': 150, 'consumption': 6},
                'Ford': {'fuel': 50, 'strength': 120, 'consumption': 12}}
print(brand_of_car.keys())
print(list(brand_of_car))