import getch
import os

def clears():os.system('cls' if os.name=='nt' else 'clear')

def printitle(str, n):
    print('-'*n)
    print(str.center(n))
    print('-'*n)

def prinsubtitle(str):
    print('-'*len(str))
    print(str)
    print('-'*len(str))

clears()

print('-'*126)
print("""  _____     _______ _    _         ____  ______     _    _ _____ _____ _    _        _____  _____ _    _  ____   ____  _
 |  __ \ /\|__   __| |  | |       / __ \|  ____|   | |  | |_   _/ ____| |  | |      / ____|/ ____| |  | |/ __ \ / __ \| |
 | |__) /  \  | |  | |__| |      | |  | | |__      | |__| | | || |  __| |__| |     | (___ | |    | |__| | |  | | |  | | |
 |  ___/ /\ \ | |  |  __  |      | |  | |  __|     |  __  | | || | |_ |  __  |      \___ \| |    |  __  | |  | | |  | | |
 | |  / ____ \| |  | |  | |      | |__| | |        | |  | |_| || |__| | |  | |      ____) | |____| |  | | |__| | |__| | |____
 |_| /_/    \_\_|  |_|  |_|       \____/|_|        |_|  |_|_____\_____|_|  |_|     |_____/ \_____|_|  |_|\____/ \____/|______|""")
print('-'*126)

printitle("Instruções", 126)
print("- O jogo é baseado em suas escolhas: preste atenção")
print("- A cada escolha que você terá que fazer ser-lhe-ão mostradas as opções. Você deve digitar a letra correspondente a sua escolha")
print("- O menu funciona da mesma forma: digite a letra correspondente a sua escolha")
print("\nPressione qualquer tecla para continuar...")

getch.getch()
print("Yay")
