#교육과정 설계
# 첫 줄에 한 줄에 필수과목의 순서가 주어집니다. 모든 과목은 영문 대문자입니다.
# 두 번째 줄에 N(1<=N<=10)이 주어집니다.
# 세 번 째 줄부터 현수가 짠 N개의 수업설계가 주어집니다.(수업설계의 길이는 30이하이다)
# 수업설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.

# 수업설계가 잘된 것이면 “YES", 잘못된 것이면 ”NO“를 출력합니다.


from collections import deque

# 필수 과목 순서
basic = input()
n = int(input())
#res = ["YES"] * n

for i in range(n):
    dq = deque(basic)
    ex = input()
    for e in ex:
        if e in dq:
            if e != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else: # 전부 다 돌고 break 문에 안걸렸을때
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
        
            
                
            
            
            