class Car:
    def __init__(self,a,b,c):
        self.make = a
        self.model = b
        self.year = c
        self.odometer_reading = 600
        print('----------父类构造函数-----------')
    def get_descriptive(self):
        long_name = f"{self.year}{self.make}{self.model}"
        return long_name.title()
    def read_odometer(self):
        print(self.odometer_reading)
    def updata_odometer(self,d):
        if d > self.odometer_reading:
            self.odometer_reading = d
        else:
            print('里程表不能调哦')
    def increment_odometer(self,e):
        self.odometer_reading = self.odometer_reading + e

class ElectricCar(Car):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
        print('----------子类构造函数-----------')

my_BYD = ElectricCar('比亚迪','汉EV',2022)
print(my_BYD.make,my_BYD.model,my_BYD.year)











































































