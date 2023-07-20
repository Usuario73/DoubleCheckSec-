import veri2step

def main():
    # Defina o segredo exclusivo para sua aplicação (deve ser compartilhado com o aplicativo de autenticação)
    secret = 'SEU_SEGREDO_AQUI'

    # Crie uma instância do Veri2Step usando TOTP (Time-Based One-Time Password)
    verifier = veri2step.Verifier(algorithm='totp', secret=secret)

    # Gere o código OTP
    otp = verifier.generate_otp()
    print("Código OTP gerado:", otp)

    # Peça ao usuário para inserir o código OTP gerado pelo aplicativo de autenticação
    user_otp = input("Insira o código OTP gerado pelo aplicativo de autenticação: ")

    # Verifique o código OTP fornecido pelo usuário
    if verifier.verify(user_otp):
        print("Autenticação bem-sucedida! Acesso concedido.")
    else:
        print("Código OTP inválido. Acesso negado.")

if __name__ == "__main__":
    main()
