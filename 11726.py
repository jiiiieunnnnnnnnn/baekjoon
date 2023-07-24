a=[1,2]
n=int(input())
for i in range(2,n):
    a.append(a[-2]+a[-1])
print(a[n-1]%10007)