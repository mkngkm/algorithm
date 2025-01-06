#pop(0)
#큐 시작: head 큐 끝: tail
#head=0부터 시작 k만큼씩 옮기고 pop
#tail n되면 0으로 만들기 : i % n을 index로 하면 됨. 
# => 다 아니고 deque 이용(데크)

from collections import deque

n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq :
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq.popleft())
        


