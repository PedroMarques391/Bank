from typing import List
from time import sleep

from Models.cliente import Cliente
from Models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print("||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||| ATM |||||||||||||||||")
    print("||||||||||| ESPECTRAL BANK |||||||||||")
    print("||||||||||||||||||||||||||||||||||||||")

    print('Selecione uma Opção no menu: ')
    print("[1] - Criar Conta")
    print("[2] - Efetuar Saque")
    print("[3] - Efetuar Depósito")
    print("[4] - Efetuar Tranferência")
    print("[5] - Listar Contas")
    print("[6] - Sair do Sistema")

    opcao: int = int(input('-> '))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Obrigado, volte sempre!!")
        sleep(2)
    else:
        print("Opção inválida, tente uma das opções listadas abaixo.")
        sleep(1)
        menu()


def criar_conta() -> None:
    print("Informe os dados do cliente: ")

    nome: str = input("Nome do Cliente: ")
    email: str = input("Email do Cliente: ")
    cpf: str = input("CPF do Cliente: ")
    data_nascimento: str = input("Data de nascimento do Cliente: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso!")
    print("Dados da Conta: ")
    print('|||||||||||||||||||||||||')
    print(conta)
    sleep(3)
    print("Voltando para o menu..")
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da conta: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor da saque: '))

            conta.saca(valor)
            print(f"O valor R$ {valor} foi sacado com sucesso! ")

        else:
            print(f"Não encontrada a conta de numero{numero}.")

    else:
        print("Ainda não existem contas cadastradas.")
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o número da conta depósito: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Dígite o valor para depósito: "))

            conta.depositar(valor)
            print(f"O valor R$ {valor} foi depositado na sua conta de numero {numero}")
        else:
            print(f'A conta de número {numero} não foi encontrada')
    else:
        print("Ainda não existem contas cadastradas.")
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input("Informe o número da sua conta: "))

        contas_o: Conta = buscar_conta_por_numero(numero_o)

        if contas_o:
            numero_d: int = int(input("Digite o número da conta de destino: "))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))

                contas_o.transferir(conta_d, valor)

                print(f"O valor de R$ {valor} foi transferido para a conta de {conta_d.cliente.nome}"
                      f"com CPF {conta_d.cliente.cpf}")
            else:
                print(f'A conta destino de número {numero_d} não foi encontrada.')
        else:
            print(f"A sua conta de número{numero_o} não foi encontrada.")
    else:
        print("Ainda não existem contas cadastradas.")
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print("Listagem de contas")
        for conta in contas:
            print(conta)
            print('|||||||||||||||||')
            sleep(2)
        menu()
    else:
        print('Não existem contas cadastradas! \nVolte ao menu.')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == "__main__":
    main()



