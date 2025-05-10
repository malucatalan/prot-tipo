from cores import colorir
import os
import time

def limpar_tela():
    os.system('cls')
 
def mostrar_titulo(texto):
    limpar_tela()
    print(colorir("=" * 50, cor="magenta"))
    print(colorir(texto.center(50), cor="magenta", estilo="bold"))
    print(colorir("=" * 50, cor="magenta"))
    print()

def menu_principal():
    while True:
        mostrar_titulo("SISTEMA DE APRENDIZADO INFANTIL")
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
            menu_matematica()
        elif opcao == "2":
            menu_informatica()
        elif opcao == "3":
            sobre_sistema()
        else:
            print(colorir("Opção inválida! Tente novamente.", cor="red"))
            time.sleep(1)
        
def menu_idades(titulo):
    while True:
        mostrar_titulo(titulo)
        print(colorir("Selecione a faixa etária:", cor="blue", estilo="bold"))
        print(colorir("1. 5-6 anos", cor="green"))
        print(colorir("2. 7-8 anos", cor="yellow"))
        print(colorir("3. 9-10 anos", cor="cyan"))
        print()
        print(colorir("0. Voltar", cor="red"))
        print()
        return input(colorir("Escolha uma opção (0-3): ", cor="cyan"))
    
def menu_matematica():
    while True:
        opcao = menu_idades("MATEMÁTICA DIVERTIDA")
        if opcao == "1":
            conteudos_exercicios("matematica", "5-6")
        elif opcao == "2":
            conteudos_exercicios("matematica", "7-8")
        elif opcao == "3":
            conteudos_exercicios("matematica", "9-10")
        elif opcao == "0":
            break

def menu_informatica():
    while True:
        opcao = menu_idades("INFORMÁTICA DIVERTIDA")
        if opcao == "1":
            conteudos_exercicios("informatica", "5-6")
        elif opcao == "2":
            conteudos_exercicios("informatica", "7-8")
        elif opcao == "3":
            conteudos_exercicios("informatica", "9-10")
        elif opcao == "0":
            break

def conteudos_exercicios(tema, idade):
   while True:
        mostrar_titulo(f"{tema.upper()} PARA {idade} ANOS")
        print(colorir("1. Ver Conteúdos", cor="green"))
        print(colorir("2. Praticar Exercícios", cor="yellow"))
        print(colorir("0. Voltar", cor="red"))
        
        
        opcao = input(colorir("\nEscolha: ", cor="cyan"))
        
        if opcao == "1":
            mostrar_conteudo(tema, idade)
        elif opcao == "2":
            mostrar_exercicios(tema, idade) 
        elif opcao == "0":
            break
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)

CONTEUDOS = {
    "matematica": {
        "5-6": {
            "Números de 1 a 50": {
                "texto": "Vamos aprender os números de 1 a 50!\n\n1 - Um\n2 - Dois\n3 - Três\n...\n10 - Dez",
                "exercicios": [
                    {
                        "pergunta": "Conte quantos animais aparecen: 🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱",
                        "resposta": "16"
                    },
                    {
                        "pergunta": "Quantos dedos há em uma mão?",
                        "resposta": "5"
                    }
                ],
                },
            },
            "Formas básicas": {
                "texto": "Formas geométricas básicas:\n\nTriângulo - 3 lados\nQuadrado - 4 lados iguais\nCírculo - Sem cantos",
                "exercicios": [
                    {
                        "pergunta": "Pergunta 1",
                        "resposta": "resposta 1"
                    },
                    {
                        "pergunta": "Pergunta 2",
                        "resposta": "Resposta 2"
                    }
                ],
            },
            "Adição com unidade simples": {
                "texto": "Vamos aprender como fazer pequenas adições",
                "exercicios": [
                    {
                        "pergunta": "Pergunta 1",
                        "resposta": "Resposta 1"
                    },
                    {
                        "pergunta": "Pergunta 2",
                        "resposta": "Resposta 2"
                    }
                ],
            },
            "Subtração com unidade simples": {
                "texto": "Vamos aprender como fazer pequenas subtrações",
                "exercicios": [
                    {
                        "pergunta": "Pergunta 1",
                        "resposta": "Resposta 1"
                    },
                    {
                        "pergunta": "Pergunta 2",
                        "resposta": "resposta 2"
                    }
                ]
            }
        },
        "7-8": {
            "Adição com unidade de dezenas": {
                "texto": "Somando números:",
                "exercicios": [
                    {
                        "pergunta": "Pergunta 1",
                        "resposta": "Resposta 1"
                    },
                    {
                        "pergunta": "Pergunta 2",
                        "resposta": "Resposta 2"
                    }
                ]
            },
            "Subtração com unidade de dezena": {
                "texto": "Vamos aprender como somar números com casas de dezena",
                "exercicios": [
                    {
                        "pergunta": "Pergunta 1",
                        "resposta": "Resposta 1"
                    },
                    {
                        "pergunta": "pergunta 2",
                        'resposta': "resposta 2"
                    }
                ]
            },
            "Formas planas e cilíndricas": {
                "texto": "Vamos aprender os tipos diferentes de formas geométricas"
            }
        },
        "9-10": {
            "Tabuada e multiplicação simples": {
                "texto": "Vamos aprender a tabuada"
            },
            "Divisão simples": {
                "texto": "Vamos aprender como fazer divisões"
            },
            "Números decimais": {
                "texto": "Vamos aprender como funcionam os números decimais"
            }
        },
    "informatica": {}
}

def mostrar_conteudo_detalhado(tema, idade, conteudo):
    dados = CONTEUDOS[tema][idade][conteudo]
    
    limpar_tela()
    print(colorir(f"{conteudo.upper()}", cor="blue", estilo="bold"))
    print(colorir("=" * 50, cor="magenta"))
    print(dados["texto"])
    input(colorir("\nPressione Enter para voltar...", cor="yellow"))

def mostrar_conteudo(tema, idade):
    while True:
        mostrar_titulo(f"CONTEÚDOS DE {tema.upper()} PARA {idade} ANOS")
        
        for i, conteudo in enumerate(CONTEUDOS[tema][idade].keys(), 1):
            print(colorir(f"{i}. {conteudo}", cor="cyan"))
        
        print(colorir("\n0. Voltar", cor="red"))
        
        opcao = input(colorir("\nEscolha um conteúdo: ", cor="yellow"))
        
        if opcao == "0":
            break
        elif opcao.isdigit() and 0 < int(opcao) <= len(CONTEUDOS[tema][idade]):
            conteudo = list(CONTEUDOS[tema][idade].keys())[int(opcao)-1]
            mostrar_conteudo_detalhado(tema, idade, conteudo)
        else:
            print(colorir("Opção inválida! Tente novamente.", cor="red"))
            time.sleep(1)

def menu_exercicios(tema, idade):
    while True:
        mostrar_titulo(f"EXERCÍCIOS DE {tema.upper()}")
        conteudos = CONTEUDOS[tema][idade]
        for i, conteudo in enumerate(conteudos.keys(), 1):
            if "exercicios" in conteudos[conteudo]: 
                print(colorir(f"{i}. {conteudo}", cor="cyan"))
        
        print(colorir("\n0. Voltar", cor="red"))
        
        opcao = input(colorir("\nEscolha o conteúdo para praticar: ", cor="yellow"))
        
        if opcao == "0":
            break
        elif opcao.isdigit() and 0 < (int(opcao) <= len(conteudos)):
            conteudo = list(conteudos.keys())[int(opcao)-1]
            if "exercicios" in conteudos[conteudo]:
                mostrar_exercicios(tema, idade, conteudo)
            else:
                print(colorir("Este conteúdo não tem exercícios ainda!", cor="red"))
                time.sleep(1)
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)

def mostrar_exercicios(tema, idade, conteudo_selecionado=None):
    limpar_tela()
    
    if not conteudo_selecionado:
        conteudo_selecionado = list(CONTEUDOS[tema][idade].keys())[0] 
    
    exercicios = CONTEUDOS[tema][idade][conteudo_selecionado]["exercicios"]
    
    print(colorir(f"EXERCÍCIOS: {conteudo_selecionado.upper()}", cor="green", estilo="bold"))
    print(colorir("=" * 50, cor="magenta"))

    quantidade_acertos = 0
    quantidade_erros = 0
    for i, exercicio in enumerate(exercicios, 1):
        print(colorir(f"\nExercício {i}: {exercicio['pergunta']}", cor="yellow"))
        resposta = input(colorir("Sua resposta: ", cor="cyan"))
        
        if resposta == exercicio["resposta"]:
            print(colorir("Correto!", cor="green"))
            quantidade_acertos += 1 
        else:
            quantidade_erros += 1
            print(colorir(f"Errado. Resposta: {exercicio['resposta']}", cor="red"))
        
        time.sleep(1)

    
    #Exibir quantidade acertos---
    time.sleep(0.8)
    limpar_tela()
    if quantidade_acertos > 0:
        if quantidade_erros == 0:
            print(colorir("Parabéns! Você acertou todas as repostas.", fundo="bg_green"))
        print(colorir(f"Repostas corretas: {quantidade_acertos}", cor="green"))
    if quantidade_erros > 0:
        if quantidade_acertos == 0:
            print(colorir("Estude mais, amigo.", cor="red", fundo="bg_red"))
        print(colorir(f"Respostas incorretas: {quantidade_erros}", cor="red"))

    
    
    input(colorir("\nPressione Enter para voltar...", cor="yellow"))
menu_principal()