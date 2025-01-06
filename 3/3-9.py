#이차원 배열받기

#상 우 하 좌
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n) #맨 윗행 추가
a.append([0] * n) #맨 아래행 추가

for x in a:
    x.insert(0,0) #insert(index, value) 각 행 첫번째에 0 추가
    x.append(0) #각 행 마지막에 0 추가

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)




            
            


