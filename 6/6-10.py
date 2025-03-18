# 조합

#N: 자연수 , M: 뽑는 개수
import sys

def dfs(L, now):
    global cnt
    if L == m:
        for r in res:
            print(r, end=" ")
        print()
        cnt += 1
    else:
        for i in range(now, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L+1, i)
                ch[i] = 0
            
                
            


if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n+1)
    cnt =  0
    dfs(0, 1)
    print(cnt)