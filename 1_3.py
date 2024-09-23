# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)
# class Rird:
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print(f'{self.name} is flying')
#
# class Pingu(Rird):
#     pass
# p = Pingu('Сара')
# p.fly()

class Bird:
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(f'{self.name} is flying')
class Pingu(Bird):
    def fly(self):
        print(f'{self.name} is not flying')

p = Pingu('Сара')
p.fly()


