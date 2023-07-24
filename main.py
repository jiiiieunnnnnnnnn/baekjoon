import sys
n = int(sys.stdin.readline())
m = list(map(int, input().split()))
a = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        a[i]=max(a[i], a[i-j]+m[j-1])
print(a[n])