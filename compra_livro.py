


qtd_livro = int(input('Quantos livros você vai comprar?'))
preco = 20
compra = qtd_livro * preco
if qtd_livro == 1:
     print("Sem desconto. Valor a pagar: 20,00 reais")
elif qtd_livro == 2 or 3:
   calculo = compra - (compra * 0.1)
   print(f"Comprando {qtd_livro} livros, terá um desconto de 10%. Valor a pagar: {calculo}")

elif qtd_livro == 4 or 5:
    calculo = compra - (compra * 0.2)
    print(f"Comprando {qtd_livro} livros, terá um desconto de 20%. Valor a pagar: {calculo}")

elif qtd_livro == 6 or 7:
     calculo = compra - (compra * 0.3)
     print(f"Comprando {qtd_livro} livros, terá um desconto de 30%. Valor a pagar: {calculo}")

else:
    print('Erro')