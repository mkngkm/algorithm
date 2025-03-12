# dfs - 바둑이 승차

import sys

def dfs(L, sum):
    global biggest
    if sum > w or a[L] > w: 
        return
    
    if L == n:
        biggest = max(sum, biggest)
        return
    else:
        dfs(L+1, sum + a[L])
        dfs(L+1, sum)


w, n = map(int, input().split())
a = list()
biggest = 0
for _ in range(n):
    a.append(int(input()))
a.sort()
dfs(0, 0)
print(biggest)



