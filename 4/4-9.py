n = int(input())
a = list(map(int,input().split()))

#AA는 내 풀이 4-9는 정답

lt = 0
rt = n-1
last = 0
res = ""
tmp = []
while lt<=rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last :
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0: #둘다 작아서 양쪽에서 아무것도 안가져온 상태
        break 
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt += 1
    tmp.clear() #양쪽 넣어서 더 작은거 하나 찾고 다 비움

print(len(res))
print(res)

    