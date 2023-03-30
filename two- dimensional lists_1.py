a, b = map(int, input().split())

matrix_1 = [list(input()) for _ in range(b)]
matrix_2 = [list(input()) for _ in range(b)]

s1, s2, s3, s4 = input()
s = {'00': s1, '01': s2, '10': s3, '11': s4}

for i in range(b):
    line = ''
    for j in range(a):
        line += s[matrix_1[i][j] + matrix_2[i][j]]
    print(line)
