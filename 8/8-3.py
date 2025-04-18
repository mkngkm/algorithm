# 도전과제 : 계단오르기(Top-Down : 메모이제이션)

# ▣ 입력설명
# 첫째 줄은 계단의 개수인 자연수 N(3≤N≤45)이 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 올라가는 방법의 수를 출력합니다.

def dfs(n):
    if dy[n] > 0:
        return dy[n]
    if n==1 or n==2:
        return n
    else:
        dy[n] = dfs(n-1) + dfs(n-2)
        return dy[n]
        
if __name__=="__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(dfs(n))
