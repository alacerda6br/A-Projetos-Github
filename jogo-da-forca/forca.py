
import random as rd
import os

lt_fruta = ['ABACAXI', 'ABACATE', 'MANGA', 'MAMAO', 'TANGERINA', 'BANANA', 'LARANJA',
            'LIMAO', 'MARACUJA', 'PESSEGO']
lt_objeto = ['LAPIS', 'CANETA', 'BORRACHA', 'CADERNO', 'TOALHA', 'COLHER', 'GARFO',
             'FACA', 'MESA', 'TELEVISAO']

letras_usuario = []

chances = 7

ganhou = False


def palavra_aleatoria(lista):
    # função para escolher uma palavra aleatória
    tamanho = len(lista)
    sorteio = rd.randint(1, tamanho-1)
    palavra_aleatoria = lista[sorteio]
    return palavra_aleatoria


def menu():
    global palavra, tipo
    while True:
        print('* * * JOGO DA FORCA * * *')
        print('Escolha uma opção!')
        print('1 para Frutas\n2 para Objetos')
        lt = str(input('==> '))

        if lt == '1':
            palavra = palavra_aleatoria(lt_fruta)
            os.system('cls')
            tipo = ('A palavra é uma FRUTA.')
            break
        elif lt == '2':
            palavra = palavra_aleatoria(lt_objeto)
            os.system('cls')
            tipo = ('A palavra é um OBJETO.')
            break
        else:
            print('Opção inválida, tente novamente!')


def continuar_jogo():
    global fim, letras_usuario, chances, ganhou
    while True:
        # Repetição para continuar a jogar
        fim = str(input('Deseja jogar novamente? [S/N] ')).upper()[0]
        if fim in 'SN':
            letras_usuario = []
            chances = 7
            ganhou = False
            os.system('cls')
            break
        print('ERRO! Por favor, digite apenas S ou N.')


def logica_jogo():
    while True:
        global chances, ganhou
        # criar a nossa lógica
        print('* * * JOGO DA FORCA * * *')
        print(tipo)
        for letra in palavra:
            if letra.upper() in letras_usuario:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print('')
        print(f'Letras já escolhidas: {letras_usuario}')
        print(f'Você ainda tem {chances} vidas.')
        tentativa = input('Escolha uma letra para adivinhar: ').upper()
        os.system('cls')
        letras_usuario.append(tentativa)
        if tentativa not in palavra:
            chances -= 1

        ganhou = True
        for letra in palavra:
            if letra not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou is True:
            break


def jogar():
    while True:
        menu()

        logica_jogo()

        if ganhou:
            print(f'Parabéns, você ganhou! A palavra era {palavra}.')
        else:
            print(f'Você perdeu! A palavra era {palavra}.')

        continuar_jogo()

        if fim == 'N':
            os.system('cls')
            break


jogar()
