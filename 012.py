produto = float(input('Digite o valor do produto em R$: '))

desconto  = produto * 5 / 100
produtod = produto - desconto

print('O valor do desconto é R${:.2f}\nE o  novo valor do produto será R${:.2f}  '.format(desconto,produtod))