"""OPERACOES DE CONSULTAS"""

def horarios_livres_data(conn):
    espaco = input("Codigo do espaco: ")
    data = input("Data (AAAA-MM-DD): ")

    cur = conn.cursor()
    cur.execute("""
        SELECT HORA_INICIO, HORA_FIM
          FROM BLOCO_HORARIO
          WHERE COD_ESPACO = %s AND DATA = %s AND COD_AGENDAMENTO IS NULL
          ORDER BY HORA_INICIO

    """, (espaco, data))

    linhas = cur.fetchall()

    if not linhas:
        print("Nenhum horario livre para esse espaco nessa data.")
    else:
        print("\nHorarios livres:")
        for inicio, fim in linhas:
            print(f"  {inicio.strftime('%H:%M')} - {fim.strftime('%H:%M')}")

    cur.close()



def agendamentos_de_um_aluno(conn):
    cpf = input("Digite o CPF do aluno(apenas numeros) para consultar os agendamentos:")
    cur = conn.cursor()

    cur.execute("""
        SELECT AGD.COD_AGENDAMENTO, ESPC.NOME, MOD.NOME, AGD.STATUS
          FROM PARTICIPA PART
          JOIN AGENDAMENTO AGD ON AGD.COD_AGENDAMENTO = PART.COD_AGEDAMENTO
          JOIN ESPACO_ESPORTIVO ESPC ON ESPC.COD_ESPACO = AGD.COD_ESPACO
          JOIN MODALIDADE  MOD ON MOD.COD_MODALIDADE = AGD.COD_MODALIDADE
          WHERE PART.CPF_ALUNO = %s
          ORDER BY AGD.COD_AGENDAMENTO
    """, [cpf])

    linhas = cur.fetchall()

    if not linhas:
        print("Esse aluno nao possui agendamentos")


    print(f"\nAgendamentos para o CPF {cpf}")
    for cod_Agendamento, nome_Espaco, nome_Modalidade, status in linhas:
        print(f" #{cod_Agendamento} - {nome_Espaco} - {nome_Modalidade} - {status}")

    cur.close()


def espacos_por_modalidades(conn):
    pass

def historico_matriculas(conn):
    pass


"""OPERACAO DE UPDATE"""

def mudar_situacao_espaco(conn):
    pass


"""OPERACAO DELETE"""

def remover_agendamento (conn):
    pass