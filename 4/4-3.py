# def sub_total(len, start, cnt):
#     if start >= n-1:
#         return cnt
#     cnt += 1
#     tot = 0

#     for i in range(start, n):
#         if( tot + songs[i] > len):
#             return sub_total(len, i, cnt)
#         else:
#             tot += songs[i]
#     return cnt

def sub_total(len, start):
   
    cnt = 1
    tot = 0
    for song in songs: ##굳이 재귀함수 쓰지 않고 반복문으로도 충분히 가능
        if tot + song > len:
            cnt += 1  # 새로운 DVD가 필요
            tot = song  # 새로운 DVD에 첫 노래 담음
        else:
            tot += song  # 현재 DVD에 노래 추가
    return cnt

n, m= map(int, input().split())
songs = list(map(int, input().split()))
res = 0 #곡 최소길이

lt = max(songs)
rt = sum(songs)
while lt <= rt:
    mid = (lt + rt) //2
    if sub_total(mid, 0) > m:
        lt = mid + 1
    elif sub_total(mid, 0) < m:
        rt = mid-1
    else:
        res = mid
        break
print(res)


