# 단지 번호 붙이기(DFS, BFS)


# 첫 번째줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력
# 되고 그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다

# 첫 번째줄에는 총 단지수를 출력하시오. 그리고 각 단지내의 집의 수를 오름차순으로 정렬하
# 여 한줄에 하나씩 출력하시오

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# n = int(input())
# apart = [list(map(int, list(input()))) for _ in range(n)]

### bfs
# dq = deque()
# dq.append((0,0))
# res = list()
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if apart[i][j] == 1:
#             apart[i][j] = 0
#             dq.append((i, j))
#             cnt = 1
#             while dq:
#                 tmp = dq.popleft()
#                 for k in range(4):
#                     x = tmp[0] + dx[k]
#                     y = tmp[1] + dy[k]
#                     if x<0 or x>=n or y<0 or y>=n or apart[x][y]==0:
#                         continue
#                     apart[x][y] = 0
#                     dq.append((x,y))
#                     cnt+= 1
#             res.append(cnt)
                    
            
### dfs
def dfs(x, y):
    global cnt
    cnt += 1
    apart[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and apart[xx][yy] == 1:
            dfs(xx, yy)
                       
            
if __name__=="__main__":
    n = int(input())
    res = list()
    apart = [list(map(int, list(input()))) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if apart[i][j] == 1:
                cnt = 0
                dfs(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)
    
        
