import random
import os

palavras = ['python', 'computador', 'programador', 'algoritmo', 'teclado', 'monitor', 'internet']
palavra_secreta = random.choice(palavras)
letras_corretas = []
tentativas = 6
forca = [
    """
      +---+
          |
          |
          |
        =====
    """,
    """
      +---+
      O   |
          |
          |
        =====
    """,
    """
      +---+
      O   |
      |   |
          |
        =====
    """,
    """
      +---+
      O   |
     /|   |
          |
        =====
    """,
    """
      +---+
      O   |
     /|\\  |
          |
        =====
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
        =====
    """,
    """
      +---+
      O   |
     /|\\  |
     / \\  |
        =====
    """
]

print('Bem vindo ao Jogo da Forca')

while tentativas > 0:
    exibicao = ''
    for letra in palavra_secreta:
        if letra in letras_corretas:
            exibicao += letra
        else:
            exibicao += '_'


    erros = 6 - tentativas
    print (forca[erros])
    print(f'Palavra {exibicao}')
    print(f'Letras já tentadas: {','.join(sorted(letras_corretas))}')
    print(f'Tentativas restantes: {tentativas}\n')


    if '_' not in exibicao:
        print(f'Parabéns, você ganhou!! A palavra era: {palavra_secreta}')
        break

    chute = input('Digite uma letra: ').lower()

    if len(chute) != 1 or not chute.isalpha():
         print('Digite apenas uma letra válida!')
         input('Pressione Enter para continuar...')
         continue
    
    if chute in letras_corretas:
         print('Você já tentou essa letra, tente outra.')
         input('Pressione Enter para continuar...')
         continue
    
    letras_corretas.append(chute)


    if chute in palavra_secreta:
         print('Boa, você acertou uma letra!')
    else:
         print('Letra errada.')
         tentativas -= 1

    input('Pressione Enter para continuar...')


if tentativas == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(forca[-1])
        print(f'Que pena, você perdeu! A palavra secreta era: {palavra_secreta}') 