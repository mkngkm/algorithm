# dfs - 중복 순열 구하기

def dfs(L, i):

    if L == M:
        print (i)
        return
    else:
        print(i, end=" ")
        for j in range(1, N+1):
            for k in range(M):
                dfs(L+1, j)


N, M = map(int, input().split())

dfs(1, 1)