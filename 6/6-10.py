# 조합

#N: 자연수 , M: 뽑는 개수
import sys
import itertools as it
def dfs(L, s):
    global cnt
    if L == m:
        for r in res:
            print(r, end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n+1):
            res[L] = i
            dfs(L+1, i+1)
            
                
            


if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0] * (m+1)
    #ch = [0] * (n+1) # 필요 없음 
    cnt =  0
    
    # 조합
    #for tmp in it.combinations(n, m)
    
    dfs(0, 1)
    print(cnt)