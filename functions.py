# -*- coding: utf-8 -*-
import os
import sys

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

getchar = _Getch()


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
        if o.lower() == 'a':
            print('Jogar aqui')
            finish()
        elif o.lower() == 'b':
            print('Instruções aqui')
            finish()
        elif o.lower() == 'c':
            print('Créditos aqui')
            finish()
        else:
            clears()
            print('Opção Inválida! Digite novamente:\n')

def finish():
    printitle('Até mais!', 126)
    getchar()
    print('\033[0;0m')
    clears()
    sys.exit()
