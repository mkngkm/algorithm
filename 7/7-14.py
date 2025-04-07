# 안전 영역

# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. 
# N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N 개의 각 줄에는 2차원 배열의 첫번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
# 각 줄에는 각 행의 첫번째 열부터 N번째 열까지 N 개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 
# 높이는 1이상 100 이하의 정수이다.

# 첫째 줄에 장마철에 물에 잠기지 않는 안전한영역의 최대 개수를 출력한다.

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = list()
max_rain = 100
min_rain = 1
for _ in range(n):
    tmp = list(map(int, input().split()))
    max_rain = max(max(tmp), max_rain)
    min_rain = min(min(tmp), min_rain)
    board.append(tmp)     
limit = min_rain
dq = deque()
cnt = 0
res = 0


while limit <= max_rain:
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > limit and ch[i][j] == 0:
                dq.append((i, j))
                while dq:
                    tmp = dq.popleft()
                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]
                        if 0<=x<n and 0<=y<n and board[x][y] > limit and ch[x][y] == 0:
                            ch[x][y] = 1
                            dq.append((x, y))
                cnt += 1
    limit += 1
    res = max(cnt, res)
print(res)
    
            
                        
### DFS
# def dfs(i, j, h):
#     ch[x][y] = 1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0<=x<n and 0<=y<n and ch[xx][yy]==0 and board[xx][yy]>h:
#             dfs(xx, yy, h)
    

# if __name__ == "__main":
#     n = int(input())
#     cnt = 0
#     res = 0
#     board = [list(map(int, input().split())) for _ in range(n)]
#     for h in range(100):
#         ch = [[0] * n for _ in range(n)]
#         cnt = 0
#         for i in range(n):
#             for j in range(n):
#                 if ch[i][j] == 0 and board[i][j] > h:
#                     cnt += 1
#                     dfs(i, j, h) 
#         res = max(res, cnt)
#         if cnt == 0: # 안전 영역이 0개면 최대 높이를 넘었단 뜻이니까
#             break 

            
        
