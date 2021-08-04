ant1 = 0
ant2 = 1
prox = 0
n = 0

n = int(input())

print("{} {}" .format(ant1, ant2), end="")
i = 2
for i in range(n-i):
    prox = ant1 + ant2
    print(end=" ")
    print(prox, end="")
    ant1 = ant2
    ant2 = prox

print("")
