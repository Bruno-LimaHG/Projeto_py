entrada = input('Digíte um número inteiro: ')

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

        print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')


