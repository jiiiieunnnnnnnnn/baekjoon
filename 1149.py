n = int(input())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
for i in range(1, n):
    x[i][0] = min(x[i-1][1], x[i-1][2]) + x[i][0]
    x[i][1] = min(x[i-1][0], x[i-1][2]) + x[i][1]
    x[i][2] = min(x[i-1][0], x[i-1][1]) + x[i][2]
print(min(x[n-1]))