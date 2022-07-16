'''
MIT License

Copyright (c) 2022 Juan Carlos Bindez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


'''
Author: www.github.com/JuanBindez
Description: command awk
Python Version: 3.10
year: 2022
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
        print(Color.MAGENTA +
            '''
                           _              ____        _   _                 
             __ ___      _| | __    _    |  _ \ _   _| |_| |__   ___  _ __  
            / _` \ \ /\ / / |/ /  _| |_  | |_) | | | | __| '_ \ / _ \| '_ \ 
           | (_| |\ V  V /|   <  |_   _| |  __/| |_| | |_| | | | (_) | | | |
            \__,_| \_/\_/ |_|\_\   |_|   |_|    \__, |\__|_| |_|\___/|_| |_| v 0.2
                                                |___/                       
                    

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


        escolha = int(input(">"))

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
'''
MIT License

Copyright (c) 2022 Juan Carlos Bindez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


'''
Author: www.github.com/JuanBindez
Description: command awk
Python Version: 3.10
year: 2022
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
        print(Color.MAGENTA +
            '''
                           _              ____        _   _                 
             __ ___      _| | __    _    |  _ \ _   _| |_| |__   ___  _ __  
            / _` \ \ /\ / / |/ /  _| |_  | |_) | | | | __| '_ \ / _ \| '_ \ 
           | (_| |\ V  V /|   <  |_   _| |  __/| |_| | |_| | | | (_) | | | |
            \__,_| \_/\_/ |_|\_\   |_|   |_|    \__, |\__|_| |_|\___/|_| |_| v 0.2
                                                |___/                       
                    

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


        escolha = int(input(">"))

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

except KeyboardInterrupt:
    print("Você Encerrou o Programa !")
