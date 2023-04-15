'''/*******************************************************************************
Autor: Douglas Oliveira de Jesus
Componente Curricular: EXA854 - MI - ALGORITMOS - TP01
Concluido em: 22/05/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''

'''Descrição do problema: 
Criação de um jogo para 2 pessoas, com 1 ou 2 tabuleiros. Cada jogador deve informar um palpite de soma
do intervalo de linhas ou colunas escolhidas, a fim de acertar a soma da matriz que será gerada com esses valores.
Só será mostrada para os jogadores uma tabela nula que terá seus elementos trocados de acordo com os acertos.
Caso a menor diferença seja menor que a soma do intervalo, será revelada a casa de menor valor; caso seja maior, 
será revelado a de maior valor e se a diferença for 0, ou seja, caso o palpite seja equivalente a soma, todas as
casas do intervalo serão reveladas. Ganha o jogo quem terminar com mais pontos, seja completando o tabuleiro, ou chegando
na quantidade de partidas descrita incialmente no método de término do jogo.
'''

import jogo_funcoes
import time

#declarações de variáveis

pontuacao=pontuacao1=pontuacao2=0
jogadas=0
escolha_linha=escolha_coluna=0
somal0=somal1=somal2=somal3=somal4=somac0=somac1=somac2=somac3=somac4=0
rodadas=9999
historico=[]
historico1=[]
historico2=[]

#contexto do jogo, com áudio e texto

jogo_funcoes.contexto()

#início, registro de jogadores e modo de iniciar e finalizar o jogo

#o código que começa com \033[ só muda a cor do trecho selecionado
print('''
\t\t\033[0;33;41m*****************************************\033[0m
\t\t\t\033[1;33;41mJOGO DAS SOMAS ESQUECIDAS\033[0m
\t\t\033[0;33;41m*****************************************\033[0m
''')

#identificação

nome1=input('\033[0;33;44mInforme o nome do jogador 1: \033[0m ').replace(' ', '')
while nome1.isalpha() == False:
    nome1=input('Coloque um nome válido: ').replace(' ', '')
nome2=input('\033[0;33;44mInforme o nome do jogador 2: \033[0m ').replace(' ', '')
while nome2.isalpha() == False:
    nome2=input('Coloque um nome válido: ').replace(' ', '')

#quantidade de tabuleiros

tabuleiros = input('''\nInforme a quantidade de tabuleiros:
[1] 1 tabuleiro;
[2] 2 tabuleiros;
>>> ''')
while (tabuleiros != '1' and tabuleiros != '2') or tabuleiros.isdigit == False:
    tabuleiros=input('Quantidade inválida :(\nSó poderá jogar com [1] tabuleiro ou com [2] tabuleiros.\nInforme novamente, por favor!\n>>> ')

#modalidade do jogo

modo = input('''\nQual modo você quer jogar? 
[1] FÁCIL (3X3);
[2] MÉDIO (4X4);
[3] DIFÍCIL (5X5).
>>> ''')
while (modo != '1' and modo != '2' and modo != '3') or modo.isdigit == False:
    modo=input('Modo inválido :(\nTente novamente algum dos disponíveis:\n[1] FÁCIL (3X3);\n[2] MÉDIO (4X4)\n[3] DIFÍCIL (5X5)\n>>> ')

#registrando a quantidade de linhasxcolunas e das casas que terá cada tabuleiro

if modo == '1':
    linhas_colunas=3
    casas=9
elif modo == '2':
    linhas_colunas=4
    casas=16
else:
    linhas_colunas=5
    casas=25

casas1=casas
casas2=casas

#como o jogo será finalizado

termino = input(f'''\nComo esta partida deve terminar?
[1] Por número de rodadas;
[2] Quando um dos tabuleiros for completamente revelado.
>>> ''')
while (termino != '1' and termino != '2') or termino.isdigit == False:
    termino=input(f'Não tem como terminar dessa maneira :(\nSomente por número de rodadas [1] ou quando um tabuleiro for revelado [2]\n>>> ')
if termino == '1':
  rodadas = int(input(f'\nCerto! Você agora deve definir quantas rodadas haverá:\n>>> '))
  while rodadas % 2 == 0 or rodadas <= 0:
      rodadas = int(input(f'O número precisa ser ímpar positivo.\n>>> '))

################# TABULEIRO 1

if tabuleiros == '1':

    #criação e impressão da tabela
    #a matriz tabela possui as somas no lado direito e abaixo de cada linha/coluna
    #a tabela_verificação possui uma tabela de acordo com a quantidade de linhas colunas, ela que troca de valor com a tabela_nula
    #tabela_nula é a tabela impressa, incialmente todos os elementos são 0, mudando de acordo com as revelações
    tabela, tabela_verificacao = jogo_funcoes.tabela(modo)
    tabela_nula = jogo_funcoes.tabela_nula(linhas_colunas)
    print()
    jogo_funcoes.impressao_matriz(tabela_nula)

    #inicio do jogo

    print("\n\t\033[0;33;44mLET'S SUM! <3\033[0m")

    while rodadas != 0 or casas != 0:
        rodadas-=1
        jogadas+=1
        #escolha de linhas/colunas, seus intervalos e o palpite do player 1
        escolha_p1, escolha_linha_coluna_p1, palpite_p1 = jogo_funcoes.escolha(linhas_colunas, nome1)
        escolha_linha_coluna_p1=int(escolha_linha_coluna_p1)

        #escolha de linhas/colunas, seus intervalos e o palpite do player 2
        escolha_p2, escolha_linha_coluna_p2, palpite_p2 = jogo_funcoes.escolha(linhas_colunas, nome2)
        escolha_linha_coluna_p2=int(escolha_linha_coluna_p2)
        
        #calculando a diferença para ver quem chegou mais próximo e registrando os dados para o histórico de jogadas
        if escolha_p1 == '1':
            diferenca_p1 = palpite_p1 - tabela[escolha_linha_coluna_p1-1][linhas_colunas]
            if diferenca_p1 > 0:
                verificacao, linha_ou_coluna='maior', 'linha'
            if diferenca_p1 < 0:
                diferenca_p1 = diferenca_p1*(-1)
                verificacao, linha_ou_coluna='menor', 'linha'
            else:
                verificacao, linha_ou_coluna='equivalente', 'linha'
        else:
            diferenca_p1 = palpite_p1 - tabela[linhas_colunas][escolha_linha_coluna_p1-1]
            if diferenca_p1 > 0:
                verificacao, linha_ou_coluna='maior', 'coluna'
            if diferenca_p1 < 0:
                diferenca_p1 = diferenca_p1*(-1)
                verificacao, linha_ou_coluna='menor', 'coluna'
            else:
                verificacao, linha_ou_coluna='equivalente', 'coluna'
            
        historico=[linha_ou_coluna, escolha_linha_coluna_p1, palpite_p1, verificacao]
        historico1.append(historico)

        if escolha_p2 == '1':
            diferenca_p2 = palpite_p2 - tabela[escolha_linha_coluna_p2-1][linhas_colunas]
            if diferenca_p2 > 0:
                verificacao, linha_ou_coluna='maior', 'linha'
            if diferenca_p2 < 0:
                diferenca_p2 = diferenca_p2*(-1)
                verificacao, linha_ou_coluna='menor', 'linha'
            else:
                verificacao, linha_ou_coluna='equivalente', 'linha'
        else:
            diferenca_p2 = palpite_p2 - tabela[linhas_colunas][escolha_linha_coluna_p2]
            if diferenca_p2 > 0:
                verificacao, linha_ou_coluna='maior', 'coluna'
            if diferenca_p2 < 0:
                diferenca_p2 = diferenca_p2*(-1)
                verificacao, linha_ou_coluna='menor', 'coluna'
            else:
                verificacao, linha_ou_coluna='equivalente', 'coluna'
        
        historico=[linha_ou_coluna, escolha_linha_coluna_p2, palpite_p2, verificacao]
        historico2.append(historico)

        #verificando quem pontua de acordo com a diferença
        if diferenca_p1 > diferenca_p2:
            #p2 pontua
            palpite=palpite_p2
            escolha=escolha_p2
            pontuador=nome2
            escolha_linha_coluna=escolha_linha_coluna_p2
            if escolha == '1':
                soma = tabela[escolha_linha_coluna_p2-1][linhas_colunas]
            else:
                soma = tabela[linhas_colunas][escolha_linha_coluna_p2-1]
        elif diferenca_p2 > diferenca_p1:
            #p1 pontua
            palpite=palpite_p1
            escolha=escolha_p1
            pontuador=nome1
            escolha_linha_coluna=escolha_linha_coluna_p1
            if escolha == '1':
                soma = tabela[escolha_linha_coluna_p1-1][linhas_colunas]
            else:
                soma = tabela[linhas_colunas][escolha_linha_coluna_p1-1]
        else:
            #os dois pontuam
            palpite=palpite_p1
            escolha=escolha_p1
            pontuador=nome1, nome2
            escolha_linha_coluna=escolha_linha_coluna_p1
            soma=tabela[linhas_colunas][escolha_linha_coluna_p1-1]
            

        #verificando e trocando os dados entre as tabelas
        tabela_nula, casas, pontuacao, tabela_verificacao = jogo_funcoes.verificacao_palpite(palpite, soma, 
            escolha, tabela_verificacao, tabela_nula, escolha_linha_coluna, linhas_colunas, casas, pontuador)
    

        if pontuador == nome1:
            pontuacao1+=pontuacao
        elif pontuador == nome2:
            pontuacao2+=pontuacao
        else:
            pontuacao1+=pontuacao
            pontuacao2+=pontuacao

        #imprimindo o histórico
        jogo_funcoes.impressao_historico(historico1, historico2, nome1, nome2, jogadas)

        print(f"\nA pontuação de {nome1} é {pontuacao1} e a de {nome2} é {pontuacao2}.\n")

        if termino == '1':
            print(f"Faltam {rodadas} rodadas para acabar a partida!")
        
        #reimprimindo a tabela nula com os valores alterados para novos palpites
        jogo_funcoes.impressao_matriz(tabela_nula)
    
    #verifica as pontuacoes e registra o vencedor
    if pontuacao1 > pontuacao2:
        vencedor=nome1
    elif pontuacao < pontuacao2:
        vencedor=nome2
    else:
        print(f'Que raro! Os dois venceram! :oooo')
    print(f'\033[0;33;44mJogo encerrado! Parabéns a {vencedor}!\033[0m')

###############2 TABULEIROS

if tabuleiros == '2':

    #criação e impressão de tabela

    tabela1, tabela_verificacao1=jogo_funcoes.tabela(modo)
    tabela2, tabela_verificacao2=jogo_funcoes.tabela(modo)
    tabela_nula1=jogo_funcoes.tabela_nula(linhas_colunas)
    tabela_nula2=jogo_funcoes.tabela_nula(linhas_colunas)
    print('TABULEIRO 1\t\t\tTABULEIRO 2')
    jogo_funcoes.impressao_matriz_dupla(tabela_nula1, tabela_nula2, linhas_colunas)

    #inicio do jogo

    print("\n\t\033[0;33;44mLET'S SUM! <3\033[0m\n")

    while rodadas != 0 or casas != 0:
        rodadas-=1
        jogadas+=1
        #escolha de linhas/colunas, seus intervalos e o palpite dos dois players (p1 e p2)
        escolha_p1, escolha_linha_coluna_p1, palpite_p1 = jogo_funcoes.escolha(linhas_colunas, nome1)
        escolha_p2, escolha_linha_coluna_p2, palpite_p2 = jogo_funcoes.escolha(linhas_colunas, nome2)
        escolha_linha_coluna_p1=int(escolha_linha_coluna_p1)
        escolha_linha_coluna_p2=int(escolha_linha_coluna_p2)

        #calculando a diferença para ver quem chegou mais próximo e registrando os dados para o histórico de jogadas
        if escolha_p1 == '1':
            diferenca_p1 = palpite_p1 - tabela1[escolha_linha_coluna_p1-1][linhas_colunas]
            if diferenca_p1 > 0:
                verificacao_p1, linha_ou_coluna='maior', 'linha'
            elif diferenca_p1 < 0:
                diferenca_p1 = diferenca_p1*(-1)
                verificacao_p1, linha_ou_coluna='menor', 'linha'
            else:
                verificacao_p1, linha_ou_coluna='equivalente', 'linha'
        else:
            diferenca_p1 = palpite_p1 - tabela1[linhas_colunas][escolha_linha_coluna_p1-1]
            if diferenca_p1 > 0:
                verificacao_p1, linha_ou_coluna='maior', 'coluna'
            elif diferenca_p1 < 0:
                diferenca_p1 = diferenca_p1*(-1)
                verificacao_p1, linha_ou_coluna='menor', 'coluna'
            else:
                verificacao_p1, linha_ou_coluna='equivalente', 'coluna'
            
        historico_p1=[linha_ou_coluna, escolha_linha_coluna_p1, palpite_p1, verificacao_p1]
        historico1.append(historico_p1)

        if escolha_p2 == '1':
            diferenca_p2 = palpite_p2 - tabela2[escolha_linha_coluna_p2-1][linhas_colunas]
            if diferenca_p2 > 0:
                verificacao_p2, linha_ou_coluna='maior', 'linha'
            elif diferenca_p2 < 0:
                diferenca_p2 = diferenca_p2*(-1)
                verificacao_p2, linha_ou_coluna='menor', 'linha'
            else:
                verificacao_p2, linha_ou_coluna='equivalente', 'linha'
        else:
            diferenca_p2 = palpite_p2 - tabela2[linhas_colunas][escolha_linha_coluna_p2-1]
            if diferenca_p2 > 0:
                verificacao_p2, linha_ou_coluna='maior', 'coluna'
            elif diferenca_p2 < 0:
                diferenca_p2 = diferenca_p2*(-1)
                verificacao_p2, linha_ou_coluna='menor', 'coluna'
            else:
                verificacao_p2, linha_ou_coluna='equivalente', 'coluna'
        
        historico_p2=[linha_ou_coluna, escolha_linha_coluna_p2, palpite_p2, verificacao_p2]
        historico2.append(historico_p2)


        if diferenca_p1 > diferenca_p2:
            #p2 pontua
            pontuador=nome2
            if escolha_p2 == '1':
                soma_p2 = tabela2[escolha_linha_coluna_p2-1][linhas_colunas]
            else:
                soma_p2 = tabela2[linhas_colunas][escolha_linha_coluna_p2-1]
            print(f'\n{nome2} chegou mais próximo da soma. :)')
            tabela_nula2, casas2, pontuacao, tabela_verificacao2 = jogo_funcoes.verificacao_palpite(palpite_p2, soma_p2, 
            escolha_p2, tabela_verificacao2, tabela_nula2, escolha_linha_coluna_p2, linhas_colunas, casas2, nome2)
 
        elif diferenca_p2 > diferenca_p1:
            #p1 pontua
            pontuador=nome1
            if escolha_p1 == '1':
                soma_p1 = tabela1[escolha_linha_coluna_p1-1][linhas_colunas]
            else:
                soma_p1 = tabela1[linhas_colunas][escolha_linha_coluna_p1-1]

            print(f'\n{nome1} chegou mais próximo da soma. :)')
            tabela_nula1, casas1, pontuacao, tabela_verificacao1 = jogo_funcoes.verificacao_palpite(palpite_p1, soma_p1, 
            escolha_p1, tabela_verificacao1, tabela_nula1, escolha_linha_coluna_p1, linhas_colunas, casas1, nome1)

        else:
            #os dois pontuam
            pontuador=nome1, nome2
            if escolha_p1 == '1':
                soma_p1 = tabela1[escolha_linha_coluna_p1-1][linhas_colunas]
            else:
                soma_p1 = tabela1[linhas_colunas][escolha_linha_coluna_p1-1]
            
            if escolha_p2 == '1':
                soma_p2 = tabela2[escolha_linha_coluna_p2-1][linhas_colunas]
            else:
                soma_p2 = tabela2[linhas_colunas][escolha_linha_coluna_p2-1]

            print(f'\nAmbos os dois jogadores chegaram mais próximo da soma. :o')

            tabela_nula1, casas1, pontuacao, tabela_verificacao1 = jogo_funcoes.verificacao_palpite(palpite_p1, soma_p1, 
                escolha_p1, tabela_verificacao1, tabela_nula1, escolha_linha_coluna_p1, linhas_colunas, casas1, nome1)
            
            tabela_nula2, casas2, pontuacao, tabela_verificacao2 = jogo_funcoes.verificacao_palpite(palpite_p2, soma_p2, 
                escolha_p2, tabela_verificacao2, tabela_nula2, escolha_linha_coluna_p2, linhas_colunas, casas2, nome2)
        
        if pontuador == nome1:
            pontuacao1+=pontuacao
        elif pontuador == nome2:
            pontuacao2+=pontuacao
        else:
            pontuacao1+=pontuacao
            pontuacao2+=pontuacao

        jogo_funcoes.impressao_historico(historico1, historico2, nome1, nome2, jogadas)

        print(f"\nA pontuação de {nome1} é {pontuacao1} e a de {nome2} é {pontuacao2}.\n")

        if termino == '1':
            print(f"Faltam {rodadas} rodadas para acabar a partida!")

        jogo_funcoes.impressao_matriz_dupla(tabela_nula1, tabela_nula2, linhas_colunas)
        
    #verifica as pontuacoes e registra o vencedor
    if pontuacao1 > pontuacao2:
        vencedor=nome1
    elif pontuacao < pontuacao2:
        vencedor=nome2
    else:
        print(f'Que raro! Os dois venceram! :oooo')
    print(f'\033[0;33;44mJogo encerrado! Parabéns a {vencedor}!\033[0m')

#tempo antes de fechar o programa automaticamente
time.sleep(30)