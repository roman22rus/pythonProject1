# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import requests
first_name = input("Введите ваше имя:")
last_name = input("Введите вашу фамилию:")
age = input("Введите ваш возраст:")
city = input("Введите город проживания:")

# Выводим пустую строку
print("")

# Выводим приветствие, подставляя имя и фамилию пользователя,
# которые он ввел с клавиатуры
print("Привет,", first_name, last_name, "!")

# Выводим пустую строку
print("")

# Выводим фиксированный текст для удобства просмотра
print("Ваш профиль:")

# Выводим возраст и город, которые указал пользователь
print("Возраст:", age)
print("Город:", city)
