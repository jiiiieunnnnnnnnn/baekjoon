import math
import sys
n = int(sys.stdin.readline())
arr = [0] * (n + 1)
ans = []
for i in range(1, n + 1):
    x = int(i**(1/2))
    for j in range(1,x+1):
        m = i - (j * j)
        ans.append(arr[m] + 1)
    arr[i] = min(ans)
    ans = []

print(arr[n])
