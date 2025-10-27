class Car:

    def fill_up(self):
        raise NotImplementedError

class PetrolCar(Car):
  
    @classmethod
    def fill_up(cls):
        return f"Fill up {cls.__name__}"

class ElectricCar(Car):
    @classmethod
    def fill_up(cls):
        return f"Charge the battery {cls.__name__}"

cars = [PetrolCar, ElectricCar] # Liste von Klassen-Objekten

for c in cars:
    print(c.fill_up()) #cls = PetrolCar ,cls = ElectricCar   ->KlassenObjekte
#Bei PetrolCar.fill_up() wird cls = PetrolCar
