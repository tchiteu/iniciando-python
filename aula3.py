# coding: utf-8

import random

totalTurnos = 15
totalNavios = 7
totalLinhas = 10
totalColunas = 10
contAcertos = 0
contJogadas = 0

def geraMatriz(valor) :
  matriz = []

  for l in range(totalLinhas) :
    linha = []

    for c in range(totalColunas):
      linha.append(valor)
    
    matriz.append(linha)

  return matriz

mapa = geraMatriz("~")
mapaReal = geraMatriz(0)

def desenhaNavios() :
  contadorDeNavios = 1

  while (contadorDeNavios <= totalNavios) :
    linhaNavio = random.randint(0, totalLinhas - 1)
    colunaNavio = random.randint(0, totalColunas - 1)

    if (mapaReal[linhaNavio][colunaNavio] == 0) :
      mapaReal[linhaNavio][colunaNavio] = 1
      
      contadorDeNavios += 1

def solicitaJogada(tipo) :
  if (tipo == "linha") :
    quantidade = totalLinhas
  else :
    quantidade = totalColunas

  repetir = True
  while (repetir) :
    mensagem = "Digite a " + tipo + " (1 à " + str(quantidade) + "): "

    valor = int(input(mensagem)) - 1

    if (valor < 0 or valor >= quantidade) :
      repetir = True
      print("Faça uma jogada válida!!")
    else :
      repetir = False

  return valor

def VerificaJogadaRepetida(linha, coluna) :
  if (mapa[linha][coluna] != "~") :
    return True
  else :
    return False

def desenhaMapa() :
  print("\n")

  numerosColunas = ''

  for c in range(totalColunas):
    numero = str(c + 1)
    numerosColunas += numero + " "

  print("        " + numerosColunas)

  for l in range(totalLinhas):
    numero = str(l + 1)
    
    if (l >= 9) :
      espacamento = "     "
    else :
      espacamento = "      " 

    linha = espacamento + numero + " "

    for c in range(totalColunas):
      linha += mapa[l][c] + " "

    print(linha)

  print("\n")

def continuarJogo() :
  if (contAcertos == totalNavios) :
    return False
  elif (contJogadas == totalTurnos) :
    return False
  else :
    return True

desenhaNavios()

while (continuarJogo()) :
  contJogadas += 1

  print("\n Jogada: " + str(contJogadas) + "/" + str(totalTurnos) + "\n Acertos: " + str(contAcertos) + "/" + str(totalNavios))
    
  desenhaMapa()

  repetir = True
  while (repetir) :
    linha = solicitaJogada("linha")
    coluna = solicitaJogada("coluna")

    if (VerificaJogadaRepetida(linha, coluna)) :
      print("Você já fez essa jogada")

      repetir = True
    else :
      repetir = False

  if (mapaReal[linha][coluna] == 1) :
    mapa[linha][coluna] = "x"

    contAcertos += 1

    print("Acertou!")
  else :
    mapa[linha][coluna] = "o"
    
    print("\n Errou!")

if (contAcertos == totalNavios) :
  print("\n\n\n")

  desenhaMapa()
  
  print("\n\n Você venceu!")
  print("\n Quantidade de jogadas para vencer: " + str(contJogadas))
else :
  print("\n\n")
  desenhaMapa()
  print("\n\n")

  print("Você perdeu!")