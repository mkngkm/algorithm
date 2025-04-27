# 알리바바와 40인의 도둑(Top-Down)

def dfs(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if x == 0 or y == 0:
            if x == 0:
                dy[x][y] = dfs(x, y-1) + arr[x][y]# 왼쪽, 위 각각 더해서
            else:
                dy[x][y] = dfs(x-1, y) + arr[x][y]# 왼쪽, 위 각각 더해서
        else:
            dy[x][y] = min(dfs(x, y-1), dfs(x-1, y)) + arr[x][y]
        return dy[x][y]
        
            
            

if __name__=="__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    for i in range(n): # 양 사이드 채우기
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]   
    dfs(n-1, n-1)
    print(dy[n-1][n-1])

    