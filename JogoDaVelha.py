import random

print ("JOGO DA VELHA")

print ("Escolha posições no tabuleiro para poder jogar!")
print ("_ _ _")
print ("_ _ _")
print ("_ _ _")
print ("Escolha numeros de 1 a 9 para marcar suas jogadas!")
print ("1 2 3")
print ("4 5 6")
print ("7 8 9")

def imprime_bloco(bloco):
    print ("Jogadas feitas!\n")

    for indice in range(len(bloco)):
        print (bloco[indice], end=" ")
        if indice == 2 or indice == 5 or indice == 8:
            print ("")

def verifica_bloco(bloco, jogador):
   
    if bloco[0] == jogador and bloco[1] == jogador and bloco[2] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if bloco[3] == jogador and bloco[4] == jogador and bloco[5] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if bloco[6] == jogador and bloco[7] == jogador and bloco[8] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2

    if bloco[0] == jogador and bloco[3] == jogador and bloco[6] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if bloco[1] == jogador and bloco[4] == jogador and bloco[7] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if bloco[2] == jogador and bloco[5] == jogador and bloco[8] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
   
    if bloco[0] == jogador and bloco[4] == jogador and bloco[8] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if bloco[2] == jogador and bloco[4] == jogador and bloco[6] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2

    return 0


quantidade_escolhas = 0

bloco = ["_"] * 9

while True:

    escolha = int(input("Faça sua jogada: "))

    while bloco[escolha-1] != "_":
        print ("Jogada invalida!")
        imprime_bloco(bloco)
        escolha = int(input("Jogue novamente! "))

    bloco[escolha-1] = "X"
    quantidade_escolhas += 1

    vencedor = verifica_bloco(bloco,"X")

    if vencedor != 0:
        break

    if quantidade_escolhas == 9:
        break

    imprime_bloco(bloco)

    escolha_computador = random.randint(1,9)
    while bloco[escolha_computador-1] != "_":
        escolha_computador = random.randint(1,9)

    bloco[escolha_computador-1] = "O"
    quantidade_escolhas += 1

    vencedor = verifica_bloco(bloco,"O")
    if vencedor != 0:
        break
    imprime_bloco(bloco)

if vencedor == 1:
    print ("GGWP, Good game, well played")
elif vencedor == 2:
    print ("Você perdeu!")
else:
    print ("Deu velha! Jogo impatado!")

imprime_bloco(bloco)