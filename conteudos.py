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