# 등산경로(DFS)

# 어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은
# 구역으로만 이동할 수 있도록 등산로를 설계하려고 합니다. 등산로의 출발지는 전체 영역에서
# 가장 낮은 곳이고, 목적지는 가장 높은 곳입니다. 출발지와 목적지는 유일합니다.


# 첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 등산경로의 가지수를 출력한다.
def dfs(x, y):
    global cnt
    if x == ei and y == ee:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n: 
                if jido[xx][yy] > jido[x][y] and ch[xx][yy] == 0:
                    ch[xx][yy] = 1
                    dfs(xx, yy)
                    ch[xx][yy] = 0
                
        

if __name__=="__main__":
    s = 2147000000
    e = -2147000000
    n = int(input())
    jido = list()
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        jido.append(tmp)
        if max(tmp) > e:
            e = max(tmp)
            ee = tmp.index(e)
            ei = i 
        if min(tmp) < s:
            s = min(tmp)
            se = tmp.index(s)
            si = i
    cnt = 0
    ch[si][se] = 1
    dfs(si, se)
    print(cnt)
            
    