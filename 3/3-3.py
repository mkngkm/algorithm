n = 3
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(n):
    a, b = map(int, input().split())
    temp = arr[a-1:b]
    arr[a-1:b] = temp[::-1]

for x in arr:
    print(x, end = " ")