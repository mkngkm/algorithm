a = [list(map(int, input().split())) for _ in range(7)]

count = 0
rowRes = True
colRes = True
for i in range(7):
    for j in range(7):
        #행
        for k in range(2):
            if a[i][j+k] == a[i][j+4-k]:
                rowRes = True
            else:
                rowRes = False
            if(rowRes):
                count += 1
            #열
            if a[j][i+k] == a[j][i+4-k]:
                colRes = True
            else:
                colRes = False
            if(colRes):
                count += 1

print(count)
            
        
       