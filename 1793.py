a = [0] * 251
a[0] = 1
a[1] = 1
a[2] = 3
while (True):
    try:
        n = int(input())
        for i in range(3, n+1):
            a[i] = a[i - 1] + 2 * a[i - 2]
        print(a[n])
    except:
        break
