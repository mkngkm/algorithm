# 14938
# 서강 그라운드

# 주어진 필드가 위의 그림과 같고, 예은이의 수색범위가 4라고 하자. 
# ( 원 밖의 숫자는 지역 번호, 안의 숫자는 아이템 수, 선 위의 숫자는 거리를 의미한다) 
# 예은이가 2번 지역에 떨어지게 되면 1번,2번(자기 지역), 3번, 5번 지역에 도달할 수 있다. 
# (4번 지역의 경우 가는 거리가 3 + 5 = 8 > 4(수색범위) 이므로 4번 지역의 아이템을 얻을 수 없다.) 
# 이렇게 되면 예은이는 23개의 아이템을 얻을 수 있고, 이는 위의 필드에서 예은이가 얻을 수 있는 아이템의 최대 개수이다.

# 입력
# 첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.

# 둘째 줄에는 n개의 숫자가 차례대로 각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.

# 세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.

# 지역의 번호는 1이상 n이하의 정수이다. 두 지역의 번호가 같은 경우는 없다.

# 출력
# 예은이가 얻을 수 있는 최대 아이템 개수를 출력한다.

n, m, r = map(int, input().split())

# 지역별로(index) item 개수
items = list(map(int, input().split()))
items.insert(0, 0) 

INF = int(1e9)
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    dist[i][i] = 0

for _ in range(r):
    # a-b 가는 길이 (양방향)
    a, b, c = map(int, input().split())
    # 지역, 길이
    dist[a][b] = min(dist[a][b], c)
    dist[b][a] = min(dist[b][a], c)

    
for k in range(1, n+1):
    for i in range(1, n+1):
        if dist[i][k] == INF:
            continue
        for j in range(1, n+1):
            if dist[k][j] == INF:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]   

res = 0
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        if dist[i][j] <= m:
            sum += items[j]
    res = max(sum, res)
print(res)
    

    
    

