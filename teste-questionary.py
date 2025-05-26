import questionary

def arrowkey(opcoes):
    acao = questionary.select(
        "Escolha uma das opções:",
        choices=opcoes
    ).ask()

    
opcoes=["hei","hello","como vai?"]

arrowkey(opcoes)

    