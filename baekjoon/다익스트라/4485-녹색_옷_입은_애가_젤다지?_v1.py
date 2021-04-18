import sys
from collections import deque

INPUT = sys.stdin.readline
INF = float('inf')
WAY = [[-1, 0], [0, 1], [1, 0], [0, -1]] # up right down left

t = 1
while True:
    n = int(INPUT())
    if not n: break

    map_ = [list(map(int, INPUT().rsplit())) for _ in range(n)]

    q = deque()
    dist = [[INF] * n for _ in range(n)]

    q.append([0, 0])
    dist[0][0] = map_[0][0]

    while q:
        y, x = q.popleft()
        # print(y, x, dist[y][x])
        for wy, wx in WAY:
            ny = y + wy
            nx = x + wx

            if 0 <= ny < n and 0 <= nx < n and dist[ny][nx] > dist[y][x] + map_[ny][nx]:
                dist[ny][nx] = dist[y][x] + map_[ny][nx]
                q.append([ny, nx])
        
    print("Problem {0}: {1}".format(t, dist[n-1][n-1]))
    t += 1

# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 0