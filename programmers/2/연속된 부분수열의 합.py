# 연속된 부분 수열의 합


# 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다. (연속)
# 부분 수열의 합은 k입니다.
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
# 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.

### 시간 초과(brute-force) => 슬라이딩 윈도우(투 포인터)로 개선
def solution(sequence, k):
    n = len(sequence)
    max_sum = 0
    end = 0
    interval = n
    
    
    for start in range(n): # (인덱스 순서 대로니까 자동 정렬)
        while max_sum < k and end < n: # 작을때까지만 더함 
            max_sum += sequence[end]
            end += 1
        if max_sum == k and end-1-start < interval: # 길이가 더 짧으면 업데이트
            res = [start, end-1]
            interval = end-1-start
        max_sum -= sequence[start] # max_sum 에서 start 가 움직여야 앞의 while문의 end가 늘어날 수 있음

    
   
    return res


if __name__=="__main__":
    seq =  [1, 2, 3, 4, 5]
    k = 7
    print(solution(seq, k))