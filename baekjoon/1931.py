# 회의실 배정

# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

if __name__=="__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(tuple(map(int, input().split())))
    sorted_a = sorted(a, key=lambda x: (x[1], x[0])) # 끝나는 시간이 같다면, 시작 시간이 빠른 회의가 먼저 오게 해야 함(중요!!!!!!)
    cnt = 1
    tmp = sorted_a[0][1] # 첫번째로 끝나는 시간
    for i in range(1, n):
        s, t = sorted_a[i]
        if tmp <= s:
            cnt += 1
            tmp = t # 끝나는 시간 업데이트
    print(cnt)
        