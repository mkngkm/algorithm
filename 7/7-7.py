# 송아지 찾기


# 첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000까지이다.

# 점프의 최소횟수를 구한다.


from collections import deque
MAX = 10000
ch = [0] * (MAX +1)
dis = [0] * (MAX + 1)
s, e = map(int, input().split())
ch[s] = 1
dis[s] = 0
dQ = deque()
dQ.append(s)
while dQ:
    cur = dQ.popleft()
    if cur == e:
        break
    for next in (cur-1, cur+1, cur+5):
        if 0<=next<=MAX and ch[next] == 0:
            dQ.append(next)
            ch[next] = 1
            dis[next] = dis[cur] + 1
print(dis[e])