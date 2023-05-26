from math import fabs, inf

def Dijkstra(N, s, matrix):
    valid = [True] * N
    weight = [inf] * N
    weight[s] = 0
    for i in range(N):
        min_weight = 1000001
        vertex_mw = -1
        for j in range(N):
            if valid[j] and weight[j] < min_weight:
                min_weight = weight[j]
                vertex_mw = j
        for k in range(N):
            if weight[vertex_mw] + matrix[vertex_mw][k] < weight[k]:
                weight[k] = weight[vertex_mw] + matrix[vertex_mw][k]
        valid[vertex_mw] = False
    return weight


n, m = map(int, input().split())
polygon = [[int(j) for j in input().split()] for i in range(n)]
start = tuple(map(int, input().split()))
load = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

N = n * m
matrix = [[inf for j in range(N)] for i in range(N)]
vertex = 0
for i in range(n):
    for j in range(m):
        if i > 0:
            if fabs(polygon[i][j] - polygon[i - 1][j]) < 101:
                matrix[vertex][(i-1)*m + j] = 1
        if i < n - 1:
            if fabs(polygon[i][j] - polygon[i + 1][j]) < 101:
                matrix[vertex][(i+1)*m + j] = 1
        if j > 0:
            if fabs(polygon[i][j] - polygon[i][j - 1]) < 101:
                matrix[vertex][i*m + j - 1] = 1
        if j < m - 1:
            if fabs(polygon[i][j] - polygon[i][j + 1]) < 101:
                matrix[vertex][i*m + j + 1] = 1
        vertex += 1

start = start[0] * m + start[1]
load = load[0] * m + load[1]
end = end[0] * m + end[1]

way = Dijkstra(N, start, matrix)[load]
way += Dijkstra(N, load, matrix)[end]
print(way)