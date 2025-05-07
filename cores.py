def colorir(texto, cor=None, fundo=None, estilo=None, reset=True):
    cores = {
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'white': 37,
        'bg_black': 40,
        'bg_red': 41,
        'bg_green': 42,
        'bg_yellow': 43,
        'bg_blue': 44,
        'bg_magenta': 45,
        'bg_cyan': 46,
        'bg_white': 47
    }
    
    estilos = {
        'bold': 1,
        'dim': 2,
        'italic': 3,
        'underline': 4,
        'blink': 5,
        'reverse': 7
    }
    codigos = []
    if estilo and estilo in estilos:
        codigos.append(str(estilos[estilo]))
    
    if cor and cor in cores:
        codigos.append(str(cores[cor]))
    
    if fundo and fundo in cores:
        codigos.append(str(cores[fundo]))
    
    if codigos:
        texto_colorido = f"\033[{';'.join(codigos)}m{texto}"
        if reset:
            texto_colorido += "\033[0m"
        return texto_colorido
    
    return texto

# ============ EXEMPLOS DE USO ============
if __name__ == "__main__":
    # Exemplos de aplicação
    print(colorir("Mensagem normal"))
    print(colorir("Erro crítico", cor="red", estilo="bold"))
    print(colorir("Aviso importante", cor="yellow", fundo="bg_black"))
    print(colorir("Texto azul sublinhado", cor="blue", estilo="underline"))
    print(colorir("Fundo magenta com texto branco", cor="white", fundo="bg_magenta"))
    
    # Uso em um sistema
    def log_sucesso(mensagem):
        print(colorir("[✓] ", cor="green") + colorir(mensagem, cor="green", estilo="dim"))
    
    def log_erro(mensagem):
        print(colorir("[✗] ", cor="red", estilo="bold") + colorir(mensagem, cor="red"))
    
    def log_alerta(mensagem):
        print(colorir("[!] ", cor="yellow") + mensagem)
    
    log_sucesso("Operação concluída com sucesso!")
    log_erro("Falha na execução do módulo!")
    log_alerta("Recomendação: Verifique as configurações")