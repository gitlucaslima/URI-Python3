i = 0
x = 0
num = 0
xin = 0
xot = 0

x = int(input())

for i in range(x):
    num = int(input())

    if num >= 10 and num <= 20:
        xin = xin+1
    else:
        xot = xot+1

print("%d in" % xin)
print("%d out" % xot)
