farinhap=0.2
feijaop=0.5
arrozp=0.5
contrap=1
farinha=5
feijão=8
arroz=8
contra=26
carrinho=[]
preço=[]
peso=[]
print("bem vindo ao mercado dois obesos")
print("lista de produtos disponiveis:")
print("arroz, cod:1")
print("feijão, cod:2")
print("contra, cod:3")
print("farinha, cod:4")
print("=_=-"*42)
dec= int(input("quantos produtos deseja comprar?:"))
print("=_=-"*42)
for c in range(1, dec+1):
    add= int(input("Digite qual os produtos vc deseja adicionar, digite o código:"))
    carrinho.append(add)
    if add == 4:
        preço.append(farinha)
        peso.append(farinhap)
    elif add == 2:
        preço.append(feijão)
        peso.append(feijaop)
    elif add == 1:
        preço.append(arroz)
        peso.append(arrozp)
    elif add== 3:
        preço.append(contra)
        peso.append(contrap)
print("=_=-"*42)
somp= sum(peso)
if somp<= 0.1:
    print("o frete será R$9.00")
    preço.append(9)
elif somp > 0.1 and somp <=0.4:
    print("o frete será R$13.00")
    preço.append(13)
elif somp >0.4 and somp <=0.6:
    print("o frete será R$18.00")
    preço.append(18)
elif somp >0.601 and somp <= 5:
    print("o frete será R$30.00")
    preço.append(30)
print("totalizando:R${}".format(sum(preço)))