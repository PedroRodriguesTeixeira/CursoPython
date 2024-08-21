import math

base = float(input('Digite a base do retangulo: '))
altura = float(input('Digite a altura do retangulo: '))
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(pow(base, 2) + pow(altura, 2))

print(f"Area = {area:.4f}")
print(f"Perimetro = {perimetro:.4f}")
print(f"Diagonal = {diagonal:.4f}")