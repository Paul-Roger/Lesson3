""" (МОДУЛЬ 1)
Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
"""
no_of_elements = 0
user_input = input("Введите количество элементов: ")

if not user_input.isdecimal():
    print("Количество элементов должно быть числом")
    exit()
else:
    if int(user_input) <= 0:
        print("Количество элементов должно быть положительным целым числом")
        exit()

no_of_elements = int(user_input)
user_list = list()

for i in range(no_of_elements):
    user_input = input("Введите элемент списка: ")
    while not user_input.isdecimal():
        user_input = input("Введите целое число в качестве элемента списка: ")
    user_list.append(int(user_input))

user_list.sort()
print("Ваш список: ", user_list)




