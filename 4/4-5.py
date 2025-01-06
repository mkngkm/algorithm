n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))

meeting.sort(key = lambda x : (x[1], x[0])) #끝나는 시간 기준 정렬 -> 시작시간
et = 0 #end time
cnt = 0
for s, e in meeting:
    if s>=et: #겹치지 않으면
        et = e #새로운 endtime이 새 e
        cnt += 1
print(cnt)