'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."
'''


'''
Author: www.github.com/JuanBindez
Description: command awk
Python Version: 3.10
Local: Brazil
OS: Linux
'''


import os
import time


try:

    class Color():
        VERDE = '\033[92m'
        VERDE_CLARO = '\033[1;92m'
        VERMELHO = '\033[91m'
        AMARELO = '\033[93m'
        AZUL = '\033[1;34m'
        MAGENTA = '\033[1;35m'
        NEGRITO = '\033[;1m'
        CYANO = '\033[1;36m'
        CYANO_CLARO = '\033[1;96m'
        CINZA_CLARO = '\033[1;37m'
        CINZA_ESCURO = '\033[1;90m'
        PRETO = '\033[1;30m'
        BRANCO = '\033[1;97m'
        INVERTE = '\033[;7m'
        RESET = '\033[0m'


    def awk_test_a(caminho):
        id = "'{print $1}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_b(caminho):
        id = "'{print $2}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_c(caminho):
        id = "'{print $3}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_d(caminho):
        id = "'{print $4}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_e(caminho):
        id = "'{print $5}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_f(caminho):
        id = "'{print $6}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_g(caminho):
        id = "'{print $7}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_h(caminho):
        id = "'{print $8}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_i(caminho):
        id = "'{print $9}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_j(caminho):
        id = "'{print $10}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_k(caminho):
        id = "'{print $11}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_l(caminho):
        id = "'{print $12}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_m(caminho):
        id = "'{print $13}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_n(caminho):
        id = "'{print $14}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_o(caminho):
        id = "'{print $15}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_p(caminho):
        id = "'{print $16}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_q(caminho):
        id = "'{print $17}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_r(caminho):
        id = "'{print $18}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_s(caminho):
        id = "'{print $19}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_t(caminho):
        id = "'{print $20}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()

        
    def awk_test_u(caminho):
        id = "'{print $1$2$3$4$5$6$7$8$10}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()

        
    def desenho_header():
        print(Color.CYANO +
            '''
                                           ___        ___  __
                            _ __  _   _   / \ \      / / |/ /
                           | '_ \| | | | / _ \ \ /\ / /| ' / 
                           | |_) | |_| |/ ___ \ V  V / | . \ 
                           | .__/ \__, /_/   \_\_/\_/  |_|\_\  V 0.4
                           |_|    |___/                      


                           [Ctrl + C ] Para Encerrar o Programa

            '''
        + Color.RESET)


    def menu_header():
        desenho_header()
        print(Color.BRANCO +
            '''

                                 Digite De 1 a 20
                                [0] Para Ver Tudo
            '''
        + Color.RESET)


        escolha = int(input(">>>"))

        match escolha:
            case 1:
                awk_test_a(nome_arquivo)

            case 2:
                awk_test_b(nome_arquivo)

            case 3:
                awk_test_c(nome_arquivo)

            case 4:
                awk_test_d(nome_arquivo)

            case 5:
                awk_test_e(nome_arquivo)

            case 6:
                awk_test_f(nome_arquivo)

            case 7:
                awk_test_g(nome_arquivo)

            case 8:
                awk_test_h(nome_arquivo)

            case 9:
                awk_test_i(nome_arquivo)

            case 10:
                awk_test_j(nome_arquivo)

            case 11:
                awk_test_k(nome_arquivo)

            case 12:
                awk_test_l(nome_arquivo)

            case 13:
                awk_test_m(nome_arquivo)

            case 14:
                awk_test_n(nome_arquivo)

            case 15:
                awk_test_o(nome_arquivo)

            case 16:
                awk_test_p(nome_arquivo)

            case 17:
                awk_test_q(nome_arquivo)

            case 18:
                awk_test_r(nome_arquivo)

            case 19:
                awk_test_s(nome_arquivo)

            case 20:
                awk_test_t(nome_arquivo)

            case 0:
                awk_test_u(nome_arquivo)

            case _:
                print("Digite Apenas Até 20")


    desenho_header()
    nome_arquivo = str(input('Digite o Nome Do Arquivo ou Caminho\n>'))
    menu_header()


except KeyboardInterrupt:
    print("Você Encerrou o Programa !")
