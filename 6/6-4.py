# dfs - 합이 같은 부분집합

import sys
#sys.stdin = open("input.txt", "r")

def dfs(L, sum):

    # 가지치기
    if sum > total // 2:
        return 
    # 인덱스 번호가 n이상이면 stop
    if L == n:            
        if sum == total - sum:
            print("YES")
            sys.exit(0)
    else:
        dfs(L+1, sum + s[L])
        dfs(L+1, sum )


n = int(input())
s = list(map(int, input().split()))
ch = [0] * n
total = sum(s)
dfs(0, 0)
print("NO")
