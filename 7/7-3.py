# 양팔 저울

# 첫 번째 줄에 자연수 K(3<=K<=13)이 주어집니다.
# 두 번째 줄에 K개의 각 추의 무게가 공백을 사이에 두고 주어집니다. 각 추의 무게는 1부터 200,000까지이다.

# 첫 번째 측정이 불가능한 가지수를 출력하세요.

def dfs(L, sum):
    global cnt
    if sum > s:
        return
    if L == k:
        if 0<sum<=s: # 음수인 경우는 양수와 대칭이니까 보지 않아도 되고, set 사용 -> 중복 제거
            res.add(sum)
    else:
        dfs(L+1, sum + choo[L]) # 포함 - 합
        # dfs(L+1, abs(sum-choo[L])) # 포함 - 차
        dfs(L+1, sum - choo[L])
        dfs(L+1, sum) # 포함 x
                
 
if __name__=="__main__":
    k = int(input())
    choo = list(map(int, input().split()))
    s = sum(choo)
    #ch = [0] * (s + 1)
    res = set()
    dfs(0, 0)
    # print(ch.count(0))
    print(s - len(res))
    
