# 단어찾기

# 첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
#두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.

# 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.

from collections import Counter

n = int(input())

words = Counter()

# 노트에 적힌 단어 개수 세기
for i in range(n):
    key = input()
    words[key] += 1  

# 시에 등장한 단어 개수 감소
for j in range(n - 1):
    note = input()
    words[note] -= 1
    if words[note] == 0:
        del words[note]

# 남은 한 개의 단어 출력
print(*words.keys())  


