n = int(input())
m = [0]*n
for i in range(n):
    m[i] = int(input())
m.sort()
ans = [0]*n
for i in range(n):
    ans[i] = m[i]*(n-i)
print(max(ans))