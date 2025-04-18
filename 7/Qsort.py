#퀵 정렬

#pivot 을 중심으로 큰건 왼쪽 작은건 오른쪽  -> 전위 순회
#pivot 보다 i 가 작을때만 pos 와 교환

def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)

if __name__=="__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print('Before sort:', end=" ")
    print(arr)
    Qsort(0, 9)
    print()
    print("After sort: ", end =" ")
    print(arr)