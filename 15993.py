import sys
n = int(sys.stdin.readline())
x=[0]*(n+1)
for i in range(1, n+1):
    x[i] = int(sys.stdin.readline())
arr = [[0 for j in range(2)] for i in range(max(x)+1)]
arr[1][0]=0
arr[1][1]=1
arr[2][0]=1
arr[2][1]=1
arr[3][0]=2
arr[3][1]=2

for i in range(4, max(x)+1):
    arr[i][1] = (arr[i-1][0] + arr[i-2][0] + arr[i-3][0]) % 1000000009
    arr[i][0] = (arr[i-1][1] + arr[i-2][1] + arr[i-3][1]) % 1000000009

for i in range(1, n+1):
    print(arr[x[i]][1], end=" ")
    print(arr[x[i]][0])