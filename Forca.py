###Jogo da Forca###

from random import choice

def exibir(palavra, tentativas):
    caracteres = (letra if letra in tentativas else '_' for letra in palavra)
    return ' '.join(caracteres)

palavras = ['bruxa', 'caveira', 'vampiro', 'lobisomem', 'abobora']
palavra = choice(palavras)

tentativas = set()
erros = 0

while True:
    print('Que os jogos comecem:', exibir(palavra, tentativas))

    while True:
        tentativa = input('Digite uma letra para sobreviver: ').lower()
        if tentativa not in tentativas:
            tentativas.add(tentativa)
            break
        print('Você já fez essa tentativa.')

    if '_' not in exibir(palavra, tentativas) or tentativa == palavra:
        print('Você sobreviveu')
        break

    if tentativa not in palavra:
        print(f'Você errou! Só te restam {5-erros} tentativas')
        erros += 1

    if erros == 6:
        print('Você morreu!')
        break


###Mega Sena###

from random import randint

def gerar_seis_numeros():
    numeros = []

    while len(numeros) < 6:
        # Executando o random
        x = randint(0, 60)
        # verificando se o numero existe na lista, caso exista não é adicionado
        if x not in numeros: numeros.append(x)

    return numeros

x = gerar_seis_numeros()
print(x)


###Maior, menor e media###

lista = [1,5,13,4,20,300,68,34,1050,780]
maior = 0 
menor = 0
soma = 0
for c in range(0,10):
  if c == 0:
    maior = menor = lista[c]
  else:
    if lista [c] > maior:
      maior = lista[c]
  
    if lista [c] < menor:
      menor = lista[c]
      
for i in lista:
  soma += i
media = soma/10

print("O maior elemento é",maior)
print("O menor elemento é",menor)
print("A media dos elementos é",media)