# -*- coding: utf-8 -*-
import functions

print('\033[;1m' + '\033[1;42m' + '\033[1;97m')
print()

getchar = functions._Getch()  # daqui pra frente, quando chamar 'getchar' o programa faz o processo explicado acima

functions.clears()

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
functions.menu()
