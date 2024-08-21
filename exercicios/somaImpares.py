print("Digite dois numeros: ")
x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y
    y = aux

soma = 0
for i in range(x+1, y):
    if i % 2 != 0:
        soma += i

print("A soma dos impares = ", soma)