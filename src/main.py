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

    opcao = input("Escolha uma opcao: ")

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
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opcao invalida!")

conn.close()
