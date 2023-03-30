a = input()

counter = 0
for i in range(len(a)):
    if '>>-->' == a[i:i + 5] or '<--<<' == a[i:i + 5]:
        counter += 1

print(counter)
