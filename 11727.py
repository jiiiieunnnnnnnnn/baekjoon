n = int(input())
a = [1,3]

for i in range(2,n+1):
    a.append(a[i-1] + 2*a[i-2])

print(a[n-1]%10007)