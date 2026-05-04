from colorama import Fore, Style

# Lista para armazenar os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)",
]


def definir_cor(nivel):
    """Função responsável por definir a cor da mensagem conforme o nível informado."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE


# Valor definido no código — simula o nível atual do reservatório (1 a 5)
nivel_atual = 2

# Exibe a situação atual do reservatório com a cor correspondente
cor = definir_cor(nivel_atual)
print(cor + niveis[nivel_atual - 1])

# Restaura o estilo padrão do terminal após a exibição
print(Style.RESET_ALL)
