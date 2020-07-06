class Car:
    def __init__(self, engine):
        self.engine = engine

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        print('process install....')
        if isinstance(engine, Engine):
            self.__engine = engine
            print('Seccessfully install')

    def move(self):
        self.engine.accelerate()



class Engine():
    def accelerate(self):
        pass

class PetrolEngine(Engine):
    def accelerate(self):
        print("Вррруммм, я бензиновый двигатель")

class DizelEngine(Engine):
    def accelerate(self):
        print("Вррруммм, я дизельный двигатель")

class ElectricEngine(Engine):
    def accelerate(self):
        print("Вррруммм, я электрический двигатель")

class Nogi:
    def accelerate(self):
        print('Иду ногами')

tesla = Car(ElectricEngine())

tesla.move()

print('Tesla fail, change electric on dizel engine')

tesla.engine = DizelEngine()

tesla.move()

tesla.engine = Nogi()

tesla.move()


