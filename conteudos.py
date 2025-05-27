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
            
                "exercício": 
                [
                    {
                        "pergunta": "Conte quantos dedos há em uma mão",
                        "alternativas":["a)1","b)2","c)3","d)4","E)5"],
                        "resposta": "4" 
                    },
                    {
                        "pergunta":f'🍓🍓🍓🍓🍓🍓🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌\nQuantos morangos e bananas há?' ,
                        "alternativas":["a)10","b)20","c)16","d)14","E)15"],
                        "resposta": "2"  
                    },
                    {
                        "pergunta": f'🐶🐶🐱🐱🐭🐭🐼🐼🐷🐷🐯🐯\nQuantos animais há?',
                        "alternativas":["a)15","b)12","c)13","d)23","E)7"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": f'⚽🏀⚽⚽⚽🏀🏀⚽⚽⚽⚾⚾🎱🎱\nQuantas bolas de futebol há?',
                        "alternativas":["a)5","b)7","c)14","d)9","E)6"],
                        "resposta":"1"
                    },
                    {
                        "pergunta": f'⚾🏈🏀🐯🍌🍓🍎🍊🍋‍🟩🐼🐭🍓🥎🏀🏈🐷🐶🐱🍌🥎⚾🐭🐼🍓🐱🐯\nQuantos animais há?' , 
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "0"
                    }
                ],
                },
            "Padronização": {
                "texto": "Padronização é quando fazemos tudo do mesmo jeitinho para ficar mais fácil de entender.",
                "exercício": [
                    {
                        "pergunta": f'🔴🟢🔴🟢🔴🟢🔴🟢🔴\nQual o próximo?',
                        "alternativas":["a)🔴","b)🔴🔴","c)🟢","d)🟢🟢","E)🔴🟢"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'⚪🟡🔺🔸⚪🟡🔺🔸⚪🟡\nQual o  próximo?',
                        "alternativas":["a)🔺","b)⚪","c)🔸","d)🟡","E)🔺🔺"],
                        "resposta": "0"
                    },
                    {
                        "pergunta": f'🔷🔷🔶🔷🔷🔶🔷🔷🔶🔷\nQual o próximo?',
                        "alternativas":["a)🔹","b)🔸","c)🔶","d)🔷","E)🔹🔹"],
                        "resposta": "0"
                    },
                    {
                        "pergunta": f'🔻🔺🔶🔻🔺🔶🔻\nQual o próximo?',
                        "alternativas":["a)🔺","b)🔻","c)🔶","d)🔶🔶","E)🔺🔻"],
                        "resposta": "0"
                    },
                    {
                        "pergunta": f'🔻🟢🔻🔻🟢🔻🔻🟢🔻\nQual o próximo?',
                        "alternativas":["a)🟢🔻","b)🔻🔻","c)🔻","d)🟢🟢","E)🟢"],
                        "resposta": "2"
                    },
                ],
            },
            "Adição simples": {
                "texto": "Sabe quando você quer comer maças com seus amigos, e não têm o suficiente? Adição é quando vamos no mercadinho do Seu Zé, para que todo mundo possa comer maças",
                "exercício": [
                    {
                        "pergunta": f'🍓🍓🍓🍓+🍌🍌🍌🍌\nQuantos morangos e bananas há?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "8"
                    },
                    {
                        "pergunta": f'🍌🍌🍌🍌+🍓🍓🍓🍓+🍎🍎🍎🍎\nQuantas frutas há?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "12"
                    },
                    {
                        "pergunta": f'🍎🍎🍎🍎🍎🍎🍎+🍓🍓🍓🍓🍓\nQuantas frutas há?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "12"
                    },
                    {
                        "pergunta": f'1 + 5',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "6"
                    },
                    {
                        "pergunta": f'3 + 7',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "10"
                    },
                ],
            },
            "Subtração simples": {
                "texto": "Sabe quando você têm 10 balinhas, e come 5? Agora voê só têm 5, subtração é isso!!",
                "exercício": [
                    {
                        "pergunta": f'🍬🍬🍬 - 🍬\nQuantas balinhas há agora?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'⚽⚽⚽⚽-⚽⚽⚽\nQuantas bolas há agora?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"1"
                    },
                    {
                        "pergunta": f'🍊🍊🍊🍊🍊🍊🍊 - 5\nQuantas laranjas há agora?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"2"
                    },
                    {
                        "pergunta": f'10 - 5',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"5"
                    },
                    {
                        "pergunta": f'13-7',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"6"
                    },
                ],
            },
            "Ordem crescente e decresente":{
                "texto":f'Quando temos um número depois do outro ele é chamado de sucessor\nAgora se temos um número antes do outro chamamos de antecessor',
                "exercício":[
                    {
                        "pergunta":"5 ou 8\nQual é maior?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"8"
                    },
                    {
                        "pergunta": "10 ou 5\nQual é maior?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "10"
                    },
                    {
                        "pergunta": "20 ou 15\nQual é maior?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "20"
                    },
                    {
                        "pergunta": f'10- -12-13\nQual é o número que esta faltando?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "11"
                    },
                    {
                        "pergunta": f'5-6-7\nQual número vem antes do 5?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
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
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "35"
                    },
                    {
                        "pergunta": "55 + 40",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "95"
                    },
                    {
                        "pergunta": "100-50",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "50"
                    },
                    {
                        "pergunta": "30 - 15",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "15"
                    },
                    {   "pergunta": "100 - 30",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "70"
                    },
                ],
            },
            "Multiplicação": {
                "texto": "Quando vamos somar um número igual um monte de vezes, para não perder tempo usamos o simbolo'x'",
                "exercício": [
                    {
                        "pergunta": "5 x 2",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "10"
                    },
                    {
                        "pergunta": "4 x 3",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        'resposta': "12"
                    },
                    {
                        "pergunta": "5 x 6",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "30"
                    },
                    {
                        "pergunta": "6 x 8",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "48"
                    },
                    {
                        "pergunta": "9 x 7",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "63"
                    },
                ],
            },
            "Números pares e ímpares": {
                "texto": f'Quando vc possui balinhas para dividir com seus amigos, imagine que se você conseguir dar duas balinhas para cada amigo, seu número de balinhas é par, do contrario ele é impar',
                "exercício": [
                    {
                        "pergunta": "O número 10 é ímpar ou par?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "par"
                    },
                    {
                        "pergunta": "O número 23 é ímpar ou par?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "ímpar"
                    },
                    {
                        "pergunta": "O número 9 é ímpar ou par?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "ímpar"
                    },
                    {
                        "pergunta": "O número 24 é ímpar ou par?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "par"
                    },
                    {
                        "pergunta": "O número 13 é ímpar ou par?",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "ímpar"
                    },
                ],
            },
            "Números Ordinais":{
                "texto": f'Quando a professora coloca todo mundo em fila, para que ela não se perca ela começa a colocar um número em cada colega, por exemplo, o numero 1 da fila será o primeiro',
                "exercício":[
                    {
                        "pergunta": f'🐷🐱🐼🐯🐭\nQual o primerio animal da fila',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "Porco"
                    },
                    {
                        "pergunta":f'🟠🔴⚪🟢\nQual a posição do vermelho',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"Segundo"
                    },
                    {
                        "pergunta": f'👩🏻👦🏻👩🏻👦🏻👩🏻👦🏻👩🏻\nQual a ultima posição da menina?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "Setima"
                    },
                    {
                        "pergunta": f'🥇🥈🥉\nQual a posição da medalha de bronze?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "Terceira"
                    },
                    {
                        "pergunta": f'Qual a posição da pessoa 10 de uma fila?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "Décima"    
                    }
                ],
            },
            "Sequência Númerica e Raciocícinio Lógico":{
                "texto":"",
                "exercicio":[
                    {
                        "pergunta": f'1-3-5-7-\nQual o próximo número?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "9"
                    },
                    {
                        "pergunta": f'10-20-30-\nQual o próximo número?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"40"
                    },
                    {
                        "pergunta": f'10-8-6-\nQual o próximo número?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "4"
                    },
                    {
                        "pergunta": f'12-9-6-\nQual o próximo número?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"3"
                    },
                    {
                        "pergunta": f'2-4-8-\nQual o próximo número?',
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "16"
                    },
                ],
            },
        },
        "9-10": {
            "Tabuada": {
                "texto": "Vamos decorar a tabuada!?",
                "exercício": [
                    {
                        "pergunta": "3x4",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "12"
                    },
                    {
                        "pergunta": "4x5",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"20"
                    },
                    {
                        "pergunta": "9x10",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "90"
                    },
                    {
                        "pergunta": "6x8",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "48"
                    },
                    {
                        "pergunta": "12x5",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "60"
                    },
                ],
            },
            "Divisão simples": {
                "texto": "Vamos aprender como fazer divisões!",
                "exercício": [
                    {
                        "pergunta": "10/10",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "1"
                    },
                    {
                        "pergunta":"64/8",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"8"
                    },
                    {
                        "pergunta":"50/5",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta": "5"
                    },
                    {
                        "pergunta":"36/6",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":"6"
                    },
                    {
                        "pergunta":"",
                        "alternativas":["a)10","b)7","c)14","d)9","E)6"],
                        "resposta":""
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