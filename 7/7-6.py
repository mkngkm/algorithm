# 알파코드

# 아스키 코드 'A' = 65, 'Z' = 90
# 변환 함수: ord() - 문자에서 숫자/ chr() - 숫자에서 문자

# 첫 번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0으로 시작하지는 않는다, 코드의 길이는 최대 50이다) 0이 입력되면 입력종료를 의미한다.

# 입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 그 가지수도 출력한다. 단어의 출력은 사전순으로 출력한다.

def dfs(L,res):
    global cnt
    if L == n:
        print(res)
        cnt += 1
    else:
        if 65<= int(code[L])+64 <=90:
            dfs(L+1, res+chr(int(code[L])+64))
        if L+1 < n and 74 <= int(code[L:L+2]) + 64 <= 90: # 두자릿수 숫자만 인정
            dfs(L+2, res + chr(int(code[L:L+2]) + 64))
            
if __name__=="__main__":
    code = input()
    n = len(code)
    cnt = 0
    dfs(0, '')
    print(cnt)
    
    
## 아스키 코드를 거의 안쓰는 경우
def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j] + 64), end="")
        print()
    else:
        for i in range(1, 27): # A 부터 Z 까지 다 확인
            if code[L]==i:
                res[P]=i
                DFS(L+1, P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                DFS(L+2, P+1)
        
if __name__=="__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1) # 에러 방지(2개 연달아 판별할떄)
    res = [0] * (n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)