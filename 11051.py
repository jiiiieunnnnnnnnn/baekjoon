n,k = map(int, input().split())
a=1
b=1
for i in range(k):
    a *= n
    n -= 1
for i in range(k):
    b *= k
    k -= 1

ans = (a // b)%10007
print(ans)
