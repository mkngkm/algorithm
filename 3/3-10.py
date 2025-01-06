a = [list(map(int, input().split())) for _ in range(9)]
num = [1,2,3,4,5,6,7,8,9]
res = 1



#열검증

for i in range(9):
    if res and len(set(a[i])) == len(a[i]):
        col = []
        for j in range(9):
            col.append(a[j][i])

        if len(set(col)) == len(col):
            res = 1
        else:
            res = 0
            break
    else:
        res = 0
        break

i=0
dx = [0, 3, 6]
while res:
    sqr = []
    for j in range(3): 
        if res == 0:
            break
        for k in range(3):
            sqr.append(a[i][j+k])
            sqr.append(a[i+1][j+k])
            sqr.append(a[i+2][j+k])

        if len(set(sqr)) == len(sqr):
            res = 1
        else:
            res = 0
            break
    
    i += 3

if res:
    print("YES")
else:
    print("NO")
    

    

    
    





        


            
        
       
