import sys
n = int(sys.stdin.readline())
x=[0]*(n+1)
y=[0]*(n+1)
for i in range(1, n+1):
    x[i], y[i] = map(int, input().split())
arr = [[0 for j in range(max(x)+1)] for i in range(max(x)+1)]
arr[1][1]=1
arr[2][1]=1
arr[2][2]=1
arr[3][1]=1
arr[3][2]=2
arr[3][3]=1
for i in range(4, max(x)+1):
    for j in range(1, i+1):
        arr[i][j] = (arr[i-1][j-1]+arr[i-2][j-1]+arr[i-3][j-1])%1000000009
for i in range(1, n+1):
    print(arr[x[i]][y[i]])