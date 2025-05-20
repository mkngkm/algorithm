#수행 시간(위상정렬)

# 입력
# 첫 번째 줄에는 컴퓨터의 개수 n이 주어진다. (3 ≤ n ≤ 100) 두 번째 줄부터 n개의 줄에 걸쳐 1번부터 n번까지 각 컴퓨터의 계급 c과 동작 속도 t가 공백을 두고 주어진다. (1 ≤ t ≤ 100)

# 출력
# 이 시스템에 대한 정보가 주어졌을 때 임무 수행이 끝날 때까지 걸린 시간을 구하여라.

from collections import deque

if __name__=="__main__":
    n = int(input())
    cls = [0] * (n+1)
    time = [0] * (n+1)
    for i in range(1, n+1):
        c, t = map(int, input().split())
        cls[i] = c
        time[i] = t
    res = 0     
    dq = deque()
    

    max_cls = max(cls) #가장 큰 클래스 값
    dp = [0] * (n+1)
    x = 1
    while x < max_cls:
        next = []
        for i in range(1, n+1):
            if cls[i] == x:
                dq.append(i)
                if cls[i] == 1:
                    dp[i] = time[i]
            if cls[i] == x+1:
                next.append(i)
        max_time = 0
        while dq:
            a = dq.popleft()
            for b in next:
                dp[b] = max(dp[b], time[b] + dp[a] + (a-b) ** 2)
                max_time = max(time[a] + (a-b) ** 2, max_time) # 동작 시간 + 전송 시간 중에 가장 큰 것
        x += 1
    print(max(dp))  
    
    
    
### 숏 코딩 예시
n = int(input())
comp = sorted(tuple(map(int,input().split()))+(i,) for i in range(n)) # 각 원소는 (계급, 동작시간, 인덱스) + 계급순으로 정렬됨. 계급이 동률이라면 인덱스. 
dp = [comp[i][1] for i in range(n)] # 동작시간으로 초기화
for i in range(n):
    for j in range(i):
        if comp[i][0] != comp[j][0]+1: continue # 계급이 하나 더 클때만
        dp[i] = max(dp[i], dp[j]+(comp[i][2]-comp[j][2])**2+comp[i][1]) # 업데이트
print(max(dp))

### 예시 2
import sys 
input=sys.stdin.readline
n=int(input())
rank=[[] for _ in range(n+1)]
time=[0]*(n+1)
total_time=[0]*(n+1)
for i in range(1,n+1):
    r,t=map(int,input().split())
    rank[r].append(i) # 각 랭크별로 리스트 관리(여기가 포인트!)
    time[i]=t
for i in rank[1]: # 1레벨인거는 동작시간만 추가
    total_time[i]=time[i]

for i in range(1,n):
    for x in rank[i]: # 현재 랭크
        for y in rank[i+1]: #다음랭크 업데이트
            total_time[y]=max(total_time[y],total_time[x]+(x-y)**2+time[y]) 
print(max(total_time))
    
    
        
        
            
    
    
        
            
        
        
            
    
    
    
    

