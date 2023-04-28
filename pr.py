def min_spanning_tree(n, matrix):
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i, j, matrix[i][j]))
    edges.sort(key=lambda x: x[2])
    used = [0]
    mst = []
    while len(used) < n:
        for i, j, w in edges:
            if i in used and j not in used:
                used.append(j)
                mst.append((i, j))
                break
            elif j in used and i not in used:
                used.append(i)
                mst.append((i, j))
                break
    mst = [(i+1, j+1) for i, j in mst]
    return mst

n = 4
matrix = [[0, 23, 66, 12],
          [23, 0, 18, 45],
          [66, 18, 0, 34],
          [12, 45, 34, 0]]
result = min_spanning_tree(n, matrix)
for i, j in result:
    print(f"{i} - {j}")
