num = int(input())
for i in range(num):
    lista = input().split()

    num1 = float(lista[0])
    num2 = float(lista[1])
    num3 = float(lista[2])

    soma = ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10
    print('%.1f' % soma)
