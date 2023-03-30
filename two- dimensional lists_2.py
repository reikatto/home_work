n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n**2)]

red_flag = [i for i in range(1, n**2 + 1)]
flag = False

row_counter = 0
column_counter = -n

for i in range(n**2):
    middle = []
    column = []
    row = []

    # заполнение списков для проверки строк и столбцов
    for j in range(n**2):
        row.append(matrix[i][j])
        column.append(matrix[j][i])

    # заполнение маленьких матриц
    column_counter += n
    for j in range(column_counter, column_counter + n):
        line = []
        for k in range(row_counter, row_counter + n):
            line.append(matrix[j][k])
        middle.extend(line)

    if column_counter == n**2 - n:
        column_counter = -n
        row_counter += n

    if sorted(row) != red_flag or sorted(column) != red_flag or sorted(middle) != red_flag:
        flag = True
        break

if flag:
    print('Incorrect')
else:
    print('Correct')
