
print("OS PRODUTOS DISPONVEIS SÃO: OPALA R$60.000,00! GOL R$15.000,00! SANTANA R$25.000,00! E CHEVETTE R$10.000,00!")
prod=[]
dec= int(input("quantos produtos vc deseja comprar?:"))
for c in range(1, dec+1):
   prod1= input("digite o código do produto que deseja inserir:")
   prod2= prod1.lower()
   if prod2 == "chevette":
      prod.append(10000)
   elif prod2 == "gol":
      prod.append(15000)
   elif prod2 == "santana":
      prod.append(25000)
   elif prod2 == "opala":
      prod.append(60000)
cal= sum(prod)*12/100
print("o total a pagar é R${}, com mais 12% de ICMS de R${}, totalizando: R${}".format(sum(prod), cal, sum(prod)+cal ))
fom= int(input("digite 1 para o pagamento ser avista, 2 para ser no débito e 3 para ser no crédito:"))
if fom == 1:
   print("enviando fatura...")
elif fom == 2:
   print("enviando fatura...")
else:
   dec1= int(input("deseja parcelar em quantas vezes?, lembrando que pode ser feito de 1 até 12 vezes.:"))
   if dec1>12:
      print("invalido, não pode ser feito mais de 12 vezes.")
   else:
      print("ficou de {}x sem juros, totalizando {} parcelas de {}.".format(dec1, dec1, (sum(prod)+cal)/dec1))