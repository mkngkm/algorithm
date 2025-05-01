# 위상정렬(그래프 정렬)

# ▣ 입력설명
# 첫 번째 줄에 전체 일의 개수 N과 일의 순서 정보의 개수 M이 주어집니다.
# 두 번째 줄부터 M개의 정보가 주어집니다.
# ▣ 출력설명
# 전체 일의 순서를 출력합니다.

# 4번 앞, 4번으로 들어오는 것-> 진입차수 
# 진입차수가 0인거 큐에 넣어서 하나씩 popleft
# popleft 할때마다 해당 노드 뒤에 해야하는 것들 진입 차수 -1

from collections import deque

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]  = 1
    degree[b] += 1
    
dq = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        dq.append(i)

while dq:
    a = dq.popleft()
    print(a, end=' ')
    for i in range(1, n+1):
        if graph[a][i] > 0:
            degree[i] -= 1
            if degree[i] == 0:
                dq.append(i)
            
    
