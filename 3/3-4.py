#첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
n = int(input())
#두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다. 
a = list(map(int, input().split()))
#세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
m = int(input())
#네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다. 
b = list(map(int, input().split()))

#오름차순으로 정렬된 리스트를 출력합니다.

arr = a + b
arr.sort()
print(arr)

#다른 풀이
#sort() O(nlogn) -퀵정렬
#이미 정렬된것 합치는 것-> O(n)

p1=p2=0
c = []

while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
print(*c)