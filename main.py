user_list = []

class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id  # Это инкапсуляция: данные спрятаны
        self.__name = name
        self.__access_level = 'user'  # У всех обычных сотрудников уровень доступа 'user'

    # Геттеры: получаем данные
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттер: изменить имя
    def set_name(self, name):
        self.__name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.set_access_level('admin')  # Администратор имеет уровень доступа 'admin'

    # Метод для изменения уровня доступа
    def set_access_level(self, level):
        self._User__access_level = level  # Изменение защищенного атрибута через метод

    # Метод для добавления нового пользователя
    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f'Пользователь {user.get_name()} добавлен.')

    # Метод для удаления пользователя
    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f'Пользователь {user.get_name()} удалён.')

# Создаём пользователей
user1 = User(1, "Иван")
user2 = User(2, "Анна")
user3 = User(3, "Олег")
user4 = User(4, "Екатерина")

admin = Admin(2, "Ольга") # Создаём администратора

# Добавляем пользователя
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
admin.add_user(user_list, user3)  # Попытка добавить уже существующего пользователя

# Выводим имена всех пользователей
print("\nПользователи в системе:")
for user in user_list:
    print(user.get_name())

# Удаляем пользователя и проверяем
admin.remove_user(user_list, user1)
admin.remove_user(user_list, user1)  # Попытка удалить уже удалённого пользователя

print("\nПользователи после удаления:")
for user in user_list:
    print(user.get_name())