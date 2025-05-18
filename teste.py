
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
            menuConteudosExercicios("matematica", "5-6")
        elif opcao == "2":
            menuConteudosExercicios("matematica", "7-8")
        elif opcao == "3":
            menuConteudosExercicios("matematica", "9-10")
        elif opcao == "0":
            break
def menuInformatica():
    while True:
        mostrarTitulo("INFORMÁTICA DIVERTIDA")
        mostrarOpcoesIdades()

        opcao = input(colorir("Escolha uma opção (0-3): ", cor="cyan"))
        if opcao == "1":
            menuConteudosExercicios("informatica", "5-6")
        elif opcao == "2":
            menuConteudosExercicios("informatica", "7-8")
        elif opcao == "3":
            menuConteudosExercicios("informatica", "9-10")
        elif opcao == "0":
            break
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
            praticarExercicios(tema, idade) 
        elif opcao == "0":
            break
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)

CONTEUDOS = {
    "matematica": {
        "5-6": {
            "Números de 1 a 50": {
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
                "exercicios": [
                    {
                        "pergunta": "Conte quantos animais aparecen: 🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱",
                        "resposta": "22"
                    },
                    {
                        "pergunta": "Conte quantos dedos há em uma mão",
                        "resposta": "5"
                    }
                ],
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
                "texto": "Vamos aprender os tipos diferentes de formas geométricas",
                "exercicios": [
                    {
                        "pergunta": "pergunta 1",
                        "resposta": "resposta1"
                    },
                    {
                        "pergunta": "pergunta 2",
                        "resposta": "resposta 2"
                    }
                ]
            }
        },
        "9-10": {
            "Tabuada e multiplicação simples": {
                "texto": "Vamos aprender a tabuada",
                "exercicios": [
                    {
                        "pergunta": "pergunta 1",
                        "resposta": "resposta 1"
                    }
                ]
            },
            "Divisão simples": {
                "texto": "Vamos aprender como fazer divisões",
                "exercicios": [
                    {
                        "pergunta": "pergunta 1",
                        "resposta": "resposta 1"
                    }
                ]
            },
            "Números decimais": {
                "texto": "Vamos aprender como funcionam os números decimais",
                "exercicios": [
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
                "exercicios": [ 
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

def praticarExercicios(tema, idade):
    while True:
        mostrarTitulo(f"EXERCÍCIOS DE {tema.upper()}")
        
        conteudosComExercicios = list(CONTEUDOS[tema][idade].items())  

        for k, (nome, _) in enumerate(conteudosComExercicios, 1):
            print(colorir(f"{k}. {nome}", cor="cyan"))
        print()
        print(colorir("0. Voltar", cor="red"))
        print()
        opcao = input(colorir("Escolha um conteúdo para praticar: ", cor="yellow"))
        
        if opcao == "0":
            break
        elif opcao.isdigit(): 
            indice = int(opcao) - 1
            if indice >= 0 and indice < len(conteudosComExercicios):
                nomeConteudo = conteudosComExercicios[indice][0]
                mostrarExercicios(tema, idade, nomeConteudo)
        else:
            print(colorir("Opção inválida!", cor="red"))
            time.sleep(1)

def mostrarExercicios(tema, idade, conteudos):
    limparTela()
    
    exercicios = CONTEUDOS[tema][idade][conteudos]["exercicios"]
    
    mostrarTitulo(f"EXERCÍCIOS: {conteudos.upper()}")
    
    quantidade_acertos = 0
    quantidade_erros = 0
    
    for i, exercicio in enumerate(exercicios, 1):
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