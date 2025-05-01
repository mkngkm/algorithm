# 플로이드 워샬 알고리즘

# ▣ 입력설명
# 첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고, M줄에 걸쳐 도로정보
# 와 비용(20 이하의 자연수)이 주어진다. 만약 1번 도시와 2번도시가 연결되고 그 비용이 13이
# 면 “1 2 13”으로 주어진다.
# ▣ 출력설명
# 모든 도시에서 모든 도시로 이동하는데 드는 최소 비용을 아래와 같이 출력한다.
# 자기자신으로 가는 비용은 0입니다. i번 정점에서 j번 정점으로 갈 수 없을 때는 비용을 “M"으
# 로 출력합니다.


if __name__=="__main__":
    n, m = map(int, input().split())
    dis = [[5000] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1): # 같은 정점 0으로 초기화
        dis[i][i] = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c
    ## 플로이드 와샬 알고리즘(O(n^3))
    for k in range(1, n+1): # 중간 노드 기준으로 업데이트
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    # 그냥 출력            
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ') 
        print()          