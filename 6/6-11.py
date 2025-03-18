#N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수는 몇 개가 있는지 출력하는 프로그램을 작성하세요.



import sys

def dfs(L, now, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(now, n): #a의 인덱스번호
            if ch[i] == 0:
                ch[i] = 1
                dfs(L+1, i, sum + a[i])
                ch[i] = 0



if __name__=="__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    sum = 0
    cnt = 0
    ch = [0] * n
    dfs(0, 0, sum)
    print(cnt)
    
    
    