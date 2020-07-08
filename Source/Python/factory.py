class AbstractFactoryParts:
	"""Абстрактный класс частей включает методы установки двигателя, покраски и установки колес"""
	def engine(self):
		pass
	def paint(self):
		pass
	def wheels(self):
		pass

class AbstractCar:
	"""Абстрактный класс машины определяет установку фабрики частей и запускает кофигурацию"""
	def __init__(self,factory_parts : AbstractFactoryParts):
		self.factory_parts = factory_parts
		self.configurate()
	def configurate(self):
		pass

	@property
	def factory_parts(self):
		return self._factory_parts
	@factory_parts.setter
	def factory_parts(self, factory_parts : AbstractFactoryParts):
		self._factory_parts = factory_parts
	

class AbstractFactory:
	"""Абстрактный класс Фабрики который указывает на присутствие метода createCar"""
	@property
	def factory_parts(self):
		return self._factory_parts
	@factory_parts.setter
	def factory_parts(self, factory_parts : AbstractFactoryParts):
		self._factory_parts = factory_parts
	
	def createCar(self, type):
		pass

class Volkswagen:
	"""Конкретный производитель, позволяет установить фабрику через которую будут собираться автомобили"""
	def __init__(self, factory : AbstractFactory):
		self.factory = factory

	def getCar(self, type):
		return self.factory.createCar(type)


	@property
	def car(self):
		return self._car
	@car.setter
	def car(self, car : AbstractCar):
		self._car = car

	@property
	def factory(self):
		return self._factory
	@factory.setter
	def factory(self, factory : AbstractFactory):
		self._factory = factory


class RussianFactory(AbstractFactory):
	"""Конкретная фабрика, устанавливает фабрику запчастей для создания машин и определяет метод createCar"""
	def __init__(self):
		self.factory_parts = RussianFactoryParts()

	def createCar(self, type):
		if(type == "Golf"):
			return Golf(self.factory_parts)
		elif(type == "Passat"):
			return Passat(self.factory_parts)
		elif type == "Tiguan":
			return Tiguan(self.factory_parts)
		return False

class AmericanFactory(AbstractFactory):
	"""Конкретная фабрика, устанавливает фабрику запчастей для создания машин и определяет метод createCar"""
	def __init__(self):
		self.factory_parts = AmericanFactoryParts()

	def createCar(self, type):
		if(type == "Golf"):
			return Golf(self.factory_parts)
		elif(type == "Passat"):
			return Passat(self.factory_parts)
		elif type == "Tiguan":
			return Tiguan(self.factory_parts)
		return False

class RussianFactoryParts(AbstractFactoryParts):
	"""Класс конкретной фабрики запчастей реализует методы engine, paint, wheels"""
	def engine(self):
		print("Установка бензинового двигателя")
	def paint(self):
		print("Покраска в белый цвет")
	def wheels(self):
		print("Установка 16 дюймовых дисков")

class AmericanFactoryParts(AbstractFactoryParts):
	"""Класс конкретной фабрики запчастей реализует методы engine, paint, wheels"""
	def engine(self):
		print("setting dizel engine")
	def paint(self):
		print("paint to white color")
	def wheels(self):
		print("setting 17 inch wheels")

class Golf(AbstractCar):
	"""Класс кокретной машины реализует метод configurate"""
	def configurate(self):
		print("Модель Golf")

		self.factory_parts.engine()
		self.factory_parts.paint()
		self.factory_parts.wheels()

class Passat(AbstractCar):
	"""Класс кокретной машины реализует метод configurate"""
	def configurate(self):
		print("Модель Passat")

		self.factory_parts.engine()
		self.factory_parts.paint()
		self.factory_parts.wheels()

class Tiguan(AbstractCar):
	"""Класс кокретной машины реализует метод configurate"""
	def configurate(self):
		print("Модель Tiguan")

		self.factory_parts.engine()
		self.factory_parts.paint()
		self.factory_parts.wheels()



print("В России")
factory_local = Volkswagen(RussianFactory())

factory_local.getCar("Golf")
print("")
factory_local.getCar("Passat")
print("")
factory_local.getCar("Tiguan")
print("")

print("В Америке")
factory_local = Volkswagen(AmericanFactory())

factory_local.getCar("Golf")
print("")
factory_local.getCar("Passat")
print("")
factory_local.getCar("Tiguan")
print("")