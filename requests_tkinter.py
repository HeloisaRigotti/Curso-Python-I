
import tkinter as tk
from tkinter import ttk, messagebox
import requests

# ==========================================
# CONFIGURAÇÕES DA JANELA
# ==========================================

janela = tk.Tk()
janela.title("Sistema de Produtos - Fake Store API")
janela.geometry("1100x650")
janela.configure(bg="#172554")
janela.resizable(True, True)

# ==========================================
# ESTILIZAÇÃO
# ==========================================

estilo = ttk.Style()
estilo.theme_use("clam")

# Estilo da tabela
estilo.configure(
    "Treeview",
    background="#FFFFFF",
    foreground="#1E293B",
    rowheight=35,
    fieldbackground="#FFFFFF",
    font=("Arial", 10)
)

# Cabeçalho da tabela
estilo.configure(
    "Treeview.Heading",
    background="#2563EB",
    foreground="#FFFFFF",
    font=("Arial", 11, "bold"),
    padding=10
)

# Seleção da tabela
estilo.map(
    "Treeview",
    background=[("selected", "#93C5FD")],
    foreground=[("selected", "#172554")]
)

# ==========================================
# CABEÇALHO
# ==========================================

titulo = tk.Label(
    janela,
    text="🛒 FAKE STORE API",
    font=("Arial", 24, "bold"),
    bg="#172554",
    fg="#FFFFFF"
)
titulo.pack(pady=(20, 5))

subtitulo = tk.Label(
    janela,
    text="CONSULTA DE PRODUTOS",
    font=("Arial", 11),
    bg="#172554",
    fg="#BFDBFE"
)
subtitulo.pack(pady=(0, 20))

# ==========================================
# FUNÇÃO PARA CARREGAR PRODUTOS
# ==========================================

def carregar_produtos():

    try:
        # Consultar API
        resposta = requests.get(
            "https://fakestoreapi.com/products",
            timeout=10
        )

        resposta.raise_for_status()

        produtos = resposta.json()

        # Limpar tabela
        for item in tabela.get_children():
            tabela.delete(item)

        # Inserir produtos
        for produto in produtos:

            id_produto = produto["id"]
            titulo_produto = produto["title"]
            titulo_categoria = produto["category"]
            preco = produto["price"]

            tabela.insert(
                "",
                "end",
                values=(
                    id_produto,
                    titulo_produto,
                    f"$ {preco:.2f}"
                )
            )

        # Atualizar quantidade
        quantidade.config(
            text=f"TOTAL DE PRODUTOS: {len(produtos)}"
        )

        status.config(
            text="Produtos carregados com sucesso!",
            fg="#86EFAC"
        )

    except requests.RequestException as erro:

        messagebox.showerror(
            "Erro de conexão",
            f"Não foi possível acessar a API.\n\n{erro}"
        )

        status.config(
            text="Erro ao carregar produtos!",
            fg="#FCA5A5"
        )

    except (ValueError, KeyError, TypeError) as erro:

        messagebox.showerror(
            "Erro nos dados",
            f"Não foi possível interpretar os produtos.\n\n{erro}"
        )

# ==========================================
# FRAME PRINCIPAL DA TABELA
# ==========================================

frame = tk.Frame(
    janela,
    bg="#FFFFFF",
    bd=0
)

frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)

# ==========================================
# BARRA DE ROLAGEM
# ==========================================

scroll = ttk.Scrollbar(
    frame,
    orient="vertical"
)

# ==========================================
# TABELA DE PRODUTOS
# ==========================================

tabela = ttk.Treeview(
    frame,
    columns=("ID", "PRODUTO", "CATEGORIA", "PREÇO"),
    show="headings",
    yscrollcommand=scroll.set
)

scroll.config(command=tabela.yview)

# Cabeçalhos
tabela.heading("ID", text="ID")
tabela.heading("PRODUTO", text="NOME DO PRODUTO")
tabela.heading("CATEGORIA", text="NOME DO CATEGORIA")
tabela.heading("PREÇO", text="PREÇO")

# Largura das colunas
tabela.column(
    "ID",
    width=70,
    anchor="center"
)

tabela.column(
    "PRODUTO",
    width=800,
    anchor="w"
)

tabela.column(
    "CATEGORIA",
    width=800,
    anchor="w"
)

tabela.column(
    "PREÇO",
    width=130,
    anchor="center"
)

# Posicionamento
tabela.pack(
    side="left",
    fill="both",
    expand=True
)

scroll.pack(
    side="right",
    fill="y"
)

# ==========================================
# RODAPÉ
# ==========================================

rodape = tk.Frame(
    janela,
    bg="#172554"
)

rodape.pack(
    fill="x",
    padx=25,
    pady=15
)

# Quantidade de produtos
quantidade = tk.Label(
    rodape,
    text="TOTAL DE PRODUTOS: 0",
    font=("Arial", 11, "bold"),
    bg="#172554",
    fg="#FFFFFF"
)

quantidade.pack(side="left")

# Botão atualizar
botao = tk.Button(
    rodape,
    text="⟳ ATUALIZAR PRODUTOS",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="#FFFFFF",
    activebackground="#1D4ED8",
    activeforeground="#FFFFFF",
    cursor="hand2",
    relief="flat",
    padx=20,
    pady=10,
    command=carregar_produtos
)

botao.pack(side="right")

# ==========================================
# STATUS
# ==========================================

status = tk.Label(
    janela,
    text="Aguardando consulta...",
    font=("Arial", 9),
    bg="#172554",
    fg="#BFDBFE"
)

status.pack(pady=(0, 12))

# ==========================================
# EXECUÇÃO
# ==========================================

# Carregar produtos ao iniciar
carregar_produtos()

# Manter janela aberta
janela.mainloop()
