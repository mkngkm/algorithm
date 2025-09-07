# n개의 최소 공배수



def lcm(a, b):
    m = min(a, b)
    for k in range(m, a*b+1):
        if k % a == 0 and k % b == 0:
            return k
        

def solution(arr):
    answer = 0
    
    # 두 수와 나머지의 최소공배수도 가능
    dp = [0] * (len(arr))
    arr.sort()
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = lcm(arr[i], dp[i-1])
    answer = dp[len(arr) - 1]
    return answer



# def nlcm(num):
#     answer = 0
#     l=num[0]
#     for i in range(1,len(num)): # 앞에까지의 최소공배수와 다른거의 최소공배수를 구하면 됨
#         l=lcm(l,num[i])
#     return l

# def lcm(a,b): # 두개 곱한걸 최대공약수로 나누면 최소공배수가 나옴
#     c=gcd(a,b)
#     return int(a*b/c)

# def gcd(a,b): ## 최대공약수
#     if not a%b:
#         return b
#     else:
#         return gcd(b,a%b)

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(nlcm([2,6,8,14,15]))