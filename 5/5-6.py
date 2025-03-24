
#응급실

# 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
# 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시 넣습니다. 그렇지 않으면 진료를 받습니다.
# 현재 N명의 환자가 대기목록에 있습니다.
# N명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M번째 환자는 몇 번째로 진료를 받는지 출력하는 프로그램을 작성하세요.
# 대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것입니다.

# 첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N) 주어집니다.
# 두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.
# 위험도는 값이 높을 수록 더 위험하다는 뜻입니다. 같은 값의 위험도가 존재할 수 있습니다.


from collections import deque

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))] # 인덱스, 위험도
dq = deque(Q)
cnt = 0 

while True:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq):
        dq.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
        
print(cnt)