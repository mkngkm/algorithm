#이차원 배열받기
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
#회전수 받기
m = int(input())

for i in range(m):
    r, d, k = map(int, input().split())
    newA = [0 for i in range(n)]
    for j in range(n):
        if d :
            newA[(j+k)%n] = a[r-1][j] #%로 구현해야함. n 초과 회전수때문 //오른쪽
        else:
            newA[(j-k) % n] = a[r-1][j] #왼쪽
    a[r-1] = newA


res = 0
s= 0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i <n//2:
        s +=1
        e-=1
    else:
        s-=1
        e+=1
print(res)