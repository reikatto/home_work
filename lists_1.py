a, b = input().split()

bulls = 0
for i in range(4):
    if a[i] == b[i]:
        bulls += 1

cows = 0
for i in range(4):
    if a[i] in b[:i] + b[i + 1:]:
        cows += 1

print(bulls, cows)
