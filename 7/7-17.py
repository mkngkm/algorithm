# 피자 배달 거리

# ▣ 입력설명
# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 12)이 주어진다.
# 둘째 줄부터 도시 정보가 입력된다.
# ▣ 출력설명
# 첫째 줄에 M개의 피자집이 선택되었을 때 도시의 최소 피자배달거리를 출력한다.


#### 조합 다 구하고 거리 구하는게 조음!!!!!!!

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)
    
    
if __name__=="__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    DFS(0,0)
    print(res)