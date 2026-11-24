import psycopg2

import conexao
import operacoes

conn = conexao.conectar()

while True:
    print("\n===== SISTEMA DE ALOCACAO DE QUADRAS - UFOP =====")
    print("1 - Horarios livres de um espaco em uma data")
    print("2 - Agendamentos de um aluno")
    print("3 - Espacos por modalidade")
    print("4 - Historico de matriculas de um aluno")
    print("5 - Mudar situacao de um espaco")
    print("6 - Remover agendamento")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "0":
        print("Saindo...")
        break

    if opcao not in ("1", "2", "3", "4", "5", "6"):
        print("Opcao invalida!")
        continue

    print("(digite 0 em qualquer campo para voltar ao menu)")
    try:
        if opcao == "1":
            operacoes.horarios_livres_data(conn)
        elif opcao == "2":
            operacoes.agendamentos_de_um_aluno(conn)
        elif opcao == "3":
            operacoes.espacos_por_modalidades(conn)
        elif opcao == "4":
            operacoes.historico_matriculas(conn)
        elif opcao == "5":
            operacoes.mudar_situacao_espaco(conn)
        elif opcao == "6":
            operacoes.remover_agendamento(conn)
        input("\nPressione Enter para voltar ao menu...")
    except operacoes.Voltar:
        # usuario digitou 0: desfaz qualquer coisa pela metade e volta ao menu
        conn.rollback()
        print("Voltando ao menu...")
    except psycopg2.Error as erro:
        # erro do banco (ex: data invalida): desfaz e continua no menu
        conn.rollback()
        print(f"\nErro no banco: {erro}")
        input("Pressione Enter para voltar ao menu...")

conn.close()
