n = int(input())
votes = {}

for i in range(n):
    name, count = input().split()
    count = int(count)
    if name in votes:
        votes[name] += count
    else:
        votes[name] = count

sorted_votes = sorted(votes.items())

for name, count in sorted_votes:
    print(name, count)

input()