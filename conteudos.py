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
                        "alternativas":["a)15","b)10","c)8","d)9","E)16"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'🍌🍌🍌🍌+🍓🍓🍓🍓+🍎🍎🍎🍎\nQuantas frutas há?',
                        "alternativas":["a)10","b)17","c)14","d)12","E)16"],
                        "resposta": "3"
                    },
                    {
                        "pergunta": f'🍎🍎🍎🍎🍎🍎🍎+🍓🍓🍓🍓🍓🍓🍓🍓🍓\nQuantas frutas há?',
                        "alternativas":["a)14","b)17","c)15","d)19","E)16"],
                        "resposta": "4"
                    },
                    {
                        "pergunta": f'1 + 5',
                        "alternativas":["a)4","b)7","c)6","d)9","E)15"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'3 + 7',
                        "alternativas":["a)10","b)3","c)4","d)9","E)37"],
                        "resposta": "0"
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
                        "alternativas":["a)10","b)5","c)12","d)15","E)16"],
                        "resposta":"1"
                    },
                    {
                        "pergunta": f'13-7',
                        "alternativas":["a)20","b)7","c)6","d)4","E)12"],
                        "resposta":"2"
                    },
                ],
            },
            "Ordem crescente e decresente":{
                "texto":f'Quando temos um número depois do outro ele é chamado de sucessor\nAgora se temos um número antes do outro chamamos de antecessor',
                "exercício":[
                    {
                        "pergunta":"5 ou 8\nQual é maior?",
                        "alternativas":["a)8","b)5"],
                        "resposta":"0"
                    },
                    {
                        "pergunta": "10 ou 5\nQual é maior?",
                        "alternativas":["a)5","b)10"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": "20 ou 15\nQual é menor?",
                        "alternativas":["a)15","b)20"],
                        "resposta": "0"
                    },
                    {
                        "pergunta": f'10- -12-13\nQual é o número que esta faltando?',
                        "alternativas":["a)12","b)10","c)11","d)13"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'5-6-7\nQual número vem antes do 5?',
                        "alternativas":["a)4","b)7","c)6"],
                        "resposta": "0"
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
                        "alternativas":["a)35","b)15","c)14"],
                        "resposta": "0"
                    },
                    {
                        "pergunta": "55 + 40",
                        "alternativas":["a)15","b)95","c)42"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": "100-50",
                        "alternativas":["a)10","b)150","c)50"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": "30 - 15",
                        "alternativas":["a)15","b)7","c)14"],
                        "resposta": "0"
                    },
                    {   "pergunta": "100 - 30",
                        "alternativas":["a)130","b)70","c)140"],
                        "resposta": "1"
                    },
                ],
            },
            "Multiplicação": {
                "texto": "Quando vamos somar um número igual um monte de vezes, para não perder tempo usamos o simbolo'x'",
                "exercício": [
                    {
                        "pergunta": "5 x 2",
                        "alternativas":["a)10","b)7","c)3",],
                        "resposta": "0"
                    },
                    {
                        "pergunta": "4 x 3",
                        "alternativas":["a)1","b)7","c)12"],
                        'resposta': "2"
                    },
                    {
                        "pergunta": "5 x 6",
                        "alternativas":["a)1","b)11","c)30"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": "6 x 8",
                        "alternativas":["a)14","b)48","c)2"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": "9 x 7",
                        "alternativas":["a)63","b)70","c)140"],
                        "resposta": "0"
                    },
                ],
            },
            "Números pares e ímpares": {
                "texto": f'Quando vc possui balinhas para dividir com seus amigos, imagine que se você conseguir dar duas balinhas para cada amigo, seu número de balinhas é par, do contrario ele é ímpar',
                "exercício": [
                    {
                        "pergunta": "O número 10 é ímpar ou par?",
                        "alternativas":["a)Par","b)Ímpar"],
                        "resposta": "0"
                    },
                    {
                        "pergunta": "O número 23 é ímpar ou par?",
                        "alternativas":["a)Par","b)Ímpar"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": "O número 9 é ímpar ou par?",
                        "alternativas":["a)Par","b)Ímpar"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": "O número 24 é ímpar ou par?",
                        "alternativas":["a)Par","b)Ímpar"],
                        "resposta": "0"
                    },
                    {
                        "pergunta": "O número 13 é ímpar ou par?",
                        "alternativas":["a)Par","b)Ímpar"],
                        "resposta": "1"
                    },
                ],
            },
            "Números Ordinais":{
                "texto": f'Quando a professora coloca todo mundo em fila, para que ela não se perca ela começa a colocar um número em cada colega, por exemplo, o numero 1 da fila será o primeiro',
                "exercício":[
                    {
                        "pergunta": f'🐷🐱🐼🐯🐭\nQual o primerio animal da fila',
                        "alternativas":["a)Porco","b)Panda","c)Tigre","d)Rato","E)Gato"],
                        "resposta": "0"
                    },
                    {
                        "pergunta":f'🟠🔴⚪🟢\nQual a posição do vermelho',
                        "alternativas":["a)Primeira","b)Segunda","c)Terceira","d)Quarta","E)Quinta"],
                        "resposta":"1"
                    },
                    {
                        "pergunta": f'👩🏻👦🏻👩🏻👦🏻👩🏻👦🏻👩🏻\nQual a ultima posição da menina?',
                        "alternativas":["a)Décima","b)Sétima","c)Segunda","d)Quinta","E)Sexta"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": f'🥇🥈🥉\nQual a posição da medalha de bronze?',
                        "alternativas":["a)Primeira","b)Segunda","c)Terceira"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'Qual a posição da pessoa 10 de uma fila?',
                        "alternativas":["a)Quinta","b)Primeira","c)Décima","d)Oitava","E)Nona"],
                        "resposta": "2"    
                    }
                ],
            },
            "Sequência Númerica e Raciocícinio Lógico":{
                "texto":"Sequência númerica é como se fosse uma regra para advinhar qual será o próximo passo. Imagine os dias da semana, depois de Segunda sempre vêm Terça, depois Quarta e assim por diante.",
                "exercicio":[
                    {
                        "pergunta": f'1-3-5-7-\nQual o próximo número?',
                        "alternativas":["a)10","b)7","c)9","d)12","E)3"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'10-20-30-\nQual o próximo número?',
                        "alternativas":["a)10","b)30","c)15","d)40","E)20"],
                        "resposta":"3"
                    },
                    {
                        "pergunta": f'10-8-6-\nQual o próximo número?',
                        "alternativas":["a)8","b)12","c)4","d)10","E)6"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": f'12-9-6-\nQual o próximo número?',
                        "alternativas":["a)10","b)7","c)12","d)6","E)3"],
                        "resposta":"4"
                    },
                    {
                        "pergunta": f'2-4-8-\nQual o próximo número?',
                        "alternativas":["a)10","b)4","c)14","d)16","E)16"],
                        "resposta": "4"
                    },
                ],
            },
        },
        "9-10": {
            "Tabuada": {
                "texto": "Vamos decorar a tabuada!?",
                "exercício": [
                    {
                        "pergunta": "3 x 4",
                        "alternativas":["a)10","b)7","c)12","d)9","E)6"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": "4 x 5",
                        "alternativas":["a)25","b)30","c)12","d)15","E)20"],
                        "resposta":"4"
                    },
                    {
                        "pergunta": "9 x 10",
                        "alternativas":["a)100","b)12","c)60","d)90","E)1"],
                        "resposta": "3"
                    },
                    {
                        "pergunta": "6 x 8",
                        "alternativas":["a)42","b)36","c)48","d)56","E)40"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": "12 x 5",
                        "alternativas":["a)10","b)70","c)12","d)50","E)60"],
                        "resposta": "4"
                    },
                ],
            },
            "Divisão simples": {
                "texto": "Não sabe quando você têm algumas balas e quer dividir com seus amigos? Divisão funciona igualzinho na matemática",
                "exercício": [
                    {
                        "pergunta": "10 / 10",
                        "alternativas":["a)10","b)1","c)20","d)0","E)21"],
                        "resposta": "1"
                    },
                    {
                        "pergunta":"64 / 8",
                        "alternativas":["a)8","b)70","c)56","d)9","E)5"],
                        "resposta":"0"
                    },
                    {
                        "pergunta":"50 / 5",
                        "alternativas":["a)50","b)45","c)10","d)5","E)12"],
                        "resposta": "2"
                    },
                    {
                        "pergunta":"36 / 6",
                        "alternativas":["a)12","b)28","c)14","d)10","E)6"],
                        "resposta":"4"
                    },
                    {
                        "pergunta":"72 / 8",
                        "alternativas":["a)10","b)7","c)8","d)9","E)6"],
                        "resposta":"3"
                    }
                ]
            },
            "Lógica matemática": {
                "texto": "Lógica matemática é como um superpoder, que desenvolvemos para resolver probleminhas mais complexos",
                "exercício": [
                    {
                        "pergunta": "João tem  duas balas a mais que Ana, se Ana tem 10 balas. Quantas balas João possui?",
                        "alternativas":["a)10","b)12","c)8","d)15","E)20"],
                        "resposta": "1"
                    },
                    {
                        "pergunta":"José consegue pular 2 vezes mais corda que Maria, se Maria consegue pular 10 vezes. Quantas vezes José consegue pular?",
                        "alternativas":["a)14","b)5","c)8","d)15","E)20"],
                        "resposta": "4"
                    },
                    {
                        "pergunta":"Um macaquinho come metade da quantidade que um Gorila, se o gorila come 10 bananas. Quantas bananas come o macaquinho?",
                        "alternativas": ["a)2","b)5","c)20","d)12","E)10"],
                        "resposta": "1"
                    },
                    {
                        "pergunta": "Se Leonardo tem 50 lápis, e Rafael tem 10 lápis a menos. Quantos lápis Rafael tem?",
                        "alternativas": ["a)20","b)30","c)40","d)50","E)60"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": "Manuela vende uma limonada por 2 reais, José por 4, Maria por 8. Por quanto Júlia vende a sua limonada?",
                        "alternativas": ["a)20","b)16","c)10","d)8","E)4"],
                        "resposta": "1"
                    },
                ],
            },
            "Matemática Financeira":{
                "texto": "Toda vez que o seu pai vai ao mercado comprar arroz, feijão ele precisa ver o preço e calcular se ele pode ou não comprar. Vamos ver como funciona?",
                "exercício":[
                    {
                        "pergunta": '''

🍎=  R$10,00
🍉 = R$20,00
🍇 = R$7,50
🍍=  R$14,00

Se você comprar 4 maças, e entregar uma nota de 50 reais, quanto você deverá receber de troco?''',
                        "alternativas": ["a)25","b)16","c)10","d)18","E)20"],
                        "resposta": "2"
                    },
                    {
                        "pergunta": '''

🍔 = R$15,00
🍕 = R$10,00
🍟 = R$5,00

Se você comprar 4 hamburguers e 2 batatas fritas. Com quantas notas de 10 reais, você irá pagar?
''',
                        "alternativas": ["a)2","b)6","c)1","d)8","E)7"],
                        "resposta": "4"
                    },
                    {
                        "pergunta": '''

🍫 = R$5,00
🍬= R$6,00
🍭= R$2,00
🍮= R$13,00

Se você tivesse apenas 28,00 reais. Qual o máximo de chocolates que você conseguiria comprar, sabendo que você vai comprar um pudim.
''',
                        "alternativas": ["a)2","b)6","c)1","d)3","E)4"],
                        "resposta": "3",
                    },
                    {
                        "pergunta": '''

⚽= R$20,00
🏀= R$30,00
🏈= R$35,00
⚾= R$5,00

Quantas bolas de futebol americano seria posível comprar com o preço de 7 bolas de futebol?
''',
                        "alternativas": ["a)4","b)2","c)1","d)8","E)6"],
                        "resposta": "0",
                    },
                    {
                        "pergunta": '''

📱= R$1500,00
⌚= R$1000,00
💻= R$4000,00

Você quer comprar um presente para a sua mae e para o seu pai, mas você só possui 5500,00 reais. Para que, não sobre nada, qual deve ser a sua escolha?
''',
                        "alternativas": ["a)Um celular e um relogio","b)Dois celulares","c)Dois computadores","d)Um celular e um computador","E)Um relógio e um computador"],
                        "resposta": "3",
                    },
                ],
            },
        },
    },
    "informatica": {
            "5-6": {
                    "Reconhecimento de Padrões": {
                    "texto": 'Sabe quando a gente vê algo que acontece do mesmo jeito várias vezes? Por exemplo, cores que se repetem: 🔴🟢🔴🟢🔴🟢🔴🟢 \nvocê sabe que depois do verde vem o vermelho, porque elas sempre aparecem na mesma sequencia.\nIsso é um padrão - uma coisa que se repete sempre igual.',
                    "exercício": [ 
                        {
                            "pergunta": f'🟠🔵🟠🔵🟠🔵🟠🔵\nQual alternativa completa o padrão?',
                            "alternativas":["a)🟠🟤","b)🔵🟠","c)🟠🔵","d)🟠🟢","E)🔶🔵"],
                            "resposta": "2"
                        },
                        {
                            "pergunta": f'🟥🟥▫️⚪🟥🟥▫️⚪🟥🟥▫️⚪🟥\nQual alternativa completa o padrão?',
                            "alternativas":["a)⚪⚪⚪","b)▫️⚪🟥","c)▫️▫️🟠","d)⚪🟥▫️","E)🟥▫️⚪"],
                            "resposta": "4"
                        },
                        {
                            "pergunta": f'🟩⬛🟩⬛🟩⬛🟩\nQual alternativa completa o padrão?',
                            "alternativas": ["a)🟥⬛", "b)⬛🟩", "c)🟩⬛", "d)🟧🟩", "e)⬛⬛"],
                            "resposta": "1"
                        },
                        {
                            "pergunta": f'🌳🦊🌳🌳🦊🌳🌳🦊🌳🌳\nQual alternativa completa o padrão?',
                            "alternativas":["a)🦊🌳🌳","b)🌳🌳🦊","c)🌳🌳🌳","d)🦊🦊🦊","E)🦊🌳🦊"],
                            "resposta": "0"
                        },
                        {
                            "pergunta": f'Pergunta 🐶🐶🐶🐶🐱🐱🐱🐱🐶🐶🐶🐶🐱🐱🐱🐱🐶🐶\nQual alternativa completa o padrão?',
                            "alternativas":["a)🐶⚪","b)🐱🐱","c)🐱🐶🐱","d)🐶🐱","E)🐶🐶"],
                            "resposta": "4"
                        }
                        ]
                    },
                
            
                    "Algoritmo Simples":{
                    "texto": "🧩 Algoritmo é quando a gente faz as coisas em uma ordem certinha para dar certo! Como escovar os dentes, tomar banho 🚿 ou fazer um sanduíche 🥪.",
                    "exercício" : [
                        {
                            "pergunta": "Qual a ordem certa para ESCOVAR OS DENTES?",
                            "alternativas":[
                            "a)🧴 Coloca pasta --> 🪥 Escova --> 💧 Molha a escova --> 🫧 Enxagua a boca",
                            "b)💧 Molha a escova --> 🧴 Coloca pasta --> 🪥 Escova --> 🫧 Enxagua a boca",
                            "c) 🪥 Escova --> 🧴 Coloca pasta --> 🫧 Enxagua a boca --> 💧 Molha a escova",
                            "d) 🫧 Enxagua a boca --> 🧴 Coloca pasta --> 🪥 Escova --> 💧 Molha a escova"
                            ],
                            "resposta":"1"
                        },
                        {
                            "pergunta": "🥪 Vamos fazer um sanduíche. Qual é o algoritmo correto?",
                            "alternativas":[
                            "a) 🍞 Pega o pão --> 🧈 Passa recheio --> 🍞 Coloca outro pão",
                            "b) 🧈 Coloca recheio --> 😋 Come --> 🍞 Pega o pão",
                            "c) 🧈 Passa manteiga --> 🍞 Guarda o pão --> 🍽️ Coloca no prato",
                            "d) 😋 Come o recheio --> 🍞 Coloca o pão --> 🔪 Passa a faca"
                            ],
                            "resposta":"0"
                        },
                        {
                            "pergunta": "👟 Qual é o algoritmo para colocar os sapatos?",
                            "alternativas":[
                            "a) 🎀 Amarra --> 🧦 Coloca a meia --> 👟 Coloca o sapato",
                            "b) 👟 Coloca o sapato --> ❌ Tira --> 🎀 Amarra",
                            "c) 🧦 Coloca a meia --> 👟 Coloca o sapato --> 🎀 Amarra"
                            ],
                            "resposta":"2"
                        },
                        {
                            "pergunta": "📅 Como organizar seu dia para estudar? 📚☀️",
                            "alternativas": [
                                "a) ☕ Toma café --> 🛋️ Descansa --> 📖 Estuda --> ⏰ Acorda",
                                "b) 📖 Estuda --> ⏰ Acorda --> ☕ Toma café --> 🛋️ Descansa",
                                "c) 🛋️ Descansa --> ☕ Toma café --> 📖 Estuda --> ⏰ Acorda",
                                "d) ⏰ Acorda --> ☕ Toma café --> 📖 Estuda --> 🛋️ Descansa"
                            ],
                            "resposta": "3"
                        },
                        {
                            "pergunta": "🍳 Qual é a ordem certa para preparar um ovo cozido? 🥚💧",
                            "alternativas": [
                                "a) 🥄 Tira o ovo da água --> 🥚 Coloca o ovo na água --> ⏳ Espera cozinhar",
                                "b) ⏳ Espera cozinhar --> 🥚 Coloca o ovo na água --> 🥄 Tira o ovo da água",
                                "a) 🥚 Coloca o ovo na água --> ⏳ Espera cozinhar --> 🥄 Tira o ovo da água",
                                "d) 🥚 Coloca o ovo na água --> 🥄 Tira o ovo da água --> ⏳ Espera cozinhar"
                            ],
                            "resposta": "2"
                        }
                        ]
                    },
                    "Verdadeiro ou Falso":{
                    "texto":"Você vai ver frases como: 'O leite vem da vaca' — Verdadeiro! ✅\nOu então: “A lua brilha porque tem lâmpada dentro” — Ihh, Falso! ❌",
                    "exercício":[
                        {
                            "pergunta":"Um cachorro mia?",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"1"
                        },
                        {
                            "pergunta":"O sol aparece durante a noite?",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"1"
                        },
                        {
                            "pergunta":"Usamos escova de dentes para pentear o cabelo? ",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"1"
                        },
                        {
                            "pergunta":"O avião serve para voar?",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"0"
                        },
                        {
                            "pergunta":"A geladeira ajuda a conservar os alimentos?",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"0"
                        },                        
                        ]
                    }
                },
            "7-8":  {
                    "Identificação de Padrões":{
                    "texto":"Identificar padrões é observar e descobrir o que se repete. Pode ser uma sequência de cores, formas, números ou letras.\nQuando o padrão é mais difícil, ele pode mudar um pouco a cada vez, e precisamos prestar bem atenção para entender a regra.",
                    "exercício": [
                        {
                            "pergunta":"Se a sequencia for:\n2, 4, 6, 8, ___ --> Qual número vem agora? ",
                            "alternativas":["a) 9 ", "b) 10", "c)8", "d) 16"],
                            "resposta":"1"                    
                        },
                        {   
                            "pergunta": "Complete a sequência:\nA, C, E, G, ___ --> Qual letra vem agora?",
                            "alternativas": ["a) H", "b) I", "c) J", "d) K"],
                            "resposta": "1"
                        },
                        {   
                            "pergunta": "Observe a sequência:\n🐶 🐱 🐶 🐱 🐶 🐸 🐶 🐱\n👉 Qual figura está fora do padrão?",
                            "alternativas": ["a) 🐶", "b) 🐱", "c) 🐸"],
                            "resposta": "2"
                        },
                        {
                            "pergunta": "Qual figura está fora do padrão?\n🟡🟢🔵🟡🟢🔵🟡🔴\n👉 Qual é a diferente?",
                            "alternativas": ["a) 🟢", "b) 🔵", "c) 🔴", "d) 🟡"],
                            "resposta": "2"
                        },
                        {
                            "pergunta": "Complete a sequência:\n🔺🔵🔺🔵🔺 ___\n👉 Qual figura vem agora?",
                            "alternativas": ["a) 🔵", "b) 🔺", "c) 🟢", "d) 🔴"],
                            "resposta": "0"
                        },
                        ]
                    },
                    "Hardware/Software":{
                    "texto":"Hardware é tudo que você pode tocar no computador, como teclado e mouse.\n"
                            "Software é o que esta dentro do computador, como jogos e programas que usamos para densenhar ou escrever.",
                    "exercício":[
                        {
                            "pergunta":"O monitor 🖥️, que mostra as imagens do computador, é ____________________",
                            "alternativas":["🖥️  Hardware","🌐 Software"],
                            "resposta":"0"
                        },
                        {
                            "pergunta":"O navegador de internet 🌐 é um tipo de ____________________:",
                            "alternativas":["🖥️  Hardware","🌐 Software"],
                            "resposta":"1"
                        },
                        {
                            "pergunta":"Classifique como  Hardware ou Software\n"
                            "A Impressora 🖨️ é um exemplo de = ________:",
                            "alternativas":["🖥️  Hardware","🌐 Software"],
                            "resposta":"0"
                        },
                        {
                            "pergunta":"O mouse 🖱️ é um exemplo de ____________________",
                            "alternativas":["🖥️  Hardware","🌐 Software"],
                            "resposta":"0"

                        },
                        {
                            "pergunta":"O aplicativo WhatsApp 📱 no celular é um ____________________",
                            "alternativas":["🖥️  Hardware","🌐 Software"],
                            "resposta":"1"

                        },
                        ]
                    },
                    "Segurança Digital":{
                    "texto":"Na internet, é importante pensar bem antes de compartilhar alguma coisa.\nAlgumas informações são seguras e podemos mostrar, como nossa cor favorita ou um bichinho de estimação 🐶.\nMas outras são muito pessoais e não devemos contar, como nossa senha 🔒 ou endereço 🏠.",
                    "exercício":[
                        {
                            "pergunta":"O que pode e o que não pode compartilhar na internet?\n"
                            "Uma foto de um animal de estimação 🐶:",
                            "alternativas":[
                                "🟢 Pode compartilhar",
                                "🔴 Não pode compartilhar"],
                            "resposta":"0"
                        },
                        {
                            "pergunta":"O que pode e o que não pode compartilhar na internet?\n"
                            "Seu nome completo ✋:",
                            "alternativas":[
                                "🟢 Pode compartilhar",
                                "🔴 Não pode compartilhar"],
                            "resposta":"1"
                        },
                        {
                            "pergunta":"O que pode e o que não pode compartilhar na internet?\n"
                            "Uma comida favorita 🍕:",
                            "alternativas":[
                                "🟢 Pode compartilhar",
                                "🔴 Não pode compartilhar"],
                            "resposta":"0"
                        },
                        {
                            "pergunta":"O que pode e o que não pode compartilhar na internet?\n"
                            "O nome da sua escola 🏫:",
                            "alternativas":[
                                "🟢 Pode compartilhar",
                                "🔴 Não pode compartilhar"],
                            "resposta":"1"
                        },
                        {
                            "pergunta":"O que pode e o que não pode compartilhar na internet?\n"
                            "A cor favorita 💙:",
                            "alternativas":[
                                "🟢 Pode compartilhar",
                                "🔴 Não pode compartilhar"],
                            "resposta":"0"
                        },
                    ]
                }
            },
            "9-10": {"Algoritmo com Condições: SE, ENTÃO":{
                     "texto":"Um algoritmo é uma sequência de passos para resolver um problema ou fazer uma tarefa. Às vezes, usamos a palavrinha mágica SE... ENTÃO... para decidir o que fazer em cada situação.\n"
                             "Por exemplo:"
                             "SE está chovendo, ENTÃO pego o guarda-chuva ☔."
                             "SE estou com fome, ENTÃO faço um lanche 🥪."
                             "\nÉ como tomar decisões com regras simples! ✅",
                     "exercício":[
                        {
                            "pergunta": "SE estiver frio, ENTÃO coloco o casaco.\nEstá frio hoje. O que acontece?",
                            "alternativas": ["a) Tira o casaco", "b) Não faz nada", "c) Coloca o casaco", "d) Vai para a praia"],
                            "resposta": "2"
                        },
                        {
                            "pergunta": "SE eu já almocei, ENTÃO posso comer sobremesa.\nAinda não almocei. O que acontece?",
                            "alternativas": ["a) Como a sobremesa", "b) Espero para comer depois", "c) Não como nada", "d) Janto"],
                            "resposta": "1"
                        },
                        {
                            "pergunta": "SE está chovendo, ENTÃO fico em casa.\nHoje não está chovendo. O que faço?",
                            "alternativas": ["a) Fico em casa", "b) Saio para brincar", "c) Tomo banho de chuva", "d) Volto a dormir"],
                            "resposta": "1"
                        },
                        {
                            "pergunta": "SE a previsão é de chuva, ENTÃO levo guarda-chuva.\nA previsão é de sol. O que faço?",
                            "alternativas": ["a) Levo o guarda-chuva", "b) Não levo o guarda-chuva", "c) Fico em casa", "d) Uso casaco"],
                            "resposta": "1"
                        },
                        {
                            "pergunta": "SE são 21h ou mais, ENTÃO é hora de dormir.\nAgora são 22h. O que devo fazer?",
                            "alternativas": ["a) Brincar mais um pouco", "b) Ver TV", "c) Dormir", "d) Comer doce"],
                            "resposta": "2"
                        }
                    ]
                },
                    "Lógica Computacional":{
                    "texto":"Lógica computacional é como ensinar o computador a tomar decisões, usando as palavras -verdadeiro- e -falso-.\n"

                            "Usamos palavrinhas como:\n"

                            "E → as duas coisas precisam ser verdadeiras.\n"
                            "👉 Exemplo: Está sol E é sábado → Podemos ir ao parque!\n"

                            "OU → só uma das coisas precisa ser verdadeira.\n"
                            "👉 Exemplo: Estou com fome OU é hora do lanche → Vou comer!\n"

                            "NÃO → muda o sentido da frase.\n"
                            "👉 Exemplo: NÃO está chovendo → Então posso sair sem guarda-chuva!",
                    "exercício":[
                        {
                            "pergunta":"Complete a Tabela Verdade\n"
                                        "'5 > 3' E '2 < 4?'= ?",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"0"
                        },
                        {
                            "pergunta":"Complete a Tabela Verdade\n"
                                        "'6 = 6' OU '7 < 2'= ?",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"0"
                        },
                        {
                            "pergunta":"Complete a Tabela Verdade\n"
                                        "'NÃO ( 4 > 2 )'",
                            "alternativas":["Verdadeiro! ✅","Falso! ❌"],
                            "resposta":"1"
                        },
                        {
                            "pergunta":"Complete a Tabela Verdade\n"
                            "A frase: 'Hoje está ensolarado' E 'Eu tenho um chapéu.'\n"
                            "Qual das alternativas 'NEGA' corretamente essa frase?",
                            "alternativas": [                                          
                                "a) Hoje NÃO está ensolarado OU eu NÃO tenho um chapéu.", 
                                "b) Hoje está ensolarado E eu tenho um chapéu.", 
                                "c) Hoje está ensolarado OU eu tenho um chapéu.", 
                                "d) Hoje NÃO está ensolarado E eu NÃO tenho um chapéu." 
                                             ],
                            "resposta": "0"
                        },
                        {
                            "pergunta":"Complete a Tabela Verdade\n"
                            "A frase: 'Eu comi o lanche' E 'Eu bebi suco.'\n"
                            "Qual das alternativas 'NEGA' corretamente essa frase?",
                            "alternativas": [
                                "a) Eu comi o lanche E bebi suco.", 
                                "b) Eu comi o lanche OU bebi suco.", 
                                "c) Eu NÃO comi o lanche OU eu NÃO bebi suco.", 
                                "d) Eu NÃO comi o lanche E NÃO bebi suco."
                                             ],
                            "resposta": "0"
                        },                        
                    ]
                },
                    "Avaliação de Fontes Confiáveis":{
                    "texto":"Quando lemos algo, precisamos verificar se a fonte (o site ou livro) é confiável. Se uma informação estiver errada, como um ano de nascimento ou um fato importante, podemos saber que não é confiável. Para isso, devemos buscar fontes que sejam bem conhecidas e que sempre tragam informações corretas.",
                    "exercício":[
                        {
                            "pergunta":"Fonte 1 (Site: Instituto de História Brasileira):\n"
                            "Monteiro Lobato nasceu em 18 de abril de 1882, em Taubaté (SP). Foi um dos mais importantes escritores da literatura infantil brasileira, criador do Sítio do Picapau Amarelo. Morreu em 4 de julho de 1948.\n"
                            "\nFonte 2 (Site: curiosidadesmentirosas.com.br ):\n"
                            "Monteiro Lobato nasceu em 1900 e escreveu livros infantis inspirados em desenhos animados. Morava no Rio de Janeiro e trabalhou com cinema.\n"
                            "\nQual fonte é confiavel?:",
                            "alternativas":[
                                "a) Fonte 1, porque as informações estão corretas e detalhadas.",
                                "b) Fonte 2, porque ela tem mais informações sobre o autor.",
                                "c) Nenhuma das fontes, pois ambas estão erradas em alguns detalhes.",
                                "d) Fonte 1, porque vem de um site conhecido e confiável."
                            ],
                            "resposta": "0"
                        },
                        {
                            "pergunta": "Por que é importante comparar informações de diferentes fontes?",
                            "alternativas": [
                                "a) Para descobrir se todo mundo está dizendo a mesma coisa.",
                                "b) Para escolher a informação mais legal.",
                                "c) Para ver se a informação está correta e verificar se é confiável.",
                                "d) Para encontrar a fonte que tenha mais imagens e vídeos interessantes."
                            ],
                            "resposta": "2"
                        },
                        {
                            "pergunta": "O que significa 'site confiável'?",
                            "alternativas": [
                                "a) Um site que tem informações verificadas e bem pesquisadas.",
                                "b) Um site com muitas cores e fontes legais.",
                                "c) Um site que fala sobre qualquer coisa.",
                                "d) Um site que tem conteúdo escrito por especialistas ou fontes reconhecidas."
                            ],
                            "resposta": "0"
                        },
                        {
                            "pergunta": "Como podemos saber se um site é confiável?",
                            "alternativas": [
                                "a) Buscando o nome do site nas redes sociais.",
                                "b) Acreditando no que o site diz, sem precisar verificar nada.",
                                "c) Checando se o site tem muitos anúncios e imagens coloridas.",
                                "d) Verificando se o site é feito por uma empresa ou instituição conhecida e respeitada."
                            ],
                            "resposta": "3"
                        },
                        {
                            "pergunta": "Por que é importante sempre verificar as informações que encontramos na internet?",
                            "alternativas": [
                                "a) Porque nem tudo o que lemos é verdade, e algumas informações podem ser erradas ou falsas.",
                                "b) Porque a internet sempre tem a verdade absoluta.",
                                "c) Porque é divertido procurar informações na internet.",
                                "d) Porque é mais rápido acreditar em tudo o que encontramos."
                            ],
                            "resposta": "0"
                        },
                    ]
                }

            }
        }
}