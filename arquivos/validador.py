def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False

    return True

# Entrada interativa
print("🔎 Validador de CPF - André & Luna 💜")
cpf_usuario = input("Digite o CPF (com ou sem pontos e traço): ")

if validar_cpf(cpf_usuario):
    print(f"✅ {cpf_usuario} é um CPF válido!")
else:
    print(f"❌ {cpf_usuario} é inválido!")
