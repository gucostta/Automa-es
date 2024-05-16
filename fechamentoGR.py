import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
import subprocess
import sys

# Função para instalar dependências
def instalar_dependencias(dependencias):
    for pacote in dependencias:
        print(f"Instalando {pacote}...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", pacote], check=True)
            print(f"{pacote} instalado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar {pacote}: {e}")

# Lista de dependências a serem instaladas
dependencias = ["pandas", "pywin32"]

# Chama a função para instalar as dependências
instalar_dependencias(dependencias)

# Importa o win32com.client após tentar instalar
try:
    import win32com.client
except ImportError as e:
    print(f"Erro ao importar win32com.client: {e}")
    win32com = None

# Função para exibir os dados filtrados
def exibir_dados():
    unidades_selecionadas = [unidades_faturamento[i] for i in lb.curselection()]
    df_filtrado = df[df['Unidade Faturamento'].isin(unidades_selecionadas)]
    
    # Criar uma nova janela para exibir os dados filtrados
    window = tk.Toplevel(root)
    window.title("Dados Filtrados")
    
    # Criar um Treeview para exibir os dados
    tree = ttk.Treeview(window)
    tree["columns"] = list(df_filtrado.columns)
    tree["show"] = "headings"
    
    # Definir os cabeçalhos
    for col in df_filtrado.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    # Inserir os dados
    for index, row in df_filtrado.iterrows():
        tree.insert("", "end", values=list(row))
    
    tree.pack(expand=True, fill='both')

    # Adicionar botão para enviar e-mail com os dados filtrados
    email_button = tk.Button(window, text="Enviar por E-mail", command=lambda: enviar_email(df_filtrado, unidades_selecionadas))
    email_button.pack()

def enviar_email(df, unidades_selecionadas):
    if not win32com:
        print("A biblioteca win32com não está disponível. Não é possível enviar e-mails.")
        return
    
    # Criar o assunto do e-mail com a unidade selecionada e data
    unidade_filtro = ', '.join(unidades_selecionadas)
    mes_ano_filtro = pd.Timestamp.now().strftime('%B de %Y')
    assunto = f"Fechamento GR {unidade_filtro} {mes_ano_filtro}"
    
    # Criar o corpo do e-mail com os dados filtrados
    body = df.to_html(index=False)
    
    # Abrir o Outlook
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    # Destinatario fixo e pessoas em cópia
    destinatario_fixo = 'Gustavo.Costa2@raizen.com'
    pessoas_copia = 'Gustavo Amancio da Costa'
    
    # Preencher o e-mail
    mail.Subject = assunto
    mail.HTMLBody = body
    mail.To = destinatario_fixo
    mail.CC = pessoas_copia
    
    # Mostrar o e-mail ao usuário
    mail.Display(True)

# Carregar o arquivo Excel
df = pd.read_excel('Teste Macro GR.xlsx')

# Obter os valores únicos na coluna "Unidade Faturamento"
unidades_faturamento = df['Unidade Faturamento'].unique()

# Criar a janela principal
root = tk.Tk()
root.title("Filtro de Unidades de Faturamento")

# Label
label = tk.Label(root, text="Selecione as Unidades de Faturamento:")
label.pack()

# Listbox de seleção múltipla
lb = tk.Listbox(root, selectmode=tk.MULTIPLE)
for unidade in unidades_faturamento:
    lb.insert(tk.END, unidade)
lb.pack()

# Botão para filtrar dados
botao = tk.Button(root, text="Filtrar", command=exibir_dados)
botao.pack()

# Executar a aplicação
root.mainloop()







