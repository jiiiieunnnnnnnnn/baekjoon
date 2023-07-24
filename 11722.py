n = int(input())
m = list(map(int, input().split()))
a=[1]*n
for i in range(1,n):
    for j in range(i):
        if m[i] < m[j]:
            a[i] = max(a[i], a[j]+1)
print(max(a))