# a =input()

# res = 0
# stack = []
# i = 0
# while i < len(a):
#     if a[i] == '(' and a[i+1] == ')': #레이저는 스택에 넣지 않고 값을 더함 
#         if stack:
#             stack = [s + 1 for s in stack]
#         i = i+2
#         continue

#     if a[i] == '(':
#         stack.append(1)
#     else: #')'를 만나면 pop
#         res += stack.pop()
#     i += 1
    
# print(res)

##강의 풀이 ##닫는 괄호를 만났들때 바로 앞 괄호를 확인해서 레이저인지 확인
##레이저면 pop 후 남아있는 괄호 개수를 더하고 레이저가 아니면(막대끝) pop 후 더하기 1
##( 면 push )면 pop인데 위의 경우 따져서 pop

###내코드
# a =input()

# res = 0
# stack = []
# before=''
# for x in a:
#     if x == '(':
#         stack.append(x)
#         before = x
#     else:
#         if before == '(': #레이저면
#             stack.pop()
#             res += len(stack)
#         else: #막대끝이면
#             stack.pop()
#             res += 1
#         before = x

# print(res)


##강의 코드
s=input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
            

