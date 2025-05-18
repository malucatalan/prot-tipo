
from cores import colorir
import os
import time
import random

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
    while True:
        mostrarTitulo("SISTEMA DE APRENDIZADO INFANTIL")
        print(colorir("1. Matemática", cor="blue"))
        print(colorir("2. Informática", cor="green"))
        print()
        print(colorir("3. Sobre o Sistema", cor="yellow"))
        print(colorir("0. Sair", cor="red"))
        print()

        opcao = input(colorir("Escolha uma opção (0-3): ", cor="cyan"))

        if opcao == "0":
            print(colorir("Até logo! Volte sempre.", cor="red"))
            break
        elif opcao == "1":
            menuMatematica()
        elif opcao == "2":
            menuInformatica()
        elif opcao == "3":
            sobreSistema()
        else:
            print(colorir("Opção inválida! Tente novamente.", cor="red"))
            time.sleep(1)
def menuMatematica():
    while True:
        mostrarTitulo("MATEMÁTICA DIVERTIDA")
        mostrarOpcoesIdades()

        opcao = input(colorir("Escolha uma opção (0-3): ", cor="cyan"))
        if opcao == "1":
            menuConteudosexercício("matematica", "5-6")
        elif opcao == "2":
            menuConteudosexercício("matematica", "7-8")
        elif opcao == "3":
            menuConteudosexercício("matematica", "9-10")
        elif opcao == "0":
            break
def menuInformatica():
    while True:
        mostrarTitulo("INFORMÁTICA DIVERTIDA")
        mostrarOpcoesIdades()

        opcao = input(colorir("Escolha uma opção (0-3): ", cor="cyan"))
        if opcao == "1":
            menuConteudosexercício("informatica", "5-6")
        elif opcao == "2":
            menuConteudosexercício("informatica", "7-8")
        elif opcao == "3":
            menuConteudosexercício("informatica", "9-10")
        elif opcao == "0":
            break
def sobreSistema():
    def voltarPagina(pagina):
        while True:
            mostrarTitulo("Sobre o Sistema")
            if pagina == 2:
                print(mostrarTextoLinhaQuebrada(lista_paragrafos[0]))
                mostrarOpcoesSobreSistema()
            if pagina == 3:
                print(mostrarTextoLinhaQuebrada(lista_paragrafos[1]))
                mostrarOpcoesSobreSistema()

            prox_anterior = input(colorir(">", cor="blue"))
            break
    def mostrarOpcoesSobreSistema():
        print()
        print(f"Pagina {n_pagina}")
        print(colorir(colorir("Qualquer tecla. Próxima", cor="green")))
        if n_pagina > 1:
            print(colorir("1. Anterior", cor="yellow"))
        print(colorir("0. Voltar", cor="red"))

    lista_paragrafos = [
        "Code e Conta é uma plataforma educacional para crianças,"
        " que tem o objetivo de tornar o aprendizado de matemática"
        " e informática mais acessível, divertido e lúdico, estimulando "
        "a criatividade e curiosidade das crianças.",
        "Com o crescente uso e avanço da tecnologia, onde as crianças já nascem em uma era "
        "digital, é de suma importância o domínio de atividades tecnológicas e do pensamento "
        "lógico. As crianças de hoje são nativas digitais, por isso é essencial que elas aprendam "
        "desde cedo a usar a tecnologia de forma consciente, criativa, crítica e responsável.",
        "Desde 2010, a taxa de autismo é estimada em cerca de 1–2 a cada 1.000 pessoas em todo o mundo, sendo mais fácil de identificar em meninos (4–5 vezes mais em meninos do que meninas). Cerca de 1,5% das crianças nos Estados Unidos (uma em cada 68) são diagnosticadas com TEA, a partir de 2014, houve um aumento de 30%, uma a cada 88, em 2012.[28][29][30] Em 2014 e 2016, os números foram de 1 em 68.[31] Em 2018, um aumento de 15%[32] no diagnóstico elevou a prevalência em 1 para 59 crianças.[32][31][33] A taxa de autismo em adultos de 18 anos ou mais no Reino Unido é de 1,1%[34] o número de pessoas diagnosticadas vem aumentando drasticamente desde a década de 1980, em parte devido a mudanças na prática do diagnóstico e incentivos financeiros subsidiados pelo governo para realizar diagnósticos;[30] a questão se as taxas reais têm aumentado realmente, ainda não é conclusiva.[35]"
    ]
    while True:
        mostrarTitulo("Sobre o Sistema")
        
        for paragrafo in lista_paragrafos:
            n_pagina += 1
        
            mostrarTextoLinhaQuebrada(paragrafo)
            mostrarOpcoesSobreSistema()

            prox_anterior = input(colorir(">", cor="blue"))
            if prox_anterior == '1':
                voltarPagina(n_pagina)
                
            elif prox_anterior == "0":
                menuPrincipal()
            n_pagina = 1
            
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
            praticarexercício(tema, idade) 
        elif opcao == "0":
            break
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)

CONTEUDOS = {
    "matematica": {
        "5-6": {
            "Contagem": {
                                "texto": "\n".join(
                    "  ".join(f"{n:>5}" for n in linha) 
                    for linha in zip(
                        range(1, 11),
                        range(11, 21),
                        range(21, 31),
                        range(31, 41),
                        range(41, 51)
                    )
                ),
            
                "exercício": [
                    {
                        "pergunta": "Conte quantos dedos há em uma mão",
                        "resposta": "5"   
                    },
                    {
                        "pergunta":f'🍓🍓🍓🍓🍓🍓🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌\nQuantos morangos e bananas há?' ,
                        "resposta": "16"  
                    },
                    {
                        "pergunta": f'🐶🐶🐱🐱🐭🐭🐼🐼🐷🐷🐯🐯\nQuantos animais há?',
                        "resposta": "12"
                    },
                    {
                        "pergunta": f'⚽🏀⚽⚽⚽🏀🏀⚽⚽⚽⚾⚾🎱🎱\nQuantas bolas de futebol há?',
                        "resposta":"7"
                    },
                    {
                        "pergunta": f'⚾🏈🏀🐯🍌🍓🍎🍊🍋‍🟩🐼🐭🍓🥎🏀🏈🐷🐶🐱🍌🥎⚾🐭🐼🍓🐱🐯\nQuantos animais há?' , 
                        "resposta": "10"
                    }
                ],
                },
            "Padronização": {
                "texto": "Padronização é quando fazemos tudo do mesmo jeitinho para ficar mais fácil de entender.",
                "exercício": [
                    {
                        "pergunta": f'🔴🟢🔴🟢🔴🟢🔴🟢🔴\nQual o próximo?\n1-🔴\n2-🟢',
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'⚪🟡🔺🔸⚪🟡🔺🔸⚪🟡\nQual o  próximo?\n1-🔺\n2-⚪\n3-🔸\n4-🟡',
                        "resposta": "1"
                    },
                    {
                        "pergunta": f'🔷🔷🔶🔷🔷🔶🔷🔷🔶🔷\nQual o próximo?\n1-🔹\n2-🔸\n3-🔶\n4-🔷',
                        "resposta": "4"
                    },
                    {
                        "pergunta": f'🔻🔺🔶🔻🔺🔶🔻\nQual o próximo?\n1-🔺\n2-🔻\n3-🔶',
                        "resposta": "1"
                    },
                    {
                        "pergunta": f'🟢🔻🔻🟢🔻🔻🟢🔻🔻🟢🔻\nQual o próximo?\n1-🟢\n2-🔻',
                        "resposta": "2"
                    },
                ],
            },
            "Adição simples": {
                "texto": "Sabe quando você quer comer maças com seus amigos, e não têm o suficiente? Adição é quando vamos no mercadinho do Seu Zé, para que todo mundo possa comer maças",
                "exercício": [
                    {
                        "pergunta": f'🍓🍓🍓🍓+🍌🍌🍌🍌\nQuantos morangos e bananas há?',
                        "resposta": "8"
                    },
                    {
                        "pergunta": f'🍌🍌🍌🍌+🍓🍓🍓🍓+🍎🍎🍎🍎\nQuantas frutas há?',
                        "resposta": "12"
                    },
                    {
                        "pergunta": f'🍎🍎🍎🍎🍎🍎🍎+🍓🍓🍓🍓🍓\nQuantas frutas há?',
                        "resposta": "12"
                    },
                    {
                        "pergunta": f'1 + 5',
                        "resposta": "6"
                    },
                    {
                        "pergunta": f'3 + 7',
                        "resposta": "10"
                    },
                ],
            },
            "Subtração simples": {
                "texto": "Sabe quando você têm 10 balinhas, e come 5? Agora voê só têm 5, subtração é isso!!",
                "exercício": [
                    {
                        "pergunta": f'🍬🍬🍬 - 🍬\nQuantas balinhas há agora?',
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'⚽⚽⚽⚽-⚽⚽⚽\nQuantas bolas há agora?',
                        "resposta":"1"
                    },
                    {
                        "pergunta": f'🍊🍊🍊🍊🍊🍊🍊 - 5\nQuantas laranjas há agora?',
                        "resposta":"2"
                    },
                    {
                        "pergunta": f'10 - 5',
                        "resposta":"5"
                    },
                    {
                        "pergunta": f'13-7',
                        "resposta":"6"
                    },
                ],
            },
            "Ordem crescente e decresente":{
                "texto":f'Quando temos um número depois do outro ele é chamado de sucessor\nAgora se temos um número antes do outro chamamos de antecessor',
                "exercício":[
                    {
                        "pergunta":"5 ou 8\nQual é maior?",
                        "resposta":"8"
                    },
                    {
                        "pergunta": "10 ou 5\nQual é maior?",
                        "resposta": "10"
                    },
                    {
                        "pergunta": "20 ou 15\nQual é maior?",
                        "resposta": "20"
                    },
                    {
                        "pergunta": f'10- -12-13\nQual é o número que esta faltando?',
                        "resposta": "11"
                    },
                    {
                        "pergunta": f'5-6-7\nQual número vem antes do 5?',
                        "resposta": "4"
                    },
                ],
            },
        },
        "7-8": {
            "Adição e subtração com 2 casas decimais": {
                "texto": "Somaremos da mesma forma de antes, só que agora não conseguiremos contar nos dedos, vamos testar?!",
                "exercício": [
                    {
                        "pergunta": "25 + 10" ,
                        "resposta": "35"
                    },
                    {
                        "pergunta": "55 + 40",
                        "resposta": "95"
                    },
                    {
                        "pergunta": "100-50",
                        "resposta": "50"
                    },
                    {
                        "pergunta": "30 - 15",
                        "resposta": "15"
                    },
                    {   "pergunta": "100 - 30",
                        "resposta": "70"
                    },
                ],
            },
            "Multiplicação": {
                "texto": "Quando vamos somar um número igual um monte de vezes, para não perder tempo usamos o simbolo'x'",
                "exercício": [
                    {
                        "pergunta": "5 x 2",
                        "resposta": "10"
                    },
                    {
                        "pergunta": "4 x 3",
                        'resposta': "12"
                    },
                    {
                        "pergunta": "5 x 6",
                        "resposta": "30"
                    },
                    {
                        "pergunta": "6 x 8",
                        "resposta": "48"
                    },
                    {
                        "pergunta": "9 x 7",
                        "resposta": "63"
                    },
                ],
            },
            "Números pares e ímpares": {
                "texto": f'Pense nos números no salão, você pega um deles e reparte de um em um, repare que alguns podem ser agrupados em pares e alguns sobraram 1\n, os que formaram pares, são chamdos de.. par e os que não são ímpares',
                "exercício": [
                    {
                        "pergunta": "O número 10 é ímpar ou par?",
                        "resposta": "par"
                    },
                    {
                        "pergunta": "O número 23 é ímpar ou par?",
                        "resposta": "ímpar"
                    },
                    {
                        "pergunta": "O número 9 é ímpar ou par?",
                        "resposta": "ímpar"
                    },
                    {
                        "pergunta": "O número 24 é ímpar ou par?",
                        "resposta": "par"
                    },
                    {
                        "pergunta": "O número 13 é ímpar ou par?",
                        "resposta": "ímpar"
                    },
                ],
            },
        },
        "9-10": {
            "Tabuada e multiplicação simples": {
                "texto": "Vamos aprender a tabuada",
                "exercício": [
                    {
                        "pergunta": "pergunta 1",
                        "resposta": "resposta 1"
                    }
                ]
            },
            "Divisão simples": {
                "texto": "Vamos aprender como fazer divisões",
                "exercício": [
                    {
                        "pergunta": "pergunta 1",
                        "resposta": "resposta 1"
                    }
                ]
            },
            "Números decimais": {
                "texto": "Vamos aprender como funcionam os números decimais",
                "exercício": [
                    {
                        "pergunta": "pergunta 1",
                        "resposta": "resposta 1"
                    }
                ]
            }
        },
    },
    "informatica": {
        "5-6": {
            "Partes do Computador": {
                "texto": "Principais componentes",
                "exercício": [ 
                    {
                        "pergunta": "Pergunta 1",
                        "resposta": "Resposta 1"
                    }
                ]
            }
        }
    } 
}

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

def praticarexercício(tema, idade):
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
                mostrarexercício(tema, idade, nomeConteudo)
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)

def mostrarexercício(tema, idade, conteudos):
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

menuPrincipal()