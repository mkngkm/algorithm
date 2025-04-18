# 최대 부분 증가수열(LIS - dp)

# ▣ 입력설명
# 첫째 줄은 입력되는 데이터의 수 N(2≤N≤1,000, 자연수)를 의미하고,
# 둘째 줄은 N개의 입력데이터들이 주어진다.
# ▣ 출력설명
# 첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.


##마지막 항이라고 생각하고 앞에 몇개 있는지를 봐야함
    

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    dy = [0] * (n+1)
    a.insert(0, 0)
    a[1] = 1
    for i in range(2, n+1):
        max = 0
        for j in range(i-1, 0, -1): # 거꾸로감
            if a[j] < a[i] and dy[j] > max:
                max = dy[j]
        dy[i] = max + 1
        if dy[i] > res:
            res = dy[i]    
print(res)
        
        
                
        
        
        
        