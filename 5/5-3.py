#문자열에서 10진수 확인하는 함수 isdigit(), isdecimal()

a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/': ##우선순위가 같은 *나 /만 pop한다. 
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(': ## + 나 - 보다 우선순위가 낮은 연산자를 다 출력한다 --(를 만난다면 stop
                res += stack.pop()
            stack.append(x)
        elif x == ')': ## (가 나올때까지 모든 연산자 출력
            while stack and stack[-1] != '(':
                res += stack.pop
            stack.pop()

while stack:
    res += stack.pop()

print(res)
