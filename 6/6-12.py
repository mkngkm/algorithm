# 인접행렬

# 첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결 정보와 거리비용이 주어진다.

# 인접행렬을 출력하세요.

n, m = map(int, input().split())

mat = [[0] * n for _ in range(n)]

for _ in range(m):
    i, j, v = map(int, input().split())
    mat[i-1][j-1] = v
    
for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()


