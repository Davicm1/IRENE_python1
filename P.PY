import matplotlib.pyplot as a
val=[12,24,50,60]
nm=['DAVI','VALDEMIR', 'WILL','MANO CU']
a.pie(val, labels=nm, autopct='%1.1f%%', startangle=140)
a.title('ex de gráfico')
a.show()