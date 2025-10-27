class Car:

    def fill_up(self):
        raise NotImplementedError

class PetrolCar(Car):
  
    def fill_up(self):
        return f"Fill up {self.__class__.__name__}"

class ElectricCar(Car):
    
    def fill_up(self):
        return f"Charge the battery {self.__class__.__name__}"

cars = [PetrolCar(), ElectricCar()]

for c in cars:
    print(c.fill_up())
