num = int(input())

vetor = []*num

for i in range(0, num):
    vetor.append(input())
    if num == 0:
        break

print(sorted(vetor)[-2])
print(vetor)

