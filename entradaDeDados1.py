salario1 : float; salario2 : float
nome1 : str; nome2 : str; sexo : str
idade : int

nome1 = input("Digite o nome da primeira pessoa: ")
salario1 = float(input("Digite o salario da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
salario2 = float(input("Digite o salario da segunda pessoa: "))

idade = int(input("Digite uma pessoa: "))
sexo = input("Digite um sexo: (F/M)")

print(f"Nome 1: {nome1}")
print(f"Salario1: {salario1:.2f}")
print(f"Nome 2: {nome2}")
print(f"Salario 2: {salario2:.2f}")
print(f"Idade: {idade}")
print(f"Sexo: {sexo}")