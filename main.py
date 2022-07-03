import torch
from functions import print_hi
from constants import MainConstants, NamesForIndexesOfExercise


if __name__ == '__main__':
    is_work = True
    constants = MainConstants()
    while is_work:
        print_hi(constants)
        user_choice = input('Введите номер пункта меню: ')
        print(constants.NUMBERS_OF_EXERCISES[user_choice][NamesForIndexesOfExercise.TEXT.value])
        if int(user_choice) == 5:
            is_work = constants.NUMBERS_OF_EXERCISES[user_choice][NamesForIndexesOfExercise.FUNCS.value]()
            continue
        n, m = map(int, input('Введите размерность массива n и m: ').split())
        tensor = torch.randint(-100, 100, (n, m))
        if 0 < int(user_choice) < 4:
            constants.NUMBERS_OF_EXERCISES[user_choice][NamesForIndexesOfExercise.FUNCS.value](tensor, n, m)
        elif int(user_choice) == 4:
            constants.NUMBERS_OF_EXERCISES[user_choice][NamesForIndexesOfExercise.FUNCS.value](tensor, n)
