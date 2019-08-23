# -*- coding: utf-8 -*-
import os

print('\033[;1m' + '\033[1;42m' + '\033[1;97m')
print()


class _Getch:
    """Similar ao getch do C++. Verifica o sistema e executa o comando certo"""
    def __init__(self):
        if os.name == 'nt':
            self.impl = _GetchWindows()  # atribui getch para windows
        elif os.name == 'posix':
            self.impl = _GetchUnix()  # atribui o getch para UNIX
        else:
            print('ERRO! Sistema não suportado')

    def __call__(self): return self.impl()  # chama o getch correspondente


class _GetchUnix:
    """Classe chamada quando num sistema UNIX"""

    def __call__(self):
        import getch  # importa o getch
        return getch.getch()  # retorna o metodo getch


class _GetchWindows:
    """Classe chamada num sistema windows"""

    def __call__(self):
        import msvcrt  # importa o similar ao getch para windows
        return msvcrt.getch()  # retorna o getch


getchar = _Getch()  # daqui pra frente, quando chamar 'getchar' o programa faz o processo explicado acima


def clears(): os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela conforme o sistema


def printitle(string, n):
    """
    :param string: o que sera mostrado
    :param n: quantos espaços de delimitação
    :return: sem retorno; mostra na tela a string contornada
    """
    print('-'*n)
    print(string.center(n))
    print('-'*n)


def prinsubtitle(string):
    """
    :param string: o que sera mostrado
    :return: sem retorno; mostra na tela a string contornada conforme seu tamanho
    """
    print('-'*len(string))
    print(string)
    print('-'*len(string))


def menu():
    clears()
    while True:
        printitle('MENU', 126)
        print('\tA - JOGAR')
        print('\tB - INSTRUÇÕES')
        print('\tC - CRÉDITOS')
        o = getchar()
        if o.lower() == b'a':
            print('Jogar aqui')
            break
        elif o.lower() == b'b':
            print('Instruções aqui')
            break
        elif o.lower() == b'c':
            print('Créditos aqui')
            break
        else:
            clears()
            print('Opção Inválida! Digite novamente:\n')


clears()

print('-'*126)
print("""  _____     _______ _    _         ____  ______     _    _ _____ _____ _    _        _____  _____ _    _  ____   ____  _
 |  __ \ /\|__   __| |  | |       / __ \|  ____|   | |  | |_   _/ ____| |  | |      / ____|/ ____| |  | |/ __ \ / __ \| |
 | |__) /  \  | |  | |__| |      | |  | | |__      | |__| | | || |  __| |__| |     | (___ | |    | |__| | |  | | |  | | |
 |  ___/ /\ \ | |  |  __  |      | |  | |  __|     |  __  | | || | |_ |  __  |      \___ \| |    |  __  | |  | | |  | | |
 | |  / ____ \| |  | |  | |      | |__| | |        | |  | |_| || |__| | |  | |      ____) | |____| |  | | |__| | |__| | |____
 |_| /_/    \_\_|  |_|  |_|       \____/|_|        |_|  |_|_____\_____|_|  |_|     |_____/ \_____|_|  |_|\____/ \____/|______|""")
print('-'*126)


print('\n\n')
print("Pressione qualquer tecla para continuar...")
getchar()
menu()
