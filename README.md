# DoubleCheckSec - Sistema de Verificação em Duas Etapas com Python e PyOTP

![Veri2Step](https://example.com/veri2step-logo.png)

## Visão Geral

O DoubleCheckSec é um sistema de verificação em duas etapas (2FA) desenvolvido em Python usando a biblioteca PyOTP. O objetivo deste projeto é aumentar a segurança das contas de usuário, adicionando uma camada extra de autenticação antes de conceder acesso aos recursos protegidos.

A verificação em duas etapas é uma técnica de segurança amplamente adotada, na qual o usuário deve fornecer dois elementos de autenticação antes de ser autorizado a entrar em sua conta. No DoubleCheckSec, combinamos a autenticação tradicional (por exemplo, senha) com a autenticação baseada em um token único de uso único gerado por um aplicativo de autenticação (como o Google Authenticator).

## Recursos Principais

- Geração de códigos OTP (One-Time Password) usando o PyOTP.
- Suporte para algoritmos HOTP (HMAC-based One-Time Password) e TOTP (Time-Based One-Time Password).
- Integração fácil com aplicativos de autenticação como Google Authenticator.
- Proteção extra para contas de usuário e recursos confidenciais.
- Facilidade de integração em sistemas existentes baseados em Python.

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema. Se ainda não tiver o Python instalado, faça o download da versão mais recente em https://www.python.org/downloads/ e siga as instruções de instalação para o seu sistema operacional.

2. Clone este repositório em seu ambiente local usando o seguinte comando:

```
git clone https://github.com/seu-usuario/Veri2Step.git
```

3. Instale as dependências necessárias executando o seguinte comando:

```
pip install -r requirements.txt
```

## Como Usar

1. Importe a biblioteca `veri2step` para o seu projeto:

```python
import veri2step
```

2. Crie uma instância do Veri2Step, especificando o tipo de algoritmo a ser usado (HOTP ou TOTP) e um segredo único para a sua aplicação:

```python
# Exemplo de uso com TOTP (Time-Based One-Time Password)
verifier = veri2step.Verifier(algorithm='totp', secret='SEU_SEGREDO_AQUI')

# Exemplo de uso com HOTP (HMAC-Based One-Time Password)
# verifier = veri2step.Verifier(algorithm='hotp', secret='SEU_SEGREDO_AQUI')
```

3. Gere o código OTP:

```python
otp = verifier.generate_otp()
print("Código OTP gerado:", otp)
```

4. Peça ao usuário para inserir o código OTP gerado no aplicativo de autenticação.

5. Verifique o código OTP fornecido pelo usuário:

```python
user_otp = input("Insira o código OTP gerado pelo aplicativo de autenticação: ")
if verifier.verify(user_otp):
    print("Autenticação bem-sucedida! Acesso concedido.")
else:
    print("Código OTP inválido. Acesso negado.")
```

## Contribuindo

Se você quiser contribuir para o Veri2Step, sinta-se à vontade para abrir uma "Issue" ou enviar um "Pull Request" com suas melhorias ou correções de bugs.

## Licença

Este projeto está licenciado sob a licença MIT. Leia o arquivo [LICENSE](LICENSE) para obter mais detalhes.

## Contato

Para qualquer dúvida ou sugestão relacionada a este projeto, entre em contato com a equipe de desenvolvimento em dev.veri2step@example.com.

---

Agradecemos por utilizar o Veri2Step para aumentar a segurança em seus sistemas e contas de usuário. Esperamos que este projeto seja útil para suas necessidades de verificação em duas etapas!
