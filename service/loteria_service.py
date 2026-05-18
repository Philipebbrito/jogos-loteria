import random
from model.jogo import Jogo

JOGOS = {
    1: Jogo("MEGASENA",   60,  6),
    2: Jogo("QUINA",      80,  5),
    3: Jogo("LOTOFÁCIL",  25, 15),
    4: Jogo("MILIONÁRIA", 50,  6),
}

def obter_jogo(opcao: int) -> Jogo | None:
    return JOGOS.get(opcao)

def gerar_numeros(jogo: Jogo) -> list[int]:
    numeros = random.sample(range(1, jogo.limite + 1), jogo.palpites)
    return sorted(numeros)

def gerar_multiplos_jogos(jogo: Jogo, quantidade: int) -> list[list[int]]:
    return [gerar_numeros(jogo) for _ in range(quantidade)]