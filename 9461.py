a = [1,1,1,2,2]
n = int(input())
for i in range(n):
    m =int(input())
    if m > 5:
        for _ in range(m-5):
            a.append(a[-1]+a[-5])
    print(a[m-1])
    a= [1,1,1,2,2]
