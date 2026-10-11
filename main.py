import tkinter as tk
import random

tentativas = 0
LIMITE = 20

root = tk.Tk()
root.withdraw()

mensagens = [
    "kakakaka pegou virus otario",
    "foi fazendo trabalho no canva baixando imagem de gente velha",
    "seu pc vai explodir kkkkkkkk",
    "eu sempre volto",
    "nunca vai se livrar de mim"
]


def encerrar():
    root.destroy()


def criar_janela():

    janela = tk.Toplevel(root)

    janela.title("Avast Antivirus GUI")
    janela.geometry("350x160")

    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()

    # Sorteando a posição da janela
    x = random.randint(0, max(0, largura - 350))
    y = random.randint(0, max(0, altura - 200))

    janela.geometry(f"+{x}+{y}")

    mensagem = tk.Label(
        janela,
        text=random.choice(mensagens),
        font=("Arial", 12, "bold"),
        wraplength=320
    )

    mensagem.pack(pady=20)

    botao = tk.Button(
        janela,
        text="ENCERRAR BRINCADEIRA KKK",
        command=encerrar
    )

    botao.pack()

    def clicou_no_x():
        global tentativas

        janela.destroy()

        tentativas += 1

        if tentativas < LIMITE:
            root.after(200, criar_janela)
        else:
            encerrar()

    janela.protocol("WM_DELETE_WINDOW", clicou_no_x)


criar_janela()

root.after(30000, encerrar)

root.mainloop()