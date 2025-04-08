import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Gerar e exibir 3 senhas seguras
for i in range(3):
    print(f"Senha {i+1}: {gerar_senha()}")
