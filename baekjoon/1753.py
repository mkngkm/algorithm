# 1753 최단경로
# 다익스트라 알고리즘

# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. 
# (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

# 정점의 개수, 간선의 개수
n, e = map(int, input().split())
k = int(input())
INF = int(1e9)

# 1번 노드부터 시작하므로 하나 더 추가
graph = [[] for _ in range(n+1)] 
dist = [INF] * (n+1)

for _ in range(e):
    # u에서 v로 가는 가중치 w인 간선
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):     
    q = []
    # 힙이 거릴로 정렬되게끔 거리, 노드 로 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        distance, node = heapq.heappop(q)
        
        # 이미 입력되어있는 값이 현재 노드의 값보다 작다면
        if dist[node] < distance:
            continue
        
        for i in graph[node]:
            # 현재노드부터 다음노드가, 기존의 값보다 작다면 업데이트
            if distance + i[1] < dist[i[0]]:
                dist[i[0]] = distance + i[1]
                heapq.heappush(q, (distance + i[1], i[0]))
                
dijkstra(k)
for d in dist[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)
    
