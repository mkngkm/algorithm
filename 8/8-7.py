# 가장 높은 탑 쌓기

# ▣ 입력설명
# 입력 파일의 첫째 줄에는 입력될 벽돌의 수가 주어진다. 입력으로 주어지는 벽돌의 수는 최대
# 100개이다. 둘째 줄부터는 각 줄에 한 개의 벽돌에 관한 정보인 벽돌 밑면의 넓이, 벽돌의 높
# 이 그리고 무게가 차례대로 양의 정수로 주어진다. 각 벽돌은 입력되는 순서대로 1부터연속적
# 인 번호를 가진다.
# ▣ 출력설명
# 첫 번째 줄에 가장 높이 쌓을 수 있는 탑의 높이를 출력한다.

# 밑면, 높이, 무게

# 밑면: 점점 작아져야/ 높이: 상관 없음 / 무게: 점점 가벼워져야

n = int(input())
a = list()
for i in range(1, n+1):
    b, h, w = map(int, input().split())
    a.append((b, h, w))
# 2번째 값 기준 정렬
sorted_a = sorted(a, key=lambda x: x[0], reverse=True)
sorted_a.insert(0, (0, 0, 0))
dy = [0] * (n+1) # 정렬된거 기준
dy[1] = sorted_a[1][1] #높이값
res = 0
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if sorted_a[j][2] > sorted_a[i][2] and dy[j] > max: # 무게가 가벼워지고, 그중에서 높이가 가장 높은것
            max = dy[j]
    dy[i] = max + sorted_a[i][1]
    if dy[i] > res:
        res = dy[i]
print(res)

