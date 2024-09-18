import tkinter as tk
from tkinter import ttk

def processar():
        nome = entry_nome.get()
        label_resultado.config(text=f"Dados processados até mais:{nome}")

#criar janela
janela = tk.Tk()
janela.title("capturar dados")

#criar entry e label para o nome
label_nome = ttk.Label(janela, text="nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = ttk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

#botão para Processar o calculo
botao_calcular = ttk.Button(janela, text="processar", command=processar)

botao_calcular.grid(row=2, columnspan=2, padx=10, pady=10)
#iniciar loop
janela.mainloop()
