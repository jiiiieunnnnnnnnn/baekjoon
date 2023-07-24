n = int(input())
m = list(map(int, input().split()))
m.sort()
cnt=0
for i in range(n):
    cnt += m[i]*(n-i)
print(cnt)