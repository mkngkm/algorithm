#아예 못품(다시 해보기)
def Count(len):
    cnt = 1
    ep = Line[0] #endPoint-마지막으로 말을 배치한 위치
    for i in range(1, n):
        if Line[i] - ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt
n, c = map(int, input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt = 1
rt = Line[n-1]
while lt <= rt:
    mid = (lt + rt)//2
    if Count(mid) >= c: #제일 가까운 간격을 최소해서 말을 배치했을때 가능한 말의 수가 c(배치해야하는 말의수) 보다 클떄
        res = mid
        lt = mid + 1 #더 큰 값을 찾아서
    else:
        rt = mid - 1 #더 작은 값을 찾아서

print(res)