def exibir_cabecalho():
    print("##### GERADOR DE PALPITES LOTERIA #####")

def exibir_menu():
    print("""
[ 1 ] - MEGASENA
[ 2 ] - QUINA
[ 3 ] - LOTOFÁCIL
[ 4 ] - MILIONÁRIA""")

def ler_opcao_jogo() -> int:
    try:
        return int(input("Tipo Jogo: "))
    except ValueError:
        return -1

def ler_quantidade_jogos() -> int:
    try:
        return int(input("Quantos palpites? "))
    except ValueError:
        return 0

def exibir_jogos(nome_jogo: str, jogos: list[list[int]]):
    print(f"-------------- {nome_jogo} --------------")
    for i, jogo in enumerate(jogos, start=1):
        print(f"Jogo {i}: {jogo}")
    print("----------------------------------------")

def perguntar_continuar() -> bool:
    resp = input("Deseja continuar [S / N]: ").strip().upper()
    if resp == "S":
        return True
    elif resp == "N":
        return False
    else:
        print("OPÇÃO INVÁLIDA!")
        return False

def exibir_encerramento():
    print("PROGRAMA ENCERRADO!!!")

def exibir_erro(mensagem: str):
    print(mensagem)