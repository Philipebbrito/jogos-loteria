from service import loteria_service
from view import loteria_view

def main():
    loteria_view.exibir_cabecalho()

    while True:
        loteria_view.exibir_menu()

        opcao = loteria_view.ler_opcao_jogo()
        jogo = loteria_service.obter_jogo(opcao)

        if jogo is None:
            loteria_view.exibir_erro("OPÇÃO INVÁLIDA")
            continue

        quantidade = loteria_view.ler_quantidade_jogos()
        if quantidade <= 0:
            loteria_view.exibir_erro("QUANTIDADE INVÁLIDA")
            continue

        jogos_gerados = loteria_service.gerar_multiplos_jogos(jogo, quantidade)
        loteria_view.exibir_jogos(jogo.nome, jogos_gerados)

        if not loteria_view.perguntar_continuar():
            break

    loteria_view.exibir_encerramento()

if __name__ == "__main__":
    main()