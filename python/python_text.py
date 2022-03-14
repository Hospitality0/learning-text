file_name = 'C:\\Users\\kewei.song\\Desktop\\learning-text\\python\\text_files\\text.txt'
with open(file_name) as tmp:
    str = tmp.readlines()
for line in str:
    print(line.rstrip())






































'''
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
    def fill_gas_tank(self):
        print('超大500块钱油箱')


class Battery:
    def __init__(self,f):
        self.battery_size = f
    def describe_battery(self):
        print(f'电池大小：{self.battery_size}')






class ElectricCar(Car):
    def __init__(self,a,b,c):
        print('----------子类构造函数-----------')
        super().__init__(a,b,c)
        self.E_battery = Battery(75)
    def fill_gas_tank(self):
        print('电动车莫得油箱')



my_BYD = ElectricCar('比亚迪','汉EV',2022)
print(my_BYD.get_descriptive())
my_BYD.E_battery.describe_battery()
'''







































































