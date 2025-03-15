# 수열 추측하기- 순열, 파스칼 응용

# N : 정수
# F: 가장 밑에 줄에 있는 수 


import sys
#sys.stdin = open('input.txt', 'rt')

def DFS(L, sum):
    if L == n and sum == f:
        for res in p:
            print(res, end = " ")
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum + (p[L] * b[L]))
                ch[i] = 0
 
if __name__=="__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n+1)
    for i in range(1, n): # 파스칼 한줄의 조합(개수) 구하기, 첫번째랑 마지막은 어차피 1이니까 제외. (중요 ****)
        b[i] = b[i-1] * (n - i) // i
    DFS(0, 0)
        
    