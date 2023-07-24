import sys
n = int(sys.stdin.readline())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = b[0]
ans=0
for i in range(n-1):
    ans = ans + (c*a[i])
    if b[i] >= b[i+1]:
        c=b[i+1]
print(ans)