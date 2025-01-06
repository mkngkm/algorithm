#이진탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid +1, end)
    

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort() #반환값 None

result = binary_search(a, m, 0, n-1)
if (result):
    print(result +1 )
