import torch


def print_hi(constant):
    print(f'{constant.full_text}')


def change_min_elm(tensor, n, m):
    print(f'Исходный тензор: \n{tensor}')
    tensor_tmp = torch.abs(tensor)
    i = j = 0
    for j in range(m):
        indexes_minimum_from_col = [i, j]
        for i in range(n):
            if tensor_tmp[i][j] < tensor_tmp[indexes_minimum_from_col[0]][indexes_minimum_from_col[1]]:
                indexes_minimum_from_col = [i, j]
        tensor_tmp[indexes_minimum_from_col[0]][indexes_minimum_from_col[1]] = 0
    print(f'Измененный тензор: \n{tensor_tmp}')
    return tensor_tmp


def insert_after_row_with_min_elm(tensor, n, m):
    print(f'Исходный тензор: \n{tensor}')
    i = j = 0
    indexes_minimum_from_col = [i, j]
    for i in range(n):
        for j in range(m):
            if tensor[i][j] < tensor[indexes_minimum_from_col[0]][indexes_minimum_from_col[1]]:
                indexes_minimum_from_col = [i, j]
    g_tensor_min = tensor[indexes_minimum_from_col[0]][indexes_minimum_from_col[1]]
    row_has_min = False
    i = j = 0
    temp = torch.tensor([], dtype=torch.uint8)
    zero_row = torch.zeros(m, dtype=torch.uint8)
    for i in range(n):
        temp = torch.cat((temp, tensor[i, :]))
        for j in range(m):
            if tensor[i, j] == g_tensor_min:
                row_has_min = True
        if row_has_min:
            temp = torch.cat((temp, zero_row))
            row_has_min = False
    temp = torch.reshape(temp, (temp.size(dim=0) // m, m))
    print(f'Измененный тензор: \n{temp}')
    return temp


def del_cols_where_first_gt_last(tensor, n, m):
    i = j = 0
    print(f'Исходный тензор: \n{tensor}')
    temp = torch.tensor([], dtype=torch.uint8)
    d_first_last_pos = {
        'first': 0,
        'last': -1,
    }
    for j in range(m):
        if tensor[d_first_last_pos['first']][j] < tensor[d_first_last_pos['last']][j]:
            temp = torch.cat((temp, tensor[:, j]), dim=0)
    temp = torch.reshape(temp, (n, temp.size(dim=0) // n))
    print(f'Измененный тензор: \n{temp}')
    return temp


def swap_first_last_cols(tensor, n):
    print(f'Исходный тензор: \n{tensor}')
    d_first_last_pos = {
        'first': 0,
        'last': -1,
    }
    for i in range(n):
        temp = tensor[i][d_first_last_pos['first']].clone().detach()
        tensor[i][d_first_last_pos['first']] = tensor[i][d_first_last_pos['last']]
        tensor[i][d_first_last_pos['last']] = temp
    print(f'Измененный тензор: \n{tensor}')
    return tensor


def exit_program():
    return False
