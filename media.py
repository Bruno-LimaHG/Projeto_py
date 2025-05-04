# Média
import os

while True:
    
    portuguese = input('Coloque o valor de português:')
    math = input('Coloque o valor de matemática:')

    calculo = float(portuguese) + float(math)
    media = calculo / 2

    if calculo >=5:
        os.system('cls')
        print (f'Média: {media}')
        print('Passou!')
        
  
    elif calculo <5:
        os.system('cls')
        print(f'Media: {media}')
        print('Não passou.')
        continue

        
  

    