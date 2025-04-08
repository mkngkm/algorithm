# 토마토 (못품. 다시 풀어야 함)

# ▣ 입력설명
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M, N ≤ 1,000 이다.
# 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

# ▣ 출력설명
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다
from collections import deque
import sys

# 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * m for _ in range(n)] # 강 칸의 토마토가 익을때 까지 걸리는 시간 
dq = deque()

# 익은 토마토의 위치를 모두 큐에 넣음 (토마토 익은거 기준으로 퍼지는 거니까 익은걸 큐에 넣어야 함)
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append((i, j))
                 
# BFS 탐색
while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            dist[nx][ny] = dist[x][y] + 1
            dq.append((nx, ny))

res = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            sys.exit()
        res = max(res, dist[i][j])
print(res)

                
    
    
    

                    
                            
                            
                
                
                
            

