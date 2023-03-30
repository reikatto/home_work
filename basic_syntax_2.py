c = int(input())

a, b = 0, 1
n = 1

while c > b:
    n += 1
    a, b = b, a + b

if c == b:
    print(n)
else:
    print(-1)