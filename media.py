
while True:
   list=[]
   nome=str(input("digite o nome do aluno:"))
   nt1=float(input("digite a nota de português:"))
   nt2=float(input("digite a nota de matemática:"))
   nt3=float(input("digite a nota de ciências:"))
   nt4=float(input("digite sua nota de humanas:"))
   cal=((nt1+nt2+nt3+nt4)/4)
   if cal <= 3:
       print ("reprovado")
   elif cal >= 3.6 and cal <=6:
      print("recuperação")
   else:
      print("aprovado")
      print(cal)
      list.append(nome)
      list.append(cal)
      print(list)