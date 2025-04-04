# 미로탐색(DFS)

# 7*7 격자판의 정보가 주어집니다.

# 첫 번째 줄에 경로의 가지수를 출력한다.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < 7 and 0 <= b < 7 and miro[a][b] == 0:
                miro[a][b] = 1
                dfs(a, b)
                miro[a][b] = 0

if __name__=="__main__":
    miro = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    miro[0][0] = 1
    dfs(0, 0)
    print(cnt)
    
        
    
    

