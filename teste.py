from texto_menu_sobre import TEXTOSOBRE
from cores import colorir
import os
import time
from conteudos import CONTEUDOS
def limparTela():
    os.system('cls')
def mostrarTitulo(texto):
    limparTela()
    print(colorir("-" * 50, cor="magenta"))
    print(colorir(texto.center(50), cor="magenta", estilo="bold"))
    print(colorir("-" * 50, cor="magenta"))
    print()
def mostrarTextoLinhaQuebrada(texto):
        inicio = 0
        fim = 50
        while inicio < len(texto):
            print(texto[inicio:fim])
            inicio += 50
            fim += 50
def mostrarOpcoesIdades():
        print(colorir("Selecione a faixa etária:", cor="blue", estilo="bold"))
        print(colorir("1. 5-6 anos", cor="green"))
        print(colorir("2. 7-8 anos", cor="yellow"))
        print(colorir("3. 9-10 anos", cor="cyan"))
        print()
        print(colorir("0. Voltar", cor="red"))
        print()
def menuPrincipal():
    OPCOESMENUPRINCIPAL = "1230"
    mostrarTitulo("SISTEMA DE APRENDIZADO INFANTIL")
    print(colorir("1. Matemática", cor="blue"))
    print(colorir("2. Informática", cor="green"))
    print()
    print(colorir("3. Sobre o Sistema", cor="yellow"))
    print(colorir("0. Sair", cor="red"))
    print()
    opcao = input(colorir("Escolha uma opção (0-3): ", cor="cyan"))
    if opcao not in OPCOESMENUPRINCIPAL:
        print(colorir("Opção inválida! Tente novamente.", cor="red"))
        time.sleep(1)
    return opcao
def menuMatematica():
    OPCOESMENUMATEMATICA = "0123"
    while True:
        mostrarTitulo("MATEMÁTICA DIVERTIDA")
        mostrarOpcoesIdades()

        opcao = input(colorir("Escolha uma opção (0-3): ", cor="cyan"))
        if opcao not in OPCOESMENUMATEMATICA:
            print(colorir("Opção inválida! Tente novamente.", cor="red"))
            time.sleep(1)
        elif opcao == "1":
            menuConteudosExercicios("matematica", "5-6")
        elif opcao == "2":
            menuConteudosExercicios("matematica", "7-8")
        elif opcao == "3":
            menuConteudosExercicios("matematica", "9-10")
        elif opcao == "0":
            main()
def menuInformatica():
    OPCOESMENUINFORMATICA = '0123'
    while True:
        mostrarTitulo("INFORMÁTICA DIVERTIDA")
        mostrarOpcoesIdades()

        opcao = input(colorir("Escolha uma opção (0-3): ", cor="cyan"))
        if opcao not in OPCOESMENUINFORMATICA:
            print(colorir("Opção inválida! Tente novamente.", cor="red"))
            time.sleep(1)
        if opcao == "1":
            menuConteudosExercicios("informatica", "5-6")
        elif opcao == "2":
            menuConteudosExercicios("informatica", "7-8")
        elif opcao == "3":
            menuConteudosExercicios("informatica", "9-10")
        elif opcao == "0":
            main()
def sobreSistema():     
    def menuSobreSistema(pagina):
        MENUSOBRESISTEMAOPCOES = "10"
        amostra_pagina = pagina + 1
        print()
        print(colorir(f"\t\tPágina {amostra_pagina}", cor="black", fundo="bg_white"))
        print(colorir(colorir("Enter. Próxima", cor="green")))
        if amostra_pagina > 1:
            print(colorir("1. Anterior", cor="yellow"))
        print(colorir("0. Voltar", cor="red"))

        opcao = input(colorir(">", cor="blue"))
        if amostra_pagina == 1 and opcao not in MENUSOBRESISTEMAOPCOES[1]:
            print(colorir("Opção inválida! Tente novamente.", cor="red"))
            time.sleep(1)
            paginas(pagina)
        if opcao not in MENUSOBRESISTEMAOPCOES:
            print(colorir("Opção inválida! Tente novamente.", cor="red"))
            time.sleep(1)
            paginas(pagina)
        return opcao
    lista_paragrafos = list(TEXTOSOBRE)
    n_pagina = 0
    ultima_pagina = len(lista_paragrafos)
    while True:
        def paginas(pagina):
            while pagina < ultima_pagina:
                mostrarTitulo("Sobre o Sistema")
                if pagina in [n for n in range(0, ultima_pagina)]:
                    mostrarTextoLinhaQuebrada(lista_paragrafos[pagina])
                prox_anterior = menuSobreSistema(pagina)
                if prox_anterior == '1' and pagina > 0:
                    pagina -= 1
                    paginas(pagina)
                elif prox_anterior == "0":
                    main()
                    return
                else:
                    pagina += 1
        paginas(n_pagina)
def menuConteudosExercicios(tema, idade):
   while True:
        mostrarTitulo(f"{tema.upper()} PARA {idade} ANOS")
        print(colorir("1. Ver Conteúdos", cor="green"))
        print(colorir("2. Praticar Exercícios", cor="yellow"))
        print(colorir("0. Voltar", cor="red"))
        
        opcao = input(colorir("Escolha uma opção (0-2): ", cor="cyan"))
        
        if opcao == "1":
            verConteudos(tema, idade)
        elif opcao == "2":
            praticarExercicio(tema, idade) 
        elif opcao == "0":
            break
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)
def conteudoCompleto(tema, idade, conteudo):
    dadosConteudo = CONTEUDOS[tema][idade][conteudo]
    limparTela()
    mostrarTitulo(f"{conteudo.upper()}")
    print(dadosConteudo["texto"])
    print()
    input(colorir("Pressione Enter para voltar", cor="yellow"))
def verConteudos(tema, idade):
    while True:
        mostrarTitulo(f"CONTEÚDOS DE {tema.upper()} PARA {idade} ANOS")
        conteudos = list(CONTEUDOS[tema][idade].items())
        
        for i, (nome, dados) in enumerate(conteudos, 1):
            print(colorir(f'{i}. {nome}', cor="cyan"))
        print()
        print(colorir("0. Voltar", "red"))
        print()
        opcao = input(colorir("Escolha um conteúdo: ", cor="yellow"))
        
        if opcao == "0":
            break
        if opcao.isdigit():  
            indice = int(opcao) - 1
            if 0 <= indice <= len(conteudos):
                nomeConteudo = conteudos[indice][0]
                conteudoCompleto(tema, idade, nomeConteudo)
            else:
                print(colorir("Número inválido! Escolha uma opção da lista.", cor="red"))
                time.sleep(1)
        else:
            print(colorir("Por favor, digite apenas números.", cor="red"))
            time.sleep(1)
def praticarExercicio(tema, idade):
    while True:
        mostrarTitulo(f"EXERCÍCIOS DE {tema.upper()}")
        
        conteudosComexercício = list(CONTEUDOS[tema][idade].items())  

        for k, (nome, _) in enumerate(conteudosComexercício, 1):
            print(colorir(f"{k}. {nome}", cor="cyan"))
        print()
        print(colorir("0. Voltar", cor="red"))
        print()
        opcao = input(colorir("Escolha um conteúdo para praticar: ", cor="yellow"))
        
        if opcao == "0":
            break
        elif opcao.isdigit(): 
            indice = int(opcao) - 1
            if indice >= 0 and indice < len(conteudosComexercício):
                nomeConteudo = conteudosComexercício[indice][0]
                mostrarExercicios(tema, idade, nomeConteudo)
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)
def mostrarExercicios(tema, idade, conteudos):
    limparTela()
    
    exercício = CONTEUDOS[tema][idade][conteudos]["exercício"]
    
    mostrarTitulo(f"EXERCÍCIOS: {conteudos.upper()}")
    
    quantidade_acertos = 0
    quantidade_erros = 0
    
    for i, exercicio in enumerate(exercício, 1):
        print()
        print(colorir(f"Exercício {i}: {exercicio['pergunta']}", cor="yellow"))
        resposta = input(colorir("Sua resposta: ", cor="cyan"))
        
        if resposta == exercicio["resposta"]:
            print(colorir("Correto!", cor="green"))
            quantidade_acertos += 1 
        else:
            quantidade_erros += 1
            print(colorir(f"Errado. Resposta: {exercicio['resposta']}", cor="red"))
        
        time.sleep(1)

    time.sleep(0.8)
    limparTela()
    if quantidade_acertos > 0:
        if quantidade_erros == 0:
            print(colorir("Parabéns! Você acertou todas as repostas.", fundo="bg_green"))
        print(colorir(f"Repostas corretas: {quantidade_acertos}", cor="green"))
    if quantidade_erros > 0:
        if quantidade_acertos == 0:
            print(colorir("Estude mais, amigo.", cor="red", fundo="bg_red"))
        print(colorir(f"Respostas incorretas: {quantidade_erros}", cor="red"))

    print()
    input(colorir("Pressione Enter para voltar...", cor="yellow"))
def main():
    while True:
        opcao = menuPrincipal()
        if opcao == "1":
            menuMatematica()
        elif opcao == "2":
            menuInformatica()
        elif opcao == "3":
            sobreSistema()
main()