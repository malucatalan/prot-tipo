from cores import colorir
import os

def limparTela():
    """limparTela limpa o terminal."""
    os.system('cls')
def mostrarTitulo(texto:str):
    """mostrarTitulo formata e imprime o texto como título no terminal."""
    limparTela()
    print(colorir("-" * 80, cor="magenta"))
    print(colorir(texto.center(80), cor="magenta", estilo="bold"))
    print(colorir("-" * 80, cor="magenta"))
    print()
def mostrarTextoLinhaQuebrada(texto, max_carac):
        """mostrarTextoLinhaQuebrada quebra a linha do texto
          a partir do número máximo de caracteres."""
        inicio = 0
        fim = max_carac
        while inicio < len(texto):
            print(texto[inicio:fim])
            inicio += max_carac
            fim += max_carac
