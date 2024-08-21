N = int(input("Qual a ordem da matriz? "))

matriz = [[0 for x in range(N)]for x in range(N)]

for i in range(0,N):
    for j in range(0,N):
        matriz[i][j] = int(input(f"Digite o elemento [{i},{j}]: "))

print("Diagonal principal: ")
for i in range(0,N):
    print(f"{matriz[i][i]} ", end="")

print()

somaNegativos = 0
for i in range(0,N):
    for j in range(0,N):
        if matriz[i][j] < 0:
            somaNegativos += 1
print("Quantidade de negativos = ", somaNegativos)
