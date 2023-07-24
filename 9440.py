import sys
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    li = n[1:]
    li = sorted(li)
    a = str()
    b = str()

    for i in range(len(li)):
        if li[i] != 0:
            a = str(li[i])
            b = str(li[i+1])
            li = li[:i]+li[i+2:]
            break

    for i in range(0,len(li),2):
        a += str(li[i])
        if i+1 < len(li):
            b += str(li[i+1])
    print(int(a)+int(b))