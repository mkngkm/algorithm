#나머지 print 전에 재귀 호출 후 print


def convert(x):
    if x == 0:
        return 
    else:
        convert(x//2)
        print(x%2, end="")

if __name__=="__main__":
    n = int(input())
    convert(n)
    
    