# SRP
# class UserManadger:
#     def __init__(self):
#         self.users = user
#
#     def change_yser_name(self, user_name):
#         self.user_name = user_name
#
#     def self_user(self):
#         file = open(self.user_name)
#         file.write(self.user)
#         file.close()

# принцип единственной ответственности (Single Responsibility Principle)
class User:
    def __init__(self, user):
        self.user = user

class UserNameChanger:
    def __init__(self, user):
        self.user = user

    def change_user_name(self, new_name):
        self.user = new_name

class SaveUser:
    def __init__(self, user):
        self.user = user

    def save_user(self):
        file = open(self.user)
        file.write(self.user)
        file.close()

# Создаем пользователя
user = User("Alex")

# Изменяем имя пользователя
user_name_changer = UserNameChanger(user.user)
user_name_changer.change_user_name("Max")
user.user = user_name_changer.user  # Обновляем имя в объекте User

# Сохраняем пользователя в файл
save_user = SaveUser(user.user)

# Откроем файл и сохраним имя пользователя
with open("user.txt", "w") as file:
    file.write(save_user.user)

print("Имя пользователя сохранено:", user.user)
