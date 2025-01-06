#문자열에서 10진수 확인하는 함수 isdigit(), isdecimal()
#연산자를 만나면 두개 pop해서 두개+연산자=> 연산결과로 교체 : 강의보고 알게됨. 

a = input()
stack = []
res = 0
for x in a:
    if not x.isdecimal():
        exp = stack.pop(-2) + x + stack.pop()
        res = eval(exp)
        stack.append(str(res))           
        # print(exp)
        # print(stack) 
    else:
        stack.append(x)
            

print(res)
