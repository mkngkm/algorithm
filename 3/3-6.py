# Online Python-3 Compiler (Interpreter)
n = int(input())

#a = []
#for i in range(n):
#    a.append(list(map(int, input().split())))

a = [list(map(int, input().split())) for _ in range(n)]
   
# max_tot = 0  
# diag_tot = 0
# diag_tot2 = 0
# for j in range(n):
#     row_sum = sum(a[j])  # 행의 합
#     col_sum = sum(a[i][j] for i in range(n))  # 열의 합
#     if row_sum > col_sum :
#         max_tot = max(row_sum, max_tot)
#     else:
#         max_tot = max(col_sum, max_tot)
# for m in range(n):
#     diag_tot += a[m][m]
#     diag_tot2 += a[m][n-m-1]

# if diag_tot > diag_tot2:
#     max_tot = max(max_tot, diag_tot)
# else:
#     max_tot = max(max_tot, diag_tot2)
# print(max_tot)

#다른 풀이(max 안씀)

largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1 > largest:
    largest = sum
if sum2 > largest:
    largest = sum2
print(largest)

    