import os


def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se o CPF não possui todos os dígitos iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula e valida os dois dígitos verificadores
    for i in range(9, 11):
        valor = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if str(digito) != cpf[i]:
            return False

    return True


def valida_cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False

    # Verifica se o CPF não possui todos os dígitos iguais
    if cnpj == cnpj[0] * 14:
        return False

    # Calcula e valida os dois dígitos verificadores
    multiplicador = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    soma1 = soma2 = 0

    for n in range(1, len(multiplicador)):
        soma1 += int(cnpj[n-1]) * int(multiplicador[n])

    digito1 = soma1 % 11

    if digito1 < 2:
        digito1 = 0
    elif digito1 >= 2:
        digito1 = 11 - digito1

    for n in range(len(multiplicador)):
        soma2 += int(cnpj[n]) * int(multiplicador[n])

    digito2 = soma2 % 11

    if digito2 < 2:
        digito2 = 0
    elif digito2 >= 2:
        digito2 = 11 - digito2

    return cnpj[-2:] == str(digito1) + str(digito2)


def nova_consulta():
    while True:
        # Repetição para continuar a consulta
        fim = str(input('\nDeseja fazer outra consulta? [S/N] ')).upper()[0]
        if fim in 'SN':
            os.system('cls')
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if fim == 'N':
        os.system('cls')
        return False
    else:
        return True


def iniciar():
    acao = True
    while acao is True:
        os.system('cls')
        print('Qual documento deseja validar?')
        print('Digite 1 para CPF')
        print('Digite 2 para CNPJ')
        opcao = input('==> ')

        if opcao == '1':
            cpf = input('Digite o CPF: ')
            if valida_cpf(cpf):
                print(f'\nO CPF {cpf} está CORRETO.')
            else:
                print(f'\nO CPF {cpf} está INVÁLIDO.')
        elif opcao == '2':
            cnpj = input('Digite o CNPJ: ')
            if valida_cnpj(cnpj):
                print(f'\nO CNPJ {cnpj} está CORRETO.')
            else:
                print(f'\nO CNPJ {cnpj} está INVÁLIDO.')
        else:
            print('Opção inválida!')

        acao = nova_consulta()


if __name__ == '__main__':
    iniciar()
