# 미로의 최단거리 통로(BFS 활용)

# 7*7 격자판의 정보가 주어집니다.

# 첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.

from collections import deque

miro = [list(map(int, input().split())) for _ in range(7)]
dist = [[0] * 7 for _ in range(7)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ch = [[0] * 7 for _ in range(7)] # 이거 궅이 안쓰고 miro 자체를 1로 만들어버리는 것이 더 좋음
dq = deque()
x = 0 
y = 0
res = 21470000
dq.append((x, y))
ch[x][y] = 1

while dq:
    x, y = dq.popleft()
    if x == 6 and y == 6:
        print(dist[x][y])
    for i in range(4):
        nextX = x+dx[i]
        nextY = y+dy[i]
        if 0<=nextX<7 and 0<=nextY <7 and miro[nextX][nextY] == 0 and ch[nextX][nextY]==0:
            ch[nextX][nextY ]=1
            dist[nextX][nextY]+= dist[x][y] + 1
            dq.append((nextX, nextY))    
if dist[6][6] == 0:
    print(-1)
            
            
        
        
