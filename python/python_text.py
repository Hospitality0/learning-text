class Dog:
    def __init__(self,name,age):
        self.NM = name
        self.AG = age
        print('---------父类构造函数-----------')
    def sit(self):
        print(f'{self.NM} is sitting')
    def roll_over(self):
        print(f'{self.NM} is rolling')
    def chang_pet_name(self,a):
        self.NM = a



class small_Dog(Dog):
    def __init__(self,name,age):
        super(small_Dog,self).__init__('大挼',2)
        self.NM = name
        self.AG = age
        print('-----------子类构造函数----------------')


mysmalldog = small_Dog('小挼',1)








'''
mydog = Dog('rua',6)
mydog.chang_pet_name('崽崽')
print(mydog.NM)
print(mydog.AG)
mydog.sit()
mydog.roll_over()

yourdog = Dog('胖胖',21)
yourdog.chang_pet_name('乌龟')
print(yourdog.NM)
print(yourdog.AG)
yourdog.sit()
yourdog.roll_over()'''




















