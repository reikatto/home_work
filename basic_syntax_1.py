a, b = map(int, input().split())

x = []

for i in range(a, b + 1):
    if i % 3 == 0:
        x.append(i)

print(sum(x)/len(x))
