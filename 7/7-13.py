#섬나라 아일랜드 (BFS 활용)

# 섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 각 섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 있으며, 
# 0은 바다입니다. 섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.


# 첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다.
# 두 번째 줄부터 격자판 정보가 주어진다.

# 첫 번째 줄에 섬의 개수를 출력한다.

from collections import deque

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, 1, -1, -1, 1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dq = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            dq.append((i, j))
            while dq:
                tmp = dq.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y] == 1:
                        board[x][y] = 0
                        dq.append((x, y))
            cnt += 1
            
print(cnt)
                
