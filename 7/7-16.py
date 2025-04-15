# 사다리 타기(DFS)

# ▣ 입력설명
# 10*10의 사다리 지도가 주어집니다.
# ▣ 출력설명
# 출발지 열 번호를 출력하세요.

# 사다리는 좌우 만나면 좌우 먼저 가야함!!! 미친 !!
# 거꾸로 가는 것도 하나의 방법 !!!!!!!!!!



# ## 위로 못감
# dx = [0, 0, 1] # 왼 오른 아래 그래서 이 순서ㅇ여야 한다
# dy = [-1, 1, 0]

# def dfs(i, j):
#     global res
#     if i == 9: 
#         if board[i][j] == 2:
#             res = 1
#             return
#     else:
#         valid = 0
#         for k in range(2):
#             x = i + dx[k]
#             y = j + dy[k]
#             if 0<=x<10 and 0<=y<10 and board[x][y] != 0 and ch[x][y] == 0:
#                 valid = 1
#                 ch[x][y] = 1 # 재방문 방지
#                 dfs(x, y)
#                 if res == 1: return 
#         if valid == 0:
#         # 좌우 둘 다 못 갔으면 아래로
#             x = i + dx[2]
#             y = j + dy[2]
#             if 0 <= x < 10 and 0 <= y < 10 and board[x][y] != 0 and ch[x][y] == 0:
#                 ch[x][y] = 1 
#                 dfs(x, y)
                
            
    


# if __name__=="__main__":
#     board = [list(map(int, input().split())) for _ in range(10)]
   
#     res = 0 
#     for k in range(10):
#         ch = [[0] * 10 for _ in range(10)]
#         if board[0][k] == 1:
#             dfs(0, k)
#             if res == 1:
#                 print(k)
#                 break
#         else: 
#             continue

def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y-1>-0 and board[x][y-1] ==1 and ch[x][y-1] == 0: #왼
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1] and ch[x][y+1]==0: # 오른
            DFS(x, y+1)
        else: # 위
            DFS(x-1, y)

if __name__=="__main__":
    board=[list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)
        
            