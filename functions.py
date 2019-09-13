# -*- coding: utf-8 -*-
import os
import sys

class Getch:
    """Similar ao getch do C++. Verifica o sistema e executa o comando"""
    def __init__(self):
        if os.name == 'nt':
            self.impl = GetchWindows()  # atribui getch para windows
        elif os.name == 'posix':
            self.impl = GetchUnix()  # atribui o getch para UNIX
        else:
            print('ERRO! Sistema não suportado')

    def __call__(self): return self.impl()  # chama o getch correspondente


class GetchUnix:
    """Classe chamada quando num sistema UNIX"""

    def __call__(self):
        import getch  # importa o getch
        return getch.getch()  # retorna o metodo getch


class GetchWindows:
    """Classe chamada num sistema windows"""

    def __call__(self):
        import msvcrt  # importa o similar ao getch para windows
        return msvcrt.getch()  # retorna o getch


getchar = Getch()


def clears():
    """
    Função para limpar a tela
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela conforme o sistema


def printitle(string, n):
    """
    :param string: String a ser mostrada
    :param n: Número de espaços de delimitação
    Mostra na tela a string contornada
    """
    print('-'*n)
    print(string.center(n))
    print('-'*n)


def prinsubtitle(string):
    """
    :param string: String a ser mostrada
    Mostra na tela a string contornada conforme seu tamanho
    """
    print('-'*len(string))
    print(string)
    print('-'*len(string))

def choice(options, functions):
    """
    :param options: Opções que o jogador deve escolher
    :param functions: Funções que serão executadas conforme a opção escolhida
    """
    alfa = ['A', 'B', 'C', 'D', 'E']
    index = 0
    while True:
        for c in range(0, (len(options))):
            print('\t{} - {}'.format(alfa[c], options[c]))
        try:
            o = getchar()
        except OverflowError:
            clears()
            print('Opção Inválida! Digite novamente:\n')
            continue

        try:
            o = o.decode('utf-8').lower()
        except AttributeError:
            o = o.lower()
        except UnicodeDecodeError:
            clears()
            print('Opção Inválida! Digite novamente:\n')
            continue

        if o == 'a':
            index = 0
        elif o == 'b':
            index = 1
        elif o == 'c':
            index = 2
        elif o == 'd':
            index = 3
        elif o == 'e':
            index = 4
        else:
            index = 10

        try:
            functions[index]()
        except IndexError:
            clears()
            print('Opção inválida! Digite novamente:\n')
            continue


def menu():
    """
    :return: sem retorno; mostra o menu na tela
    """
    clears()
    choice(['JOGAR', 'INSTRUÇÕES', 'CRÉDITOS', 'SAIR'], [play, finish, credit, finish])

def finish():
    """
    :return: sem retorno; acaba o programa
    """
    clears()
    printitle('Até mais!', 126)
    print('\033[0;0m')
    clears()
    sys.exit()


def credit():
    """
    :return: sem retorno; mostra os créditos
    """""
    clears()
    printitle('CRÉDITOS', 126)
    print('\n')
    print('\tCriadores:')
    print('\n\tArthur Illa\n\tIsaac Younes\n\tGabriel José\n\tGabriel Massi\n\tLucas Linhaus\n\tLucas Loos\n')
    print()
    print('\tOrientadores:')
    print('\n\tFelipe Henriques\n\tMarco Aurélio\n')
    print()
    printitle('CEFET-RJ - 1°Ano Telecomunicações', 126)
    print('\nPressione qualquer tecla para voltar...')
    getchar()
    menu()


def play():
    """
    :return: sem retorno; comeca o jogo
    """
    clears()
    print('\t\o/: Puxa vida! Terminei meu ensino fundamental e pretendo fazer um ensino médio integrado no CEFET... \nQue curso devo escolher?')
