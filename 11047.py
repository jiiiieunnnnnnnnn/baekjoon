n, k = map(int, input().split())
m = [0]*n
cnt = 0
for i in range(n):
    m[i] = int(input())
m.sort(reverse=True)
for i in range(n):
    if k >= m[i]:
        a = k//m[i]
        cnt += a
        k -= m[i]*a
        if k == 0:
            break
print(cnt)