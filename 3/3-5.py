#N, M 입력받기
n, m = map(int, input().split())

#수열 입력받기
a = list(map(int, input().split()))
#수열에서 연속된 수의 합이 M이 되는 경우의수


#슬라이딩 윈도우 (Sliding Window) 또는 투 포인터 (Two Pointer) 알고리즘
lt = 0
rt =1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt<n:
            tot += a[rt]
            rt +=1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
