from cores import colorir
import time
from texto_menu_sobre import TEXTOSOBRE
from conteudos import CONTEUDOS
import questionary
from prompt_toolkit.styles import Style
from func_secundarias import limparTela, mostrarTextoLinhaQuebrada, mostrarTitulo

def selecaoMenuIdades():
    """selecaoMenuIdades solicita a seleção da faixa etária."""
    estilo = Style([
        ('pointer', 'fg:ansimagenta bold'),
        ('question', 'fg:ansiblue bold'),
        ('highlighted', 'fg:ansibrightred bold')])
    
    escolha= questionary.select(
    " Selecione a faixa etária",
    choices=[
        questionary.Choice(
            title=[('fg:ansigreen nobold', '5-6 anos')], 
            value='1'
        ),
        questionary.Choice(
            title=[('fg:ansiyellow nobold','7-8 anos')],
            value='2'
        ),
        questionary.Choice(
            title=[('fg:ansicyan nobold', '9-10 anos')],
            value='3'
        ),
        questionary.Choice(
            title=[('fg:ansired nobold', 'Sair')],
            value='0'
        ),],instruction=" ",qmark=" ",style=estilo).ask()
    
    return escolha
def menuPrincipal():
    """menuPrincipal apresenta a parte inicial do programa."""
    mostrarTitulo('''
   _____ ____  _____  ______   ______    _____ ____  _   _ _______       
  / ____/ __ \|  __ \|  ____| |  ____|  / ____/ __ \| \ | |__   __|/\    
 | |   | |  | | |  | | |__    | |__    | |   | |  | |  \| |  | |  /  \   
 | |   | |  | | |  | |  __|   |  __|   | |   | |  | | . ` |  | | / /\ \  
 | |____ |__| | |__| | |____  | |____  | |____ |__| | |\  |  | |/ ____ \ 
  \_____\____/|_____/|______| |______|  \_____\____/|_| \_|  |_/_/    \_|
                                                                         
                                                                         
''')
    estilo = Style([
        ('pointer', 'fg:ansimagenta bold'),
        ('highlighted', 'fg:ansibrightred bold')])
        
    escolha= questionary.select(
    " ",
    choices=[
        questionary.Choice(
            title=[('fg:ansiblue nobold', 'Matemática')], 
            value='1'
        ),
        questionary.Choice(
            title=[('fg:ansigreen nobold','Informática')],
            value='2'
        ),
        questionary.Choice(
            title=[('fg:ansiyellow nobold', 'Sobre o Sistema')],
            value='3'
        ),
        questionary.Choice(
            title=[('fg:ansired nobold', 'Sair')],
            value='0'
        ),],instruction=" ",qmark=" ",style=estilo).ask()
    
    return escolha  
def menuMatematica():
    """menuMatematica gerencia quais conteúdos serão apresentados,
     de acordo com a faixa etária selecionada."""
    
    while True:
        mostrarTitulo("MATEMÁTICA DIVERTIDA")
        opcao=selecaoMenuIdades()

        if opcao == "1":
            menuConteudosExercicios("matematica", "5-6")
        elif opcao == "2":
            menuConteudosExercicios("matematica", "7-8")
        elif opcao == "3":
            menuConteudosExercicios("matematica", "9-10")
        elif opcao == "0":
            main()
def menuInformatica():
    """menuInformatica gerencia quais conteúdos serão apresentados,
     de acordo com a faixa etária selecionada."""
    
    while True:
        mostrarTitulo("INFORMÁTICA DIVERTIDA")
        opcao = selecaoMenuIdades()

         
        if opcao == "1":
            menuConteudosExercicios("informatica", "5-6")
        elif opcao == "2":
            menuConteudosExercicios("informatica", "7-8")
        elif opcao == "3":
            menuConteudosExercicios("informatica", "9-10")
        elif opcao == "0":
            main() 
def sobreSistema():
    """sobreSistema apresenta o sistema."""   

    def menuSobreSistema(indice_pagina):
        """menuSobreSistema recebe o indice da página atual e imprime o número da página. 
        Por fim, retorna as opções selecionadas."""

        estilo = Style([
        ('pointer', 'fg:ansimagenta bold'),
        ('highlighted', 'fg:ansibrightred bold')])

        ultima_pagina = len(conjunto_paragrafos)
        pagina_texto = indice_pagina + 1
        print()
        print(colorir(f"Página {pagina_texto} de {ultima_pagina}", cor="black", fundo="bg_white").center(92))

        if pagina_texto > 1:
            opcao = questionary.select(
        " ",
        choices=[
            questionary.Choice(
                title=[('fg:ansigreen nobold', 'Próxima Página')], 
                value=''
            ),
            questionary.Choice(
                title=[('fg:ansiyellow nobold', 'Anterior')], 
                value='1'
            ),
            questionary.Choice(
                title=[('fg:ansired nobold','Sair')],
                value='0'
            ),
        ],instruction=" ",qmark=" ",style=estilo).ask()
        else:
            opcao = questionary.select(
        " ",
        choices=[
            questionary.Choice(
                title=[('fg:ansigreen nobold', 'Próxima Página')], 
                value=''
            ),
            questionary.Choice(
                title=[('fg:ansired nobold','Sair')],
                value='0'
            ),
            
        ],instruction=" ",qmark=" ",style=estilo).ask()
        return opcao
    def paginar(paragrafos:list[str], indice_paragrafo=0):
        """paginar pagina cada parágrafo de um conjunto de Strings."""

        while indice_paragrafo < len(paragrafos):
            mostrarTitulo("Sobre o Sistema")
            mostrarTextoLinhaQuebrada(paragrafos[indice_paragrafo], 80)
            opcao = menuSobreSistema(indice_paragrafo)
            if opcao == '1' and indice_paragrafo > 0:
                paginar(paragrafos, indice_paragrafo - 1)
            elif opcao == "0":
                main()
                return
            indice_paragrafo += 1
    conjunto_paragrafos = list(TEXTOSOBRE)
    paginar(conjunto_paragrafos)
def menuConteudosExercicios(tema, idade):
   """menuConteudosExercicios solicita a modalidade de aprendizado."""

   while True:
        mostrarTitulo(f"{tema.upper()} PARA {idade} ANOS")
        estilo = Style([
        ('pointer', 'fg:ansimagenta bold'),
        ('highlighted', 'fg:ansibrightred bold')])
        
        escolha= questionary.select(
        " ",
        choices=[
            questionary.Choice(
                title=[('fg:ansigreen nobold', 'Ver Conteúdos')], 
                value='1'
            ),
            questionary.Choice(
                title=[('fg:ansiyellow nobold','Praticar Exercícios')],
                value='2'
            ),
            questionary.Choice(
                title=[('fg:ansired nobold', 'Sair')],
                value='0'
            ),],instruction=" ",qmark=" ",style=estilo).ask()
        
        if escolha == "1":
            mostrarConteudos(tema, idade)
        elif escolha == "2":
            mostrarExercicios(tema, idade)
        elif escolha  == "0":
            break
def apresentarConteudo(tema, idade, conteudo):
    """conteudoCompleto apresenta o conteúdo selecionado"""

    dadosConteudo = CONTEUDOS[tema][idade][conteudo]
    limparTela()
    mostrarTitulo(f"{conteudo.upper()}")
    print(colorir(dadosConteudo["texto"],cor="yellow"))
    print()
    input(colorir("Pressione Enter para voltar", cor="cyan"))
def mostrarConteudos(tema, idade):
    """verConteudos apresenta os conteúdos disponíveis."""

    while True:
        mostrarTitulo(f"CONTEÚDOS DE {tema.upper()} PARA {idade} ANOS")
        conteudos = list(CONTEUDOS[tema][idade].items())

        estilo_menu = Style([ 
            ('pointer', 'fg:ansimagenta bold'),
            ('question', 'fg:ansiyellow bold'), 
            ('highlighted', 'fg:ansibrightred bold')
        ])
        
        escolhas_para_menu = []
        cor_opcao_padrao = 'fg:ansicyan'

       
        for i, (nome_do_conteudo, _dados) in enumerate(conteudos):
            escolha = questionary.Choice(
                title=[(cor_opcao_padrao, nome_do_conteudo)], 
                value=str(i)  
            )
            escolhas_para_menu.append(escolha)
        
        
        escolhas_para_menu.append(
            questionary.Choice(
                title=[('fg:ansired', "Sair")], 
                value= "Sair" 
            )
        )
            
        opcao_valor = questionary.select(
            "Escolha um conteúdo:", 
            choices=escolhas_para_menu,
            style=estilo_menu,
            qmark=" ", 
            instruction=" " 
        ).ask()
        
        if opcao_valor == "Sair": 
            break 
        else:
            indice_selecionado = int(opcao_valor)
            nome_conteudo_escolhido = conteudos[indice_selecionado][0] 
            apresentarConteudo(tema, idade, nome_conteudo_escolhido)            
def mostrarExercicios(tema, idade):
    """mostrarExercicio apresenta os exercícios disponíveis."""

    while True:
        mostrarTitulo(f"EXERCÍCIOS DE {tema.upper()}")
        
        conteudosComexercício = list(CONTEUDOS[tema][idade].items())  

        estilo_menu = Style([ 
            ('pointer', 'fg:ansimagenta bold'),
            ('question', 'fg:ansiyellow bold'), 
            ('highlighted', 'fg:ansibrightred bold')
        ])

        escolhas_para_menu = []
        cor_opcao_padrao = 'fg:ansicyan'

        for j, (nome_do_conteudo, _) in enumerate(conteudosComexercício):
            escolha = questionary.Choice(
                title=[(cor_opcao_padrao, nome_do_conteudo)], 
                value=str(j)  
            )
            escolhas_para_menu.append(escolha)
        
        
        escolhas_para_menu.append(
            questionary.Choice(
                title=[('fg:ansired', "Sair")], 
                value= "Sair" 
            )
        )
            
        opcao_valor = questionary.select(
            "Escolha um conteúdo:", 
            choices=escolhas_para_menu,
            style=estilo_menu,
            qmark=" ", 
            instruction=" " 
        ).ask()
        
        if opcao_valor == "Sair": 
            break 
        else:
            indice_selecionado = int(opcao_valor)
            nome_conteudo_escolhido = conteudosComexercício[indice_selecionado][0] 
            praticarExercicio(tema, idade, nome_conteudo_escolhido)     
def praticarExercicio(tema, idade, nome_do_conteudo):
    """praticarExercicio gerencia o exercício selecionado."""

    estilo_menu = Style([ 
            ('pointer', 'fg:ansimagenta bold'),
            ('question', 'fg:ansiyellow bold'), 
            ('highlighted', 'fg:ansibrightred bold')
        ])
    cor = 'fg:ansicyan'

    exercicios_lista = CONTEUDOS[tema][idade][nome_do_conteudo]["exercício"]
    
    mostrarTitulo(f"EXERCÍCIOS: {nome_do_conteudo.upper()}")
    
    quantidade_acertos = 0
    quantidade_erros = 0
    
    for i, exercicio in enumerate(exercicios_lista, 1):
        limparTela()
        mostrarTitulo(f"EXERCÍCIO {i} de {len(exercicios_lista)}: {nome_do_conteudo.upper()}")
        print()
        print(colorir(f"Exercício {i}: {exercicio['pergunta']}", cor="yellow"))
        print()

        alternativas=[]

        for j, texto_alternativa in enumerate(exercicio['alternativas']):
            escolha = questionary.Choice(
                title=[(cor, texto_alternativa)], 
                value=str(j)  
            )
            alternativas.append(escolha)
            
        resposta = questionary.select(
            " ", 
            choices=alternativas,
            style=estilo_menu,
            qmark=" ", 
            instruction=" " 
        ).ask()

        
        
        if resposta == exercicio["resposta"]:
            print(colorir("Correto!", cor="green"))
            quantidade_acertos += 1 
        else:
            resposta_correta = int(exercicio["resposta"])
            texto_resposta_correta=exercicio['alternativas'][resposta_correta]
            quantidade_erros += 1
            print(colorir(f"Errado. A Resposta era : {texto_resposta_correta}", cor="red"))
        
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

