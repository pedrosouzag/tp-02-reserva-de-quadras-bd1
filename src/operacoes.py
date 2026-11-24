"""FUNCOES AUXILIARES"""

class Voltar(Exception):
    """lancada quando o usuario digita 0 para voltar ao menu"""


def ler(texto):
    # le uma entrada do usuario; se digitar 0, volta para o menu
    valor = input(f"{texto} (0 = voltar): ").strip()
    if valor == "0":
        raise Voltar
    return valor


"""OPERACOES DE CONSULTAS"""

"""consulta 1: mostra os blocos de horario livres de um espaco em uma data"""
def horarios_livres_data(conn):
    # pede o codigo do espaco e a data para o usuario
    espaco = ler("Codigo do espaco")
    data = ler("Data (AAAA-MM-DD)")

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
    cpf = ler("Digite o CPF do aluno (apenas numeros)")
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
    modalidade = ler("Digite o nome da modalidade (ex: futsal, volei)")
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

"""consulta 4: mostra o historico de matriculas (cursos) de um aluno"""
def historico_matriculas(conn):
    cpf = ler("Digite o CPF do aluno (apenas numeros)")
    cur = conn.cursor()

    # parte da matricula (relacionamento aluno-curso) e junta o curso (nome)
    # e o usuario (nome do aluno); ordena pela data de ingresso
    cur.execute("""
        SELECT USU.PRIMEIRO_NOME, USU.SOBRENOME, CUR.NOME, MAT.NUM_MATRICULA, MAT.DATA_INGRESSO, MAT.SITUACAO
          FROM MATRICULA MAT
          JOIN CURSO CUR ON CUR.COD_CURSO = MAT.COD_CURSO
          JOIN USUARIO USU ON USU.CPF = MAT.CPF_ALUNO
          WHERE MAT.CPF_ALUNO = %s
          ORDER BY MAT.DATA_INGRESSO
    """, [cpf])

    linhas = cur.fetchall()

    if not linhas:
        print("Nenhuma matricula encontrada para esse CPF.")
    else:
        nome, sobrenome = linhas[0][0], linhas[0][1]
        print(f"\nHistorico de matriculas de {nome} {sobrenome}:")
        for _, _, curso, num_Matricula, data_Ingresso, situacao in linhas:
            print(f"  {curso} - matricula {num_Matricula} - "
                  f"ingresso em {data_Ingresso.strftime('%d/%m/%Y')} - {situacao}")

    cur.close()


"""OPERACAO DE UPDATE"""

"""update: muda a situacao de um espaco (ex: disponivel -> manutencao)"""
def mudar_situacao_espaco(conn):
    cur = conn.cursor()

    # mostra os espacos para o usuario escolher
    cur.execute("SELECT COD_ESPACO, NOME, SITUACAO FROM ESPACO_ESPORTIVO ORDER BY COD_ESPACO")
    print("\nEspacos cadastrados:")
    for cod, nome, situacao in cur.fetchall():
        print(f"  {cod} - {nome} - {situacao}")

    espaco = ler("Codigo do espaco")
    nova = ler("Nova situacao (disponivel / manutencao / interditado)")

    cur.execute("""
        UPDATE ESPACO_ESPORTIVO
           SET SITUACAO = %s
         WHERE COD_ESPACO = %s
    """, (nova, espaco))

    # rowcount = quantas linhas o update alterou (0 = codigo nao existe)
    if cur.rowcount == 0:
        print("Nenhum espaco com esse codigo.")
        conn.rollback()
    else:
        conn.commit()
        print(f"Situacao do espaco {espaco} alterada para '{nova}'.")

    cur.close()


"""OPERACAO DELETE"""

"""delete: remove um agendamento
   PARTICIPA e CANCELAMENTO dele sao apagados em cascata (ON DELETE CASCADE)
   e os blocos de horario voltam a ficar livres (ON DELETE SET NULL)"""
def remover_agendamento (conn):
    cur = conn.cursor()

    # mostra os agendamentos para o usuario escolher
    cur.execute("""
        SELECT AGD.COD_AGENDAMENTO, ESPC.NOME, MDL.NOME, AGD.STATUS
          FROM AGENDAMENTO AGD
          JOIN ESPACO_ESPORTIVO ESPC ON ESPC.COD_ESPACO = AGD.COD_ESPACO
          JOIN MODALIDADE MDL ON MDL.COD_MODALIDADE = AGD.COD_MODALIDADE
          ORDER BY AGD.COD_AGENDAMENTO
    """)
    print("\nAgendamentos cadastrados:")
    for cod, espaco, modalidade, status in cur.fetchall():
        print(f"  #{cod} - {espaco} - {modalidade} - {status}")

    cod = ler("Codigo do agendamento a remover")
    confirma = ler(f"Confirma a remocao do agendamento #{cod}? (s/n)")
    if confirma.lower() != "s":
        print("Remocao cancelada.")
        cur.close()
        return

    # conta os blocos ocupados antes, para mostrar quantos foram liberados
    cur.execute("SELECT COUNT(*) FROM BLOCO_HORARIO WHERE COD_AGENDAMENTO = %s", [cod])
    blocos = cur.fetchone()[0]

    cur.execute("DELETE FROM AGENDAMENTO WHERE COD_AGENDAMENTO = %s", [cod])

    if cur.rowcount == 0:
        print("Nenhum agendamento com esse codigo.")
        conn.rollback()
    else:
        conn.commit()
        print(f"Agendamento #{cod} removido. {blocos} bloco(s) de horario liberado(s).")

    cur.close()
