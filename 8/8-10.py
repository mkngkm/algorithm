# 가방문제(냅색 알고리즘)

# ▣ 입력설명
# 첫 번째 줄은 보석 종류의 개수와 가방에 담을 수 있는 무게의 한계값이 주어진다.
# 두 번째 줄부터 각 보석의 무게와 가치가 주어진다.
# 가방의 저장무게는 1000kg을 넘지 않는다. 보석의 개수는 30개 이내이다.
# ▣ 출력설명
# 첫 번째 줄에 가방에 담을 수 있는 보석의 최대가치를 출력한다.



## 냅색 알고리즘 사용
if __name__=="__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1) # 해당 무게(index)까지에서 최대로 가질 수 있는 가치
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, m+1):
            dy[j] = max(dy[j], dy[j-w] + v) # 기존 가치 + 새 보석 가치 와 해당 무게 원래가치 비교
            
    print(dy[m])












####시간 초과
# def dfs(w, v, L):
#     global res
#     if w > limit:
#         res = max(res, v - sorted_dia[L][1])
#     else:
#         for i in range(n): # 중복되어도 상관 없다..?
#             nw = sorted_dia[i][0]
#             nv = sorted_dia[i][1]
#             if nw <= limit:
#                 dfs(w + nw, v + nv, i)
                        
    
# if __name__=="__main__":
#     n, limit = map(int, input().split())
#     dia = list()
#     for _ in range(n):
#         a, b = map(int, input().split())
#         dia.append((a,b))
#     sorted_dia = sorted(dia, key=lambda x: dia[0], reverse=True)
#     ch = [0] * n  
#     res = 0
#     dfs(0, 0, 0)
#     print(res)


