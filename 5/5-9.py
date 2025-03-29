# Anagram(아나그램 : 구글 인터뷰 문제)

# 첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다.
# 단어의 길이는 100을 넘지 않습니다.

# 두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.

from collections import Counter

a = Counter()
b = Counter()
one = input()
for s in one: 
    a[s] += 1
two = input()
for s in two:
    b[s] += 1
    
if a == b:
    print("YES")
else:
    print("NO")
    
### 카운터 사용 안하고 딕셔너리만 이용했을때

a = dict()
b = dict()

str1 = input()
str2 = input()

for s in str1:
    a[s] = a.get(s, 0) + 1
for s in str2:
    b[s] = b.get(s, 0) + 1
    
for i in a.keys():
    if i in b.keys():
        if a[i] != b[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
    
    
### 딕셔너리 해쉬 개선 코드

for s in str1:
    a[s] = a.get(s, 0) + 1
for s in str2:
    b[s] = b.get(s, 0) - 1 # 뺄셈으로 개수 비교
    
for x in a:
    if a.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
    
    
### 리스트로 풀기(아스키 코드)

for s in str1:
    if s.isupper():
        a[ord(s)-65] += 1
    else:
        a[ord(s)-71] += 1
for s in str2:
    if s.isupper():
        b[ord(s)-65] += 1
    else:
        b[ord(s)-71] += 1
for i in range(52):
    if a[i] != b[i]:
        print("NO")
        break
else:
    print("YES")
        
