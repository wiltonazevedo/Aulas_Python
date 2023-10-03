valor = int(input('qual o valor da compra?'))

if valor > 2000 :
    print(f'vc ganhou um desconto de 20%. o valor do seu desconto e de {valor *0.80}')

elif valor >=1000:
    print(f'vc ganhou um desconto de 10%. o valor do seu desconto e de {valor *0.90}')

else :
    print(f' vc não ganhou desconto. o valor da sua compra e de {valor}')

