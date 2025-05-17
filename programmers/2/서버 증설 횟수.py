### 서버 증설 횟수

# 0시에서 23시까지의 시간대별 게임 이용자의 수를 나타내는 1차원 정수 배열 players, 서버 한 대로 감당할 수 있는 최대 이용자의 수를 나타내는 정수 m, 
# 서버 한 대가 운영 가능한 시간을 나타내는 정수 k가 주어집니다. 
# 이때, 모든 게임 이용자를 감당하기 위한 최소 서버 증설 횟수를 return 하도록 solution을 완성해 주세요.


def solution(players, m, k):
    cnt = [0] * 24 # 증설된 서버의 수 
    plus = [0] * 24 # 증설 횟수
    
    for i in range(len(players)):
        needs = players[i] // m # 필요 서버 수
        if cnt[i] < needs: # 서버 증설이 필요하다면,
            plus[i] = needs-cnt[i]
            for j in range(i, i+k):
                if j < len(players): # player 범위 내라면,
                    cnt[j] += plus[i]
    answer = sum(plus)
    return answer

if __name__=="__main__":
    arr = [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0]
    m = 5
    k = 1
    print(solution(arr, m , k))
    

    

## 다른 풀이
# def solution(players, m, k):
#     answer = 0
#     servers = [0]*(24+k)
#     nowmax = m
#     for i,p in enumerate(players):
#         nowmax -= servers[i]*m
#         if nowmax<=p:
#             addservers = ((p-nowmax)//m)+1
#             answer += addservers
#             nowmax+=addservers*m
#             servers[i+k]+=addservers
#     return answer
