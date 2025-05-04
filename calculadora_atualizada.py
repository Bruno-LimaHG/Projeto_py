import os

Iniciar = input('Deseja utilizar a calculadora 2.0? "Sim" ou "Não"')
    
while True:

    if Iniciar == "Não" or Iniciar == "não":
        print('Até mais...')
        break

    
    
    
    
    
    if Iniciar == "Sim" or Iniciar == "sim":
        valor1 = input('Insira o primeiro valor: ')
        valor2 = input('Insira o segundo valor:  ')
        operador = input('Escolha um operador: (+-*/) ')

        

        print('Resultado abaixo: ')
        
        
        if operador == '+':
            adicao = float(valor1) + float(valor2)
            print(f'resultado {adicao:.2f}')
            continue
        elif operador == '-':
            subtracao = float(valor1) - float(valor2)
            print(f'Resultado {subtracao:.2f}')
            continue
        elif operador == '*':
            multiplicacao = float(valor1) * float(valor2)
            print(f'resultado {multiplicacao:.2f}')
            continue
        elif operador == '/':
            divisao = float(valor1) / float(valor2)
            print(f'Resultado {divisao:.2f}')
            continue
    
       
        

    



