import random
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

#a biblioteca random serve para gerar números aleatórios para as matrizes

#as bibliotecas time, environ e pygame servem apenas para gerar contexto do jogo, trazendo um aidiconal do que foi pedido no problema.
#Ambas não interferem no jogo em si e em nenhuma otimização.

#função que encontra o menor valor da lista diferente de 0, será utilizada para gerar novos valores mínimos na tabela
def menor(lista):
    menor=99999
    for i in range(len(lista)):
        if lista[i] < menor:
            if lista[i] == 0:
                continue
            else:
                menor = lista[i]
    return menor

#função que define contexto do jogo
def contexto():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()
    print('Após ressuscitar, redescobrindo a simulação do mundo real em que vive, Neo começa a buscar seus companheiros...')
    time.sleep(5)
    print('Durante sua jornada, ele se depara com seu inimigo Smith, que o prende em um labirinto de enigmas...')
    time.sleep(5)
    print('Neo, no limite do seu dom, consegue resolver quase todos os desafios, restando apenas um...')
    time.sleep(5)
    print('A RESOLUÇÃO DA TABELA DAS SOMAS ESQUECIDAS.')
    time.sleep(5)
    print('Neo chamou um colega para ajudá-lo nessa batalha, mas não contava com a astúcia de Smith, que também chamou um.')
    time.sleep(5)
    print('Dois jogadores (Player 1 e Player 2) precisarão representar essa batalha. Se apresentem e bem-vindos ao...')
    pygame.mixer.music.fadeout (6000)
    time.sleep(6)

#função que gera matriz nula
def tabela_nula(linhas_colunas):
    tabela_nula=[[0 for j in range(linhas_colunas)] for i in range(linhas_colunas)]
    return tabela_nula

#função que gera matriz com números aleatórios
def tabela(modo):
    tabela=[]
    tabela_verificacao=[]
    if modo == '1':
        linha = random.sample(range(1, 31), 9)
        tabela.append(linha[:3])
        tabela.append(linha[3:-3])
        tabela.append(linha[-3:])
        tabela_verificacao.append(linha[:3])
        tabela_verificacao.append(linha[3:-3])
        tabela_verificacao.append(linha[-3:])
        #adiciona a linha e coluna da somatória
        lista_nula=[0 for i in range(3)]
        tabela.append(lista_nula)
        for item in tabela:
            item.append(0)
        #soma cada linha e coloca no último elemento
        for item in tabela:
            item[3]=sum(item)
        #soma cada coluna e coloca no último elemento
        contador=0
        for i in range(4):
            soma_coluna=0
            for j in range(len(tabela)):
                soma_coluna+=tabela[j][contador]
            tabela[3][contador]=soma_coluna
            contador+=1
        tabela[3][3]=0
        return tabela, tabela_verificacao

    elif modo == '2':
        linha = random.sample(range(1, 61), 16)
        tabela.append(linha[:4])
        tabela.append(linha[4:-8])
        tabela.append(linha[-8:-4])
        tabela.append(linha[-4:])
        tabela_verificacao.append(linha[:4])
        tabela_verificacao.append(linha[4:-8])
        tabela_verificacao.append(linha[-8:-4])
        tabela_verificacao.append(linha[-4:])

        #adiciona a linha e coluna da somatória
        lista_nula=[0 for i in range(4)]
        tabela.append(lista_nula)
        for item in tabela:
            item.append(0)
        #soma cada linha e coloca no último elemento
        for item in tabela:
            item[4]=sum(item)
        #soma cada coluna e coloca no último elemento
        contador=0
        for i in range(5):
            soma_coluna=0
            for j in range(len(tabela)):
                soma_coluna+=tabela[j][contador]
            tabela[4][contador]=soma_coluna
            contador+=1
        tabela[4][4]=0
        return tabela, tabela_verificacao

    else:
        linha = random.sample(range(1, 101), 25)
        tabela.append(linha[:5])
        tabela.append(linha[5:-15])
        tabela.append(linha[-15:-10])
        tabela.append(linha[-10:-5])
        tabela.append(linha[-5:])
        tabela_verificacao.append(linha[:5])
        tabela_verificacao.append(linha[5:-15])
        tabela_verificacao.append(linha[-15:-10])
        tabela_verificacao.append(linha[-10:-5])
        tabela_verificacao.append(linha[-5:])
        #adiciona a linha e coluna da somatória
        lista_nula=[0 for i in range(5)]
        tabela.append(lista_nula)
        for item in tabela:
            item.append(0)
        #soma cada linha e coloca no último elemento
        for item in tabela:
            item[5]=sum(item)
        #soma cada coluna e coloca no último elemento
        contador=0
        for i in range(6):
            soma_coluna=0
            for j in range(len(tabela)):
                soma_coluna+=tabela[j][contador]
            tabela[5][contador]=soma_coluna
            contador+=1
        tabela[5][5]=0
        return tabela, tabela_verificacao

#função que imprime uma matriz por vez
def impressao_matriz(matriz):
    for listas in matriz:
        print(listas)
    
#função que imprime duas matrizes juntas
def impressao_matriz_dupla(matriz, matriz2, linhas_colunas):
    for i in range(linhas_colunas):
        print(matriz[i], end='')
        print(f'\t\t\t{matriz2[i]}')

#função que verifica se o palpite é igual a soma e faz a revelação da matriz nula
def verificacao_palpite(palpite, soma, escolha, tabela, tabela_nula, escolha_linha_ou_coluna, linhas_colunas, casas, pontuador):
    pontuacao=0
    if palpite == soma:
        #iteração para garantir que o intervalo já não foi revelado ou escolhido
        for item in tabela_nula[escolha_linha_ou_coluna-1]:
            if item == 0:
                pontuacao+=1
        if pontuacao == 0:
            print('-'*75)
            print(f'\nEsse intervalo já foi revelado, {pontuador}. Não foi dessa vez :(')
        else:
            print('-'*75)
            print(f'\nAff, {pontuador} você é muito bom! Acertou a soma do intervalo!\nPor isso, será revelado TODAS as casas da sequência escolhida!')
            casas-=linhas_colunas
            if escolha == '1':
                tabela_nula[escolha_linha_ou_coluna-1] = tabela[escolha_linha_ou_coluna-1]
            else:
                for i in range(linhas_colunas):
                    tabela_nula[i][escolha_linha_ou_coluna-1]=tabela[i][escolha_linha_ou_coluna-1]
        return tabela_nula, casas, pontuacao, tabela

    elif palpite > soma:
        if escolha == '1':
            if sum(tabela[escolha_linha_ou_coluna-1]) == 0:
                print('-'*75)
                print(f'\nTodos os elementos desse intervalo já foram pontuados, {pontuador}. Tente outro intervalo.')
                return tabela_nula, casas, pontuacao, tabela
            valor=max(tabela[escolha_linha_ou_coluna-1])
            pos=tabela[escolha_linha_ou_coluna-1].index(valor)
            print('-'*75)
            print(f'\nSeu palpite foi maior que a soma, {pontuador}, será revelada a casa que contém o maior valor.')
            casas-=1
            pontuacao=1
            #colocando o valor máximo da linha na tabela nula
            tabela_nula[escolha_linha_ou_coluna-1][pos] = valor
            #transformando o valor max da linha em 0 para que seja desconsiderado no novo max/min
            tabela[escolha_linha_ou_coluna-1][pos] = 0

        else:
            lista_coluna_maior=[]
            for linha in tabela:
                lista_coluna_maior.append(linha[escolha_linha_ou_coluna-1])
            if sum(lista_coluna_maior) == 0:
                print('-'*75)
                print(f'\nTodos os elementos desse intervalo já foram pontuados, {pontuador}. Tente outro intervalo.')
                return tabela_nula, casas, pontuacao, tabela
            valor=max(lista_coluna_maior)
            pos=lista_coluna_maior.index(valor)
            print('-'*75)
            print(f'\nSeu palpite foi maior que a soma, {pontuador}, será revelada a casa que contém o maior valor.')
            casas-=1
            pontuacao=1
            #colocando o valor máximo da coluna na tabela nula
            tabela_nula[pos][escolha_linha_ou_coluna-1]=valor
            #transformando o valor max da coluna em 0 para que seja desconsiderado no novo max/min
            tabela[pos][escolha_linha_ou_coluna-1] = 0
        return tabela_nula, casas, pontuacao, tabela

    elif palpite < soma:
        if escolha == '1':
            #verifica se todas as casas foram reveladas
            if sum(tabela[escolha_linha_ou_coluna-1]) == 0:
                print('-'*75)
                print(f'\nTodos os elementos desse intervalo já foram pontuados, {pontuador}. Tente outro intervalo.')
                return tabela_nula, casas, pontuacao, tabela
            valor=menor(tabela[escolha_linha_ou_coluna-1])
            pos=tabela[escolha_linha_ou_coluna-1].index(valor)
            print('-'*75)
            print(f'\nSeu palpite foi menor que a soma, {pontuador}, será revelada a casa que contém o menor valor.')
            casas-=1
            pontuacao=1
            #colocando o valor mínimo da linha na tabela nula
            tabela_nula[escolha_linha_ou_coluna-1][pos]=valor
            #transformando o valor min da linha em 0 para que seja desconsiderado no novo max/min
            tabela[escolha_linha_ou_coluna-1][pos]=0
        else:
            lista_coluna_menor=[]
            for linha in tabela:
                lista_coluna_menor.append(linha[escolha_linha_ou_coluna-1])
            if sum(lista_coluna_menor) == 0:
                print('-'*75)
                print(f'\nTodos os elementos desse intervalo já foram pontuados, {pontuador}. Tente outro intervalo.')
                return tabela_nula, casas, pontuacao, tabela
            valor=menor(lista_coluna_menor)
            pos=lista_coluna_menor.index(valor)
            print('-'*75)
            print(f'\nSeu palpite foi menor que a soma, {pontuador}, será revelada a casa que contém o menor valor.')
            casas-=1
            pontuacao=1
            #colocando o valor mínimo da coluna na tabela nula
            tabela_nula[pos][escolha_linha_ou_coluna-1]=valor
            #transformando o valor min da linha em 0 para que seja desconsiderado no novo max/min
            tabela[pos][escolha_linha_ou_coluna-1]=0
        return tabela_nula, casas, pontuacao, tabela

#função que registra a escolha de linha/coluna, o intervalo e o palpite da soma
def escolha(linhas_colunas, nome):
    escolha = input(f'''\n{nome}, escolha entre linha e coluna:
[1] Linha
[2] Coluna 
>>> ''')
    while (escolha != '1' and escolha != '2') or escolha.isdigit == False:
        escolha=input('Fique atento! Ou linha [1] ou coluna [2]:\n>>> ')
    if escolha == '1':
        escolha_linha = input(f'\nQual linha você quer, {nome}?\nEscolha de [1] até [{linhas_colunas}].\n>>> ')
        while (escolha_linha.isdigit == False) or (int(escolha_linha) > linhas_colunas) or (int(escolha_linha) < 0):
            escolha_linha = input(f'Espertinho(a), eu preciso de um valor de [1] até [{linhas_colunas}]. Tente novamente:\n>>> ')
        escolha_linha=int(escolha_linha)

        palpite = input(f'\nQual o valor que você acha que é a soma desse intervalo escolhido, {nome}?\n>>> ')
        while palpite.isdigit == False:
            palpite = input(f'Parece que você digitou um valor errado. Tenta de novo!\n>>> ')
        palpite=int(palpite)
        return escolha, escolha_linha, palpite

    else:
        escolha_coluna = input(f'\nQual coluna você quer?\nEscolha de [1] até [{linhas_colunas}].\n>>> ')
        while (escolha_coluna.isdigit == False) or (int(escolha_coluna) > linhas_colunas) or (int(escolha_coluna) < 0):
            escolha_coluna = input(f'Espertinho(a), eu preciso de um valor de [1] até [{linhas_colunas}]. Tente novamente:\n>>> ')
        escolha_coluna=int(escolha_coluna)

        palpite = input(f'\nQual o valor que você acha que é a soma desse intervalo escolhido, {nome}?\n>>> ')
        while palpite.isdigit == False:
            palpite = input('Parece que você digitou um caractere inválido. Tenta de novo!\n>>> ')
        palpite=int(palpite)
        return escolha, escolha_coluna, palpite

#funcao que imprime o historico de paplpites, escolhas e acertos
def impressao_historico(historico1, historico2, nome1, nome2, jogadas):
    print(f'\n\t\t\033[0;33;44mHISTÓRICO {nome1}\033[0m\t\t\t\t\t\t\t\t\033[0;33;44mHISTÓRICO {nome2}\033[0m')
    for j in range(jogadas):
        if len(historico1) > j:
            print(f'Linha ou coluna: {historico1[j][0]}; Intervalo: {historico1[j][1]}; Palpite: {historico1[j][2]}; Verificação: {historico1[j][3]};', end="")
        if len(historico2) > j:
            print(f'\t\tLinha ou coluna: {historico2[j][0]}; Intervalo: {historico2[j][1]}; Palpite: {historico2[j][2]}; Verificação: {historico2[j][3]}')