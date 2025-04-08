import os
import shutil

# Caminho da pasta a ser organizada
pasta_alvo = "C:\\Users\\SeuUsuario\\Documents"  # troque pelo seu caminho real!

# Tipos de arquivos e suas pastas correspondentes
tipos = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Vídeos': ['.mp4', '.mov', '.avi'],
    'Música': ['.mp3', '.wav'],
    'Compactados': ['.zip', '.rar'],
}

def organizar():
    for arquivo in os.listdir(pasta_alvo):
        caminho_arquivo = os.path.join(pasta_alvo, arquivo)
        if os.path.isfile(caminho_arquivo):
            nome, ext = os.path.splitext(arquivo)
            for categoria, extensoes in tipos.items():
                if ext.lower() in extensoes:
                    pasta_destino = os.path.join(pasta_alvo, categoria)
                    os.makedirs(pasta_destino, exist_ok=True)
                    shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                    print(f"Movido: {arquivo} ➜ {categoria}")
                    break

organizar()
