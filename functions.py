# -*- coding: utf-8 -*-
import os
import sys

armas = {'arma':['ForçaBruta'], 'atk':[2]}
CRS = 0
ATQ = armas['atk'][0]
DEF = 10
HP = 30

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

def wait():
    print('Pressione qualquer tecla...')
    try:
        getchar()
        clears()
    except OverflowError:
        clears()


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
    choice(['JOGAR', 'INSTRUÇÕES', 'CRÉDITOS', 'SAIR'], [play, tutorial, credit, finish])

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
    wait()
    menu()


def play():
    """
    :return: sem retorno; comeca o jogo
    """
    clears()
    print('\t')
    print('\t\o/: Puxa vida! Terminei meu ensino fundamental e pretendo fazer um ensino médio integrado no CEFET... \nQue curso devo escolher?')
    choice(['Telecomunicações', 'Tursimo'], [telecom, turismo])


def mostra_atq():
    clears()
    print("\n\tÉ a sua força contra as adversidades do ensino médio. Você o usa para passar pelos desafios e derrotar inimigos\n")
    wait()

def mostra_def():
    clears()
    print("\n\tDegenerador Energético Funcional é o quanto você consegue absorver das 'pancadas' da vida e não se abalar por elas\n")
    wait()

def mostra_hp():
    clears()
    print("\n\tHabilidade Produtiva é a sua saúde, ele define o quanto as adversidades te afetam e se ele chegar a 0 você ficará triste\n")
    wait()

def mostra_crs():
    clears()
    print("\n\tCaRiSma é a sua persuasão, pois os professores não são monstros e se sensibilizam com a situação deplorável do aluno\n")
    wait()

def tutorial():
    """
    :return: sem retorno; mostra as instruções
    """
    clears()
    print("\tOlá! Bem-vindo ao Path of High School")
    wait()
    print("\nEsse é você:  \o/\n")
    print("\tVocê acabou de se formar no ensino fundamental e pretende fazer um ensino médio técnico no CEFET\n")
    print("\tEsses são os seus status:\n	ATQ: {}, DEF: {}, HP: {}, CRS: {}".format(ATQ, DEF, HP, CRS))
    print("\tSobre qual deles você gostaria de saber mais?")
    choice(['ATQ', 'DEF', 'HP', 'CRS', 'Voltar'], [mostra_atq, mostra_def, mostra_hp, mostra_crs, tutorial_continua])

def tutorial_continua():
    print("\n\tEsse é um Desafio(Insira aqui um Dummy)")
    print("\n\tDesafios são as adversidades do dia a dia e precisam ser superados.")
    print("\n\te eles também possuem status")
    wait()
    print("\n			(Insira um dummy aqui)			")
    print("\n ATQ: 1		DEF: 0			HP: 1		")
    print("\n\n\tPara derrotá-los, você precisa de equipamento, quero dizer, conhecimento")
    print("\n\tEsses são seus conhecimentos, ou melhor, os espaços para elas:\n")
    print("\n\tA - 	C -\n\tB - 	D -\n\tE -Força Bruta")
    print("\n\tPor enquanto você só tem a força bruta..\n")
    print("\tAgora vamos começar o jogo...")
    wait()
    play()


def turismo():
    clears()
    print('\tSeu espírito explorador e aventureiro o força a experimentar novas coisas')
    wait()
    print('\tDurante uma delas, assim como D. Sebastião, você some')
    wait()
    print('\tNinguem nunca mais ouviu falar sobre seu paradeiro...')
    wait()
    printitle('Fim de jogo!', 126)
    wait()
    menu()

def telecom():
    clears()
    print('\tUm ser misterioso surge...')
    print('\t°_°')
    wait()
    print('\t°_°: Bela escolha meu caro amigo! Eu sou Tim Berners-Lee, mas pode me chamar de TB')
    wait()
    print('\t°_°: Eu sou o criador da famosa rede WWW e te guiarei por este caminho')
    wait()
    print('\t°_°: Presentear-te-ei com um grande invento meu!')
    wait()
    print('\tVocê ganhou um novo conhecimento!')
    print('\tJogador recebeu HTML!')
    wait()
    armas['arma'].append('HTML')
    armas['atk'].append(1.5)
