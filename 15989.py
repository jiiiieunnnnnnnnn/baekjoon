import sys
n = int(sys.stdin.readline())
m = [0]*(n+1)
for i in range(1, n+1):
    m[i] = int(sys.stdin.readline())
k = max(m)
a = [1] * (k+1)
for i in range(1, k+1):
    a[i] = (i//2) + 1
ans = [0]*(n+1)
for i in range(1, n+1):
    x = m[i]//3
    for j in range(x+1):
        y = m[i]-(3*j)
        ans[i] += a[y]
for i in range(1, n+1):
    print(ans[i])