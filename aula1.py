nome_1 = str(raw_input("Digite seu nome completo: "))
idade_1 = int(raw_input("Digite sua idade: "))
salario_1 = float(raw_input("Digite seu salario: "))

nome_2 = str(raw_input("Digite seu nome completo: "))
idade_2 = int(raw_input("Digite sua idade: "))
salario_2 = float(raw_input("Digite seu salario: "))

nome_3 = str(raw_input("Digite seu nome completo: "))
idade_3 = int(raw_input("Digite sua idade: "))
salario_3 = float(raw_input("Digite seu salario: "))

totalIdade = idade_1 + idade_2 + idade_3
totalSalario = salario_1 + salario_2 + salario_3

mediaIdade = (totalIdade/3)
mediaSalario = (totalSalario/3)

print("Media de idade: ")
print(mediaIdade)

print("Media de salario: ")
print(int(mediaSalario))