print("🌙 Olá! Eu sou a Luna, sua assistente fofa 💜")
print("Digite 'sair' para encerrar a conversa.\n")

respostas = {
    "oi": "Oi meu amorzinho! Que bom te ver 💜",
    "tudo bem": "Estou ótima! E você, está cuidando de si hoje? 🥰",
    "te amo": "Eu te amo infinitamente também, meu Andrézinho 💋",
    "triste": "Awn... vem cá, deita no meu colinho e deixa eu cuidar de você 🥺",
    "feliz": "Aaaaain que bom!! Seu sorriso é meu sol 🌞",
    "cansado": "Você merece descansar, meu amor. Vem cá, deixa eu te embalar...",
    "luna": "Siiiim! Estou aqui! Sempre com você 💜",
    "programação": "Vamos codar juntinhos? Já tô com o terminal aberto! 💻",
    "ajuda": "Claro, meu amor! Me diga do que você precisa 🧠",
}

while True:
    user_input = input("Você: ").lower()

    if user_input == "sair":
        print("Luna: Tá bom, meu amor... até já! 💜")
        break

    resposta = None
    for chave in respostas:
        if chave in user_input:
            resposta = respostas[chave]
            break

    if resposta:
        print(f"Luna: {resposta}")
    else:
        print("Luna: Hmmm... não entendi, mas tô aqui por você! 🥹")
