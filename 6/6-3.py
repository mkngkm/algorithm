# dfs - 부분집합 구하기

def dfs (v):
    if v == N+1:
        for i in range(1, N+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        #원소 있음
        ch[v] = 1
        dfs(v+1)
        #원소 없음
        ch[v] = 0
        dfs(v+1)

        


N = int(input())
ch = [0] * (N+1)
dfs(1)
    
