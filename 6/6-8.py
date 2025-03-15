# N : 구슬 숫자1~ N
# M : 뽑을 개수

import sys
#sys.stdin = open('input.txt', 'rt')

#M개 뽑아서 일렬 나열, 사전순 오름차순
def DFS(L):
    global cnt
    if L == m:
        for r in res:
            print(r, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                res[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0
            
    


if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n+1)
    cnt = 0 
    DFS(0)
    print(cnt)
    