n = int(input())
apply = []
for _ in range(n):
    h, w = map(int, input().split())
    apply.append((h,w))

apply.sort()
print(apply)
we = 0
cnt = n
for i in range(n):
    w = apply[i][1]
    for j in range(i, n):
        we = apply[j][1]
        if w < we :
            cnt -= 1
            break;      
print(cnt)
                    