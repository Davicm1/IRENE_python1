#programa estoque com frete
#variaveis de memória
vcont="s"
vprod=""
vq=0
vvalor=0
vpeso=0
#criando lista
lprod=[]
lvalor=[]
lq=[]
lpeso=[]
print("sistema de vendas")
while vcont=="s":
      vprod=input("digite o produto:")
      vvalor=float(input("valor:"))
      vq=int(input("quantidade:"))
      vpeso=float(input("peso:"))
      if vpeso<= 100:
         vvalor+9
      elif vpeso >= 101 and vpeso >=400:
         vvalor+10
      elif vpeso >=401 and vpeso <=600:
         vvalor+18
      elif vpeso >=601 and vpeso <= 5000:
         vvalor+30
      lvalor.append(vvalor)
      lq.append(vq)
      lpeso.append(vpeso)
      dec=input("deseja parar? s ou n?")
      if dec == "s":
            break
      else:
            print("+-="*45)
print("o valor ficou R${} com R${} de frete.".format(sum(lvalor),))
