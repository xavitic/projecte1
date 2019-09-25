def equacio_recta(x,m,d):
    return m * x + d

print("Introdueix pendent de la recta: ")
pendent = input()
pendent = int(pendent)

print("Introdueix constant de la recta: ")
constant = input()
constant = int(constant)

print("Introdueix punt X de la recta: ")
x = input()
x = int(x)

y = equacio_recta(x,pendent,constant)

print("El punt y és: " + str(y))





