class Drink:
    """Главный класс напитка, содержит методы печатания цены и состава"""
    price = 0
    label = 'Drink'
    def printprice(self):
        return self.price
    
    def printconsistent(self):
        return self.label

class Espresso(Drink):
    """Эспрессо"""
    price = 30
    label = 'Эспрессо'
        
class Cappucino(Drink):
    """Каппучино"""
    price = 50
    label = 'Каппучино'
        
class Tea(Drink):
    """Чай"""
    price = 15
    label = 'Чай'

class Decorator(Drink):
    """Главный класс декоратора, переопределяет конструктор и методы принта цены и состава"""
    def __init__(self, subject):
        self.subject = subject
    def printprice(self):
        return self.price + self.subject.printprice()
    def printconsistent(self):
        return self.label + ' + ' + self.subject.printconsistent()
    
class SugarDecorator(Decorator):
    """Конкретный декоратор - сахар"""
    price = 5
    label = 'Сахар'

class MilDecorator(Decorator):
    """Конкретный декоратор - молоко"""
    price = 20
    label = 'Молоко'
        
americanowithsugar = SugarDecorator(MilDecorator(Espresso()))

teawithsugar = SugarDecorator(Tea())

americanowithoutsugar = MilDecorator(Espresso())

print(americanowithsugar.printprice(), ' руб')
print(americanowithsugar.printconsistent())

print(teawithsugar.printprice(), ' руб')
print(teawithsugar.printconsistent())

print(americanowithoutsugar.printprice(), ' руб')
print(americanowithoutsugar.printconsistent())
