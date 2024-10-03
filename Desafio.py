import textwrap

def menu():
    menu_text = """\n
    ================ MENU ================
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair
    => """
    return input(textwrap.dedent(menu_text))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe o valor do depósito em R$: "))
            print(f"Valor depositado: R${valor:.2f}")  # Depuração: Exibe o valor informado
            saldo, extrato = depositar(saldo, valor, extrato)
            print(f"Saldo após depósito: R${saldo:.2f}")  # Depuração: Exibe o saldo após o depósito

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "2":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executar o programa
main()
