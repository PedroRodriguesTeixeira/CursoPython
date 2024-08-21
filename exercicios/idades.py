print("Dados da primeira pessoa:")
nome1 = input("Digite seu nome: ")
idade1 = int(input("Digite sua idade: "))

print("Dados da segunda pessoa:")
nome2 = input("Digite seu nome: ")
idade2 = int(input("Digite sua idade: "))

media = (idade1 + idade2) / 2.0

print(f"A idade media de {nome1} e {nome2} eh de {media:.1f} anos.")