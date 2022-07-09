import torch

# Functions.py содержит основные функции, непосредственно отвечающие за выолнение пунктов
# задания практики. Изучение алгоритмов работы с массивами в практике основано на рассмотрении
# тензоров PyTorch как массивов данных. Сведено к минимуму использование встроенных средств Torch
# по обработке тензоров, так как цель практики - научиться самому оперировать алгоритмами работы
# с массивами
from constants import MainConstants

if __name__ == '__main__':
    is_work = True
    constants = MainConstants()  # создаем объект класса, в который собраны основые переменные программы
    while is_work:
        constants.print_hi()
        user_choice = input('Введите номер пункта меню: ')
        if int(user_choice) == 5:
            is_work = constants.NUMBERS_OF_EXERCISES[user_choice][constants.NamesForIndexesOfExercise["FUNCS"]]()
            continue

        try:
            print(constants.NUMBERS_OF_EXERCISES[user_choice][constants.NamesForIndexesOfExercise["TEXT"]])
        except:
            print("Неправильно введено значение")
            continue
        try:
            n, m = map(int, input('Введите размерность массива n и m: ').split())
        except:
            print("Неправильный ввод")
            continue
        else:
            tensor = torch.randint(-100, 100, (n, m))
            if 0 < int(user_choice) < 4:
                constants.NUMBERS_OF_EXERCISES[user_choice][constants.NamesForIndexesOfExercise["FUNCS"]](tensor, n, m)
            elif int(user_choice) == 4:
                constants.NUMBERS_OF_EXERCISES[user_choice][constants.NamesForIndexesOfExercise["FUNCS"]](tensor, n)
