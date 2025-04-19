# 최대 선 연결하기

# ▣ 입력설명
# 첫 줄에 자연수 N(1<=N<=100)이 주어집니다.
# 두 번째 줄에 1부터 N까지의 자연수 N개의 오른쪽 번호 정보가 주어집니다. 순서는 위쪽번호
# 부터 아래쪽번호 순으로입니다.
# ▣ 출력설명
# 첫 줄에 겹치지 않고 그을 수 있는 최대선의 개수를 출력합니다.


n = int(input())
arr = list(map(int, input().split()))
dy = [0] * (n+1)
arr.insert(0, 0)
dy[1] = 1
res = 0
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]
print(res)
            
            
        