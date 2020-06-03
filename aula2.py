import math

opcao = int(raw_input("Selecione uma opcao:\n 1 - Realizar um calculo\n 2 - Usar Funcoes Math\n 3 - Sair\n"))

if opcao == 1:
  num1 = int(raw_input("Informe o primeiro numero:\n"))
  num2 = int(raw_input("Informe o segundo numero\n"))

  operacao = int(raw_input("Selecione uma operacao:\n 1 - Soma\n 2 - Subtracao\n 3 - Multiplicacao\n 4 - Divisao\n 5 - Exponenciacao\n 6 - Extracao\n"))

  if operacao == 1:
    resultado = num1 + num2
  elif operacao == 2:
   resultado = num1 - num2
  elif operacao == 3:
    resultado = num1 * num2
  elif operacao == 4:
    resultado = num1 / num2
  elif operacao == 5:
    resultado = num1 ** num2
  elif operacao == 6:
    resultado = num1 // num2
  else:
    print("Operacao invalida!")
    exit()

  print("\n\nResultado: " + str(resultado)) 
elif opcao == 2:
  num1 = int(raw_input("Informe um numero:\n"))
  operacao = int(raw_input("Selecione uma operacao:\n 1 - Ceil\n 2 - Floor\n 3 - Sqrt\n 4 - Abs\n"))
  
  if operacao == 1:
    resultado = math.ceil(num1)
  elif operacao == 2:
   resultado = math.floor(num1)
  elif operacao == 3:
    resultado = resultado = math.sqrt(num1)
  elif operacao == 4:
    resultado = math.abs(num1)
  else:
    print("Opcao invalida!")
    exit()

  print("\n\nResultado: " + str(resultado))

elif opcao == 3:
  exit()

else:
  print("Opcao invalida!")
  exit()
