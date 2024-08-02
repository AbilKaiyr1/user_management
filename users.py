class UserManager:
    def __init__(self):
        self.users = {} # Используем словарь (dict) для хранения пользователей с их id
        self.id = 1 #  счетчик(counter) для подсчета id-шников пользователей

    def addUser(self, name):
        user_id = self.id # id пользователя равен текущему значению счетчика. Первый добавленный пользователь будет с первым id
        self.users[user_id] = name # Добавляем пользователя в словарь с его id и именем
        self.id += 1 # Инкрементируем значение счетчика для следующего пользователя
        return user_id # Возвращаем id добавленного пользователя

    def getUser(self, user_id):
        if user_id in self.users: # Проверяем, существует ли данный id в словаре
            return self.users[user_id] # Возвращаем имя пользователя с данным id
        return None # Возвращаем None, если id не найден в словаре

    def deleteUser(self, user_id):
        if user_id in self.users: # Проверяем, существует ли данный id в словаре
            del self.users[user_id] # Удаляем пользователя с данным id из словаря
            return True # Возвращаем True, если удаление успешно
        return False # Возвращаем False, если id не найден в словаре

    def findUserByName(self, name):
        found_users = [] # Список для хранения найденных id пользователей
        for user_id, user_name in self.users.items(): # Проходимся по словарю items(ключ, значение)
            if user_name == name: # Если имя пользователя совпадает с искомым именем
                found_users.append(user_id) # Добавляем id пользователя в список
        return found_users # Возвращаем список найденных id

# Пример использования
userManager = UserManager()

id1 = userManager.addUser("Jarasar")
id2 = userManager.addUser("Adil")
id3 = userManager.addUser("Jarasar")
print(userManager.users) 
print(userManager.getUser(id1))  # Вернет "Jarasar"
print(userManager.getUser(id2))  # Вернет "Adil"
print(userManager.getUser(999))  # Вернет None

print(userManager.findUserByName("Jarasar"))  # Вернет [1, 3]
print(userManager.findUserByName("Baha"))  # Вернет []

print(userManager.deleteUser(id2))  # Вернет True
print(userManager.deleteUser(999))  # Вернет False
print(userManager.users) 
print(userManager.getUser(id2))  # Вернет None