# Принцип разделения интерфейсов (ISP, Interface Segregation Principle)
# class CmartHouse:
#     def turn_on_lights(self):
#         print('Включаем освещение')
#
#
#     def turn_on_tv(self):
#         print('Включаем телевизор')
#
#
#     def turn_on_ac(self):
#         print('Включаем кондиционер')

class Lights:
    def turn_on_lights(self):
        print('Включаем освещение')
class TV:
    def turn_on_tv(self):
        print('Включаем телевизор')
class AC:
    def turn_on_ac(self):
        print('Включаем кондиционер')
