"""OPERACOES DE CONSULTAS"""

"""consulta 1: mostra os blocos de horario livres de um espaco em uma data"""
def horarios_livres_data(conn):
    # pede o codigo do espaco e a data para o usuario
    espaco = input("Codigo do espaco: ")
    data = input("Data (AAAA-MM-DD): ")

    # o cursor e quem executa o sql no banco
    cur = conn.cursor()

    # bloco sem agendamento (COD_AGENDAMENTO IS NULL) = horario livre
    # o join com o espaco_esportivo e so para pegar o nome do espaco
    cur.execute("""
        SELECT ESPC.NOME, BH.DATA, BH.HORA_INICIO, BH.HORA_FIM
          FROM BLOCO_HORARIO BH
          JOIN ESPACO_ESPORTIVO ESPC ON ESPC.COD_ESPACO = BH.COD_ESPACO
          WHERE BH.COD_ESPACO = %s AND BH.DATA = %s AND BH.COD_AGENDAMENTO IS NULL
          ORDER BY BH.HORA_INICIO

    """, (espaco, data))

    linhas = cur.fetchall()

    # se a lista vier vazia, nao tem horario livre
    if not linhas:
        print("Nenhum horario livre para esse espaco nessa data.")
    else:
        print("\nHorarios livres:")
        for nome_Espaco, data_Bloco, inicio, fim in linhas:
            # strftime formata a data como 24/11/2026 e a hora como 08:00
            print(f"  {nome_Espaco} - {data_Bloco.strftime('%d/%m/%Y')} - "
                  f"{inicio.strftime('%H:%M')} as {fim.strftime('%H:%M')}")

    cur.close()



"""consulta 2: mostra os agendamentos de que um aluno participa"""
def agendamentos_de_um_aluno(conn):
    # o cpf eh digitado so com numeros
    cpf = input("Digite o CPF do aluno(apenas numeros) para consultar os agendamentos:")
    cur = conn.cursor()

    # parte da participa (onde esta o cpf) e junta o usuario (nome), o agendamento,
    # o espaco, a modalidade e o bloco de horario (data e hora)
    # cada join cola as linhas de outra tabela usando a chave estrangeira
    # o where deixa so as linhas do aluno digitado
    cur.execute("""
        SELECT USU.PRIMEIRO_NOME, USU.SOBRENOME, AGD.COD_AGENDAMENTO, ESPC.NOME, MOD.NOME, BH.DATA, BH.HORA_INICIO, BH.HORA_FIM, AGD.STATUS
          FROM PARTICIPA PART
          JOIN USUARIO USU ON USU.CPF = PART.CPF_ALUNO
          JOIN AGENDAMENTO AGD ON AGD.COD_AGENDAMENTO = PART.COD_AGENDAMENTO
          JOIN ESPACO_ESPORTIVO ESPC ON ESPC.COD_ESPACO = AGD.COD_ESPACO
          JOIN MODALIDADE  MOD ON MOD.COD_MODALIDADE = AGD.COD_MODALIDADE
          JOIN BLOCO_HORARIO BH ON BH.COD_AGENDAMENTO = AGD.COD_AGENDAMENTO
          WHERE PART.CPF_ALUNO = %s
          ORDER BY BH.DATA, BH.HORA_INICIO
    """, [cpf])

    linhas = cur.fetchall()

    if not linhas:
        print("Esse aluno nao possui agendamentos")
    else:
        print(f"\nCPF consultado: {cpf}")
        for nome, sobrenome, cod_Agendamento, nome_Espaco, nome_Modalidade, data, inicio, fim, status in linhas:
            # strftime formata a data como 24/11/2026 e a hora como 08:00
            print(f" {nome} {sobrenome} - #{cod_Agendamento} - {nome_Espaco} - {nome_Modalidade} - "
                  f"{data.strftime('%d/%m/%Y')} das {inicio.strftime('%H:%M')} as {fim.strftime('%H:%M')} - {status}")

    cur.close()


"""consulta 3: mostra os espacos que oferecem uma modalidade"""
def espacos_por_modalidades(conn):
    modalidade = input("Digite o nome da modalidade (ex: futsal, volei): ")
    cur = conn.cursor()

    # parte da espaco_modalidade (ponte entre espaco e modalidade)
    # junta a modalidade para filtrar pelo nome, o espaco para os dados e o campus para o nome dele
    # ilike compara o texto sem ligar para maiuscula e minuscula
    cur.execute("""
        SELECT ESPC.NOME, CAMP.NOME, ESPC.CAPACIDADE, ESPC.SITUACAO
          FROM ESPACO_MODALIDADE EM
          JOIN MODALIDADE MDL ON MDL.COD_MODALIDADE = EM.COD_MODALIDADE
          JOIN ESPACO_ESPORTIVO ESPC ON ESPC.COD_ESPACO = EM.COD_ESPACO
          JOIN CAMPUS CAMP ON CAMP.COD_CAMPUS = ESPC.COD_CAMPUS
          WHERE MDL.NOME ILIKE %s
          ORDER BY ESPC.NOME
    """, [modalidade])

    linhas = cur.fetchall()

    if not linhas:
        print("Nenhum espaco oferece essa modalidade.")
    else:
        print(f"\nEspacos que oferecem {modalidade}:")
        for nome_Espaco, nome_Campus, capacidade, situacao in linhas:
            print(f" {nome_Espaco} ({nome_Campus}) - capacidade {capacidade} - {situacao}")

    cur.close()

def historico_matriculas(conn):
    pass


"""OPERACAO DE UPDATE"""

def mudar_situacao_espaco(conn):
    pass


"""OPERACAO DELETE"""

def remover_agendamento (conn):
    pass
