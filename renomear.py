import os

def renomear_pastas(diretorio):
    # Lista todos os arquivos e pastas no diretório
    lista_arquivos = os.listdir(diretorio)

    for arquivo in lista_arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        # Verifica se o caminho é um diretório
        if os.path.isdir(caminho_completo):
            # Aplicar regras de renomeação
            novo_nome = aplicar_regras(arquivo)
            novo_caminho = os.path.join(diretorio, novo_nome)
            # Renomeia a pasta
            os.rename(caminho_completo, novo_caminho)
            print("Pasta '{}' renomeada para '{}'.".format(arquivo, novo_nome))
            
            # Renomear todos os arquivos dentro da pasta
            renomear_arquivos_na_pasta(novo_caminho, novo_nome)

def renomear_arquivos_na_pasta(caminho_pasta, novo_nome_pasta):
    # Lista todos os arquivos na pasta
    arquivos_na_pasta = os.listdir(caminho_pasta)
    for arquivo in arquivos_na_pasta:
        caminho_completo_arquivo = os.path.join(caminho_pasta, arquivo)
        if os.path.isfile(caminho_completo_arquivo):
            # Extrai a extensão do arquivo
            extensao = os.path.splitext(arquivo)[1]
            # Novo nome do arquivo
            novo_nome_arquivo = novo_nome_pasta + extensao
            novo_caminho_arquivo = os.path.join(caminho_pasta, novo_nome_arquivo)
            # Renomeia o arquivo
            os.rename(caminho_completo_arquivo, novo_caminho_arquivo)
            print("Arquivo '{}' renomeado para '{}'.".format(arquivo, novo_nome_arquivo))

def aplicar_regras(nome_original):
    if nome_original == "Ipaussú":
        return "4 - Ipaussú"
    elif nome_original == "Univalem":
        return "8 - Univalem"
    elif nome_original == "Gasa":
        return "9 - Gasa"
    elif nome_original == "Barra Bonita":
        return "11 - Barra Bonita"
    elif nome_original == "Dois Corregos":
        return "12 - Dois Corregos"
    elif nome_original == "Destivale":
        return "13 - Destivale"
    elif nome_original == "Bonfim":
        return "15 - Bonfim"
    elif nome_original == "Tamoio":
        return "16 - Tamoio"
    elif nome_original == "Benalcool":
        return "21 - Benalcool"
    elif nome_original == "Paraguaçu":
        return "58 - Paraguaçu"
    elif nome_original == "Costa Pinto":
        return "27 - Costa Pinto"
    elif nome_original == "Santa Helena":
        return "28 - Santa Helena"
    elif nome_original == "São Francisco":
        return "29 - São Francisco"
    elif nome_original == "Diamante":
        return "30 - Diamante"
    elif nome_original == "Serra":
        return "31 - Serra"
    elif nome_original == "Rafard":
        return "32 - Rafard"
    elif nome_original == "Junqueira":
        return "33 - Junqueira"
    elif nome_original == "Mundial":
        return "34 - Mundial"
    elif nome_original == "Bom Retiro":
        return "35 - Bom Retiro"
    elif nome_original == "ARARAQUARA":
        return "56 - ARARAQUARA"
    elif nome_original == "Tarumã":
        return "59 - Tarumã"
    elif nome_original == "Maracaí":
        return "60 - Maracaí"
    elif nome_original == "Bionergia Costa Pinto":
        return "225 - Bionergia Costa Pinto"
    elif nome_original == "Barra":
        return "234 - Barra"
    elif nome_original == "CAR PIRACICABA":
        return "830 - CAR PIRACICABA"
    elif nome_original == "Dois Córregos":
        return "604 - Dois Córregos"
    # Adicione mais regras conforme necessário
    else:
        # Se nenhum correspondente, retorna o nome original
        return nome_original

# Diretório onde estão as pastas a serem renomeadas
diretorio_alvo = r"Z:\Beneficios\6. VA VR VT\2024\02. Cesta Básica - TESTE\Macro - Lista Branca\Arquivos txt"

renomear_pastas(diretorio_alvo)

