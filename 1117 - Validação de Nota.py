num = int(input())
i = 0
aux = 0

for i in range(num):
    for x in range(4):
        x += 1
        aux += 1
        if x == 4:
            print("PUM")
        else:
            print(aux, end=" ")