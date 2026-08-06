import os, json
def arquivo_existe(nome):
    return os.path.exists(nome)
    
def criar_arquivo(nome):
    with open(nome, 'w') as arquivo:
        json.dump([], arquivo, indent=4)

def salvar_arquivo(nome, dados):
    with open(nome, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def ler_arquivo(nome):
    with open(nome, 'r') as arquivo:
        objeto = json.load(arquivo)
    return objeto