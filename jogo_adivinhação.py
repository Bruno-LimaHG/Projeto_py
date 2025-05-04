import random
import os
numero_secreto = random.randint(1, 50)
tentativas = 0
limite_tentativas = 5

while tentativas < limite_tentativas:
    
    
    print('Jogo de Adivinhação')
    tentativa = int(input('Insira um número de 1 à 50: '))

    tentativas += 1

    if tentativa == numero_secreto:
        os.system('cls')
        print('Parabéns, você acertou!')
        break
    elif tentativa > numero_secreto:
        os.system('cls')
        print("O número é menor do que você digitou.")
        continue
    elif tentativa < numero_secreto:
        os.system('cls')
        print('O número é maior do que você digitou.')
        continue
if tentativas == limite_tentativas:
        print('Você atingiu o limite de tentativas.')
        print(f'Resposta: {numero_secreto}')
