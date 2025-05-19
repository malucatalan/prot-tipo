
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
        if opcao == "1":
            menuConteudosExercicios("matematica", "5-6")
        elif opcao == "2":
            menuConteudosExercicios("matematica", "7-8")
        elif opcao == "3":
            menuConteudosExercicios("matematica", "9-10")
        elif opcao == "0":
            break
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
            break
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
    lista_paragrafos = [
        "Code e Conta é uma plataforma educacional para crianças, "
        "que tem o objetivo de tornar o aprendizado de matemática "
        "e informática mais acessível, divertido e lúdico, "
        "estimulando a criatividade e curiosidade das crianças.",
        
        "Com o crescente uso e avanço da tecnologia, "
        "onde as crianças já nascem em uma era digital, "
        "é de suma importância o domínio de atividades "
        "tecnológicas e do pensamento lógico. "
        "As crianças de hoje são nativas digitais, "
        "por isso é essencial que elas aprendam desde "
        "cedo a usar a tecnologia de forma consciente, "
        "criativa, crítica e responsável.",

        "De acordo com o PISA (Programa Internacional de Avaliação de Estudantes) "
        "no Brasil, mais de 70% das crianças e adolescentes, enfrentam dificuldades "
        "básicas em matemática. Uma análise do PISA 2022 revelou que apenas 3% dos "
        "estudantes brasileiros de baixo nível socioeconômico, têm aprendizado adequado em matemática.",

        "A partir desses dados, nossa equipe constatou a necessidade de uma plataforma que "
        "busque ensinar de maneira democrática e divertida, acentuando o interesse no "
        "aprendizado, tendo como meta auxiliar no aumento do conhecimento de matemática e "
        "informática de forma gratuita e acessível."
        ]
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
            praticaExercicio(tema, idade) 
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
def praticaExercicio(tema, idade):
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
                mostrarExercicio(tema, idade, nomeConteudo)
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)
def mostrarExercicio(tema, idade, conteudos):
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