import sys
input = sys.stdin.readline
n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]
a = [[[0]*3 for _ in range(n)] for _ in range(n)]
a[0][1][0] = 1

for i in range(2,n):
    if m[0][i] == 0 :
        a[0][i][0] = a[0][i-1][0]

for i in range(1,n):
    for j in range(1,n):
        if m[i][j] == 0 and m[i][j-1] == 0 and m[i-1][j] == 0:
            a[i][j][2] = a[i-1][j-1][0]+a[i-1][j-1][1]+a[i-1][j-1][2]
        if m[i][j] == 0:
            a[i][j][1] = a[i-1][j][1] + a[i-1][j][2]
            a[i][j][0] = a[i][j-1][0] + a[i][j-1][2]
print(a[n-1][n-1][0]+a[n-1][n-1][1]+a[n-1][n-1][2])