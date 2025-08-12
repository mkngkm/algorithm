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
    
        
