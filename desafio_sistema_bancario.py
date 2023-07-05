import os
menu = """=== Digite uma opção ===

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

========================

=> """

saldo = 0
LIMITE_POR_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

os.system('cls')

while True:
    
    opcao = input(menu).lower()

    if opcao == "d":
        os.system('cls')

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print('\n'+ '=' * 32)
            print(f'Depósito de R$ {valor:.2f} realizado')
            input('Aperte ENTER para continuar')
            os.system('cls')

        else:
            print('\n'+ '=' * 32)
            print("Operação inválida! Só é possível depositar valores positivos.")
            input('Aperte ENTER para continuar')
            os.system('cls')

    elif opcao == "s":
        os.system('cls')      
          
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print('\n'+ '=' * 32)
            print("Não é possível concluir a operação! Saldo insuficiente.")
            input('Aperte ENTER para continuar')
            os.system('cls')

        elif valor > LIMITE_POR_SAQUE:
            print('\n'+ '=' * 32)
            print(f"Não é possível concluir a operação. O limite por saque atual é R$ {LIMITE_POR_SAQUE:.2f}")
            input('Aperte ENTER para continuar')
            os.system('cls')

        elif numero_saques >= LIMITE_SAQUES:
            print('\n'+ '=' * 32)
            print(F"Não é possível concluir a operação! Sua conta só permite {LIMITE_SAQUES} saques diários.")
            input('Aperte ENTER para continuar')
            os.system('cls')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print('\n'+ '=' * 32)
            print(f"operação concluída com sucesso!Saque de R$ {valor}.")            
            input('Aperte ENTER para continuar')
            os.system('cls')

        else:
            print('\n'+ '=' * 32)
            print("Operação falhou! O valor informado é inválido.")
            input('Aperte ENTER para continuar')
            os.system('cls')

    elif opcao == "e":
        os.system('cls')
        print("\n================ EXTRATO ================\n")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"\nSaldo:    R$ {saldo:.2f}\n")
        print("==========================================")
        input('Aperte ENTER para continuar')
        os.system('cls')

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
