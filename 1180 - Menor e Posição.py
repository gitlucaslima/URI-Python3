n = int(input())

x = input()
x = x.split()

for i in range(len(x)):
    x[i] = int(x[i])

mnum = x[0]
mpsc = 0
for j in range(1,len(x)):
    if x[j] < mnum:
        mnum = x[j]
        mpsc = j

print('Menor valor: %d' % mnum)
print('Posicao: %d' % mpsc)
