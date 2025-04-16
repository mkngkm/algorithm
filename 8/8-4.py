# 도전과제 : 돌다리 건너기(Bottom-Up)

n = int(input())
dp1= [0] * (n+1)
dp2 = [0] * (n+1)
dp1[1] = 1
dp1[2] = 2
for i in range(3, n+1):
    dp1[i]= dp1[i-1] + dp1[i-2]
    dp2[i] = dp1[i-1] * 2 + dp1[i-2]
print(dp2[n])