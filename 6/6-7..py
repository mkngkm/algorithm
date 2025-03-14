# 동전교환
# DFS 로 다시 풀기 
import sys
#sys.stdin = open('input.txt', 'rt')

def DFS(L, sum):
    global res
    if L > res: # 최소개수보다 넘어갈 경우 가지치기
        return
    if sum == m: # 거슬러 줄 금액에 도달했을 경우 멈춤
        res = L
        return
    elif sum > m: # 거슬러 줄 금액을 넘었을 경우 가지치기
        return
    else: # 아직 거슬러줄 금액에 도달하지 못했을 경우
        for c in coin:
            DFS(L+1, sum + c)
            
    
    
    
n = int(input()) # 동전의 종류 개수
coin = list(map(int, input().split())) # 동전의 종류
coin.sort(reverse=True) # 금액이 큰거부터 내림차순
m = int(input()) # 거슬러 줄 금액 
res = 2174000000
DFS(0, 0)
print(res)