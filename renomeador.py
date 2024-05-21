"""""""""""""""""""""
RENOMEADOR DE PASTAS '
"""""""""""""""""""""

import os

def renomear_pastas(diretorio):
    if not os.path.exists(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return
    lista_arquivos = os.listdir(diretorio)
    for arquivo in lista_arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        if os.path.isdir(caminho_completo):
            novo_nome = aplicar_regras(arquivo)
            novo_caminho = os.path.join(diretorio, novo_nome)
            os.rename(caminho_completo, novo_caminho)
            print("Pasta '{}' renomeada para '{}'.".format(arquivo, novo_nome))
            renomear_arquivos_na_pasta(novo_caminho, novo_nome)

def renomear_arquivos_na_pasta(caminho_pasta, novo_nome_pasta):
    arquivos_na_pasta = os.listdir(caminho_pasta)
    for arquivo in arquivos_na_pasta:
        caminho_completo_arquivo = os.path.join(caminho_pasta, arquivo)
        if os.path.isfile(caminho_completo_arquivo):
            extensao = os.path.splitext(arquivo)[1]
            novo_nome_arquivo = novo_nome_pasta + extensao
            novo_caminho_arquivo = os.path.join(caminho_pasta, novo_nome_arquivo)
            os.rename(caminho_completo_arquivo, novo_caminho_arquivo)
            print("Arquivo '{}' renomeado para '{}'.".format(arquivo, novo_nome_arquivo))

def aplicar_regras(nome_original):
    regras = {
        "Ipaussú": "4 - Ipaussú",
        "Univalem": "8 - Univalem",
        "Gasa": "9 - Gasa",
        "Barra Bonita": "11 - Barra Bonita",
        "Dois Corregos": "12 - Dois Corregos",
        "Destivale": "13 - Destivale",
        "Bonfim": "15 - Bonfim",
        "Tamoio": "16 - Tamoio",
        "Benalcool": "21 - Benalcool",
        "Paraguaçu": "58 - Paraguaçu",
        "Costa Pinto": "27 - Costa Pinto",
        "Santa Helena": "28 - Santa Helena",
        "São Francisco": "29 - São Francisco",
        "Diamante": "30 - Diamante",
        "Serra": "31 - Serra",
        "Rafard": "32 - Rafard",
        "Junqueira": "33 - Junqueira",
        "Mundial": "34 - Mundial",
        "Bom Retiro": "35 - Bom Retiro",
        "ARARAQUARA": "56 - ARARAQUARA",
        "Tarumã": "59 - Tarumã",
        "Maracaí": "60 - Maracaí",
        "Bionergia Costa Pinto": "225 - Bionergia Costa Pinto",
        "Barra": "234 - Barra",
        "CAR PIRACICABA": "830 - CAR PIRACICABA",
        "Dois Córregos": "604 - Dois Córregos"
    }
    return regras.get(nome_original, nome_original)

# Solicitar o caminho do diretório alvo
diretorio_alvo = input("Digite o caminho do diretório onde deseja renomear pastas e arquivos: ")
renomear_pastas(diretorio_alvo)

