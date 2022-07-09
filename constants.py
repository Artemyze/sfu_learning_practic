import functions


class MainConstants:
    def __init__(self):
        self.AUTHOR = 'Затолокин А.В.'
        self.GROUP = 'ст. гр. ЗКИ21-16Б '
        self.NamesForIndexesOfExercise = {
            'TEXT': 0,
            'FUNCS': 1,
        }
        self.NUMBERS_OF_EXERCISES = {
            '1': ('Заменить минимальный по модулю элемент каждого столбца нулем',
                  functions.change_min_elm),
            '2': ('Вставить после каждой строки, содержащей минимальное значение строку из нулей.',
                  functions.insert_after_row_with_min_elm),
            '3': ('Удалить все столбцы, в которых первый элемент больше последнего',
                  functions.del_cols_where_first_gt_last),
            '4': ('Поменять местами первый и последний столбцы.',
                  functions.swap_first_last_cols),
            '5': ('Выход.', functions.exit_program)
        }
        self.INFO_TEXT = f'''Дан двумерный массив размером n*m, заполненный случайным образом.'''
        self.__full_text = ''

    @property
    def full_text(self):
        if self.__full_text == '':
            self.__full_text = f'{self.GROUP + self.AUTHOR}\n' \
                               f'{self.INFO_TEXT}\n'
            for key, item in self.NUMBERS_OF_EXERCISES.items():
                self.__full_text += f'{key}. {item[self.NamesForIndexesOfExercise["TEXT"]]}\n'
        return self.__full_text

    def print_hi(self):
        print(f'{self.full_text}')
