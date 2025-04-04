# 사과나무(BFS)


# 첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
# 각 격자안의 사과의 개수는 100을 넘지 않는다.

# 수확한 사과의 총 개수를 출력합니다.


# n = int(input())

# a = [list(map(int, input().split())) for _ in range(n)]
# s = n // 2
# e = n // 2
# res = 0

# for i in range(n):
#     if 0<= s < n and 0<= e < n:
#         for j in range(s, e+1):
#             res += a[i][j]
#         if i >= n // 2:
#             s += 1
#             e -= 1
#         else:
#             s -= 1
#             e += 1
# print(res)
   
   
#### bfs 방법으로 풀기 

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
sum = 0
Q = deque()
ch[n//2][n//2] = 1
sum += a[n//2][n//2]
Q.append((n//2, n//2))
L = 0
while True:
    if L==n//2:
        break
    size = len(Q)
    for i in range(size): # 4방향(상하좌우) 탐방해야할 곳  계속 추가됨
        tmp=Q.popleft()
        for j in range(4): # 상하좌우
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    
        
    L += 1
print(sum)
            
    