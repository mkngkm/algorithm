# 멀리뛰기 


def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    answer = dp[n] % 1234567
    return answer
print(solution(4))