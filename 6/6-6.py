# dfs - 중복 순열 구하기

def dfs(L):
    global cnt
    if L == M:
        for r in res:
            print(r, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            res[L] = i
            dfs(L+1)

if __name__=="__main__":
    
    N, M = map(int, input().split())
    res = [0] * M
    cnt = 0 
    dfs(0)
    print(cnt)