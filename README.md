
# Sistema Bancário com Registro e Login

Este projeto implementa um sistema bancário simples em Python, permitindo que os usuários se registrem, façam login e realizem operações bancárias básicas, como depósito, saque e visualização de extratos.
O projeto utiliza como base o codigo do professor Guilherme Carvalho (https://github.com/guicarvalho), porém com algumas modificações de otimização e acrescimo de funções como "Registro" e "Login".

## Funcionalidades

1. **Registrar Usuário**: Cria uma conta para um novo usuário com validação de CPF (ficticio) e senha.
2. **Login de Usuário**: Permite que um usuário existente faça login no sistema.
3. **Depósito**: Adiciona valores positivos ao saldo da conta do usuário logado.
4. **Saque**: Permite até três saques diários de no máximo R$ 500,00 cada, com verificação de saldo.
5. **Extrato**: Exibe todas as operações realizadas e o saldo atual.

## Como Utilizar

1. Clone o repositório:
    ```bash
    git clone https://github.com/HunterKNA/Desafio_01_DIO-NTT.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Desafio_01_DIO-NTT
    ```
3. Execute o script Python:
    ```bash
    python banco_app.py
    ```

## Exemplo de Uso

```python
# Exemplo de execução do sistema

[r] Registrar
[l] Login
[0] Sair

=> r
Insira seu username: user123
Insira seu nome: João Silva
Insira seu CPF sem pontuação: 12345678900
Insira seu e-mail: joao@exemplo.com
Crie sua senha, deve conter no mínimo 8 dígitos: senha123
Cadastro confirmado, user123!

[l] Login
=> l
Insira seu username: user123
Insira sua senha: senha123
Login bem-sucedido. Bem-vindo, user123!

[1] Depositar
[2] Sacar
[3] Extrato
[0] Logout

=> 1
Digite o valor do depósito: 200.00
Depósito realizado com sucesso!

=> 3
Extrato:
Depósito: R$ 200.00
Saldo: R$ 200.00

