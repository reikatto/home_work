n = int(input())
gods = {}
for i in range(n):
    god_name = input()
    gods[god_name] = 0

m = int(input())
for i in range(m):
    suspect = input()
    for god_name in gods:
        diff_count = sum(a != b for a, b in zip(suspect, god_name))
        if diff_count == 1:
            gods[god_name] += 1

for god_name in gods:
    print(gods[god_name])
