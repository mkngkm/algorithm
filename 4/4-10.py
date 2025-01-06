n= int(input())
a = list(map(int, input().split()))

seq = [0] * n


for i in range(n):
     for j in range(n): 
          if a[i] == 0 and seq[j] == 0: #역수열 값이 0이되고 처음 만나는 0에 삽입
              seq[j] = i+1
              break
          elif seq[j] == 0:
              a[i] -=1  #역수열값이 0이 될때까지 반복(seq를-> 역수열값만큼 0찾으러감)
              

for x in seq:
     print(x, end=" ")



