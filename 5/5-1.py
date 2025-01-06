num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m>0 and stack[-1] <x: #지울수 있는 count 남아있고 stack값이 x보다 작으면 pop
        stack.pop()
        m -= 1
    stack.append(x)

if m!=0: #다 지우지 못했다면
    stack = stack[:-m]
res=''.join(map(str, stack))
print(res)