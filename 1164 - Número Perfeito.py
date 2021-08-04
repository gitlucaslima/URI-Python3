n = int(input())

for x in range(0, n):
    num = int(input())

    i = 1
    aux = 0

    while i < num:
        if num % i == 0:
            aux += i

        i += 1

    if aux == num:
        print('%d eh perfeito' % num)
    else:
        print('%d nao eh perfeito' % num)