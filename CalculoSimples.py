cpeca1, npeca1, vpeca1 = input().split()
cpeca2, npeca2, vpeca2 = input().split()

cpeca1 = int(cpeca1)
npeca1 = int(npeca1)
vpeca1 = float(vpeca1)

cpeca2 = int(cpeca2)
npeca2 = int(npeca2)
vpeca2 = float(vpeca2)

total = float(((npeca1 * vpeca1) + (npeca2 * vpeca2)))

print("VALOR A PAGAR: R$ %.2f"%total)
