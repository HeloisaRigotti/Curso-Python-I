from os import system
system('cls')

import tkinter as tk # para abrir janela do window
from tkinter import messagebox

def exibir_mesangem():
    # Recuperar Informação digitadas no Entry
    nome = campo.get()

    if nome:
        messagebox.showinfo(
            "Bem vindo(a)", 
             f'Olá {nome}. Se você está vendo esta mensagem, é porque clicou no botão!'
        )
    else:
        messagebox.showwarning(
        "Ops", 
        "Primeiro você precisa digitar o seu NOME!"
        )

# criando uma janela
janela = tk.Tk()
# inserindo titulo para a janela
janela.title("Montando Interface com Python")
# Definindo dimensões
janela.geometry("600x400")
titulo = tk.Label(
    janela,
    text="Olá Mudo",
    font=("Arial", 20)
).pack(pady=10)

botao = tk.Button(
    janela,
    text="Clique aqui",
    font=("Arial", 12),
    command=exibir_mesangem
).pack(pady=10)

# abrir campo para digitar
campo = tk.Entry(
    janela,
    font=("Arial", 12),
    width=20
)
campo.pack(pady=10)








# Excutar janela Tkinter
janela.mainloop()


