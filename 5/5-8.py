# 단어찾기

# 첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
#두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.

# 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.

from collections import Counter

n = int(input())
words = Counter()

for i in range(n):
    key = input()
    words[key] += 1  
    #그냥 = 1

for j in range(n - 1):
    note = input()
    words[note] -= 1
    # 그냥 = 0 해도 상관 x 넘 복잡하게 생각 x
    if words[note] == 0:
        del words[note]
print(*words.keys())