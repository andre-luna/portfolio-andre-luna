with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    nomes = arquivo.readlines()

for nome in nomes:
    nome = nome.strip()
    if nome:
        print(f"Oi {nome}! Que bom te ver por aqui! ☀️💜")
