# 회장뽑기(플로이드-워샬 응용)

# ▣ 입력설명
# 입력의 첫째 줄에는 회원의 수가 있다.
# 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 
# 회원번호는 1부터 회원의 수만큼 번호가 붙어있다.
# 마지막 줄에는 -1이 두 개 들어있다
# ▣ 출력설명
# 첫째 줄은 회장 후보의 점수와 회장후보 수를 출력하고 두 번째 줄은 회장 후보를 모두 출력한다.

from collections import Counter

if __name__=="__main__":
    n = int(input())
    friend = [[50] * (n+1) for _ in range(n+1)]
    while True:
        a, b = map(int, input().split())
        if a== -1 and b == -1:
            break
        friend[a][b] = 1
        friend[b][a] = 1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])
    # 점수는 한 라인의 최대값으로 비교. 
    res = [50] * (n+1)
    for i in range(1, n+1):
        res[i] = max(friend[i][1:])
    min_score = min(res)
    
    out = []
    for i in range(1,n+1):
        if res[i] == min_score:
            out.append(i)

    print("%d %d" %(min_score, len(out)))
    for o in out:
        print(o, end=" ")
        
    
    
    

                
            
    
    