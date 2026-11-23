
-- 1. USUARIO: toda pessoa cadastrada no sistema
--    (superclasse de USUARIO_COMUM, FUNCIONARIO e ADMINISTRADOR)
CREATE TABLE USUARIO(

);

-- 2. TELEFONE_USUARIO: telefones do usuário (atributo multivalorado)
CREATE TABLE TELEFONE_USUARIO(

);

-- 3. RESPONSAVEL: quem realiza um agendamento (união de USUARIO_COMUM e ORGANIZACAO, com chave própria)
CREATE TABLE RESPONSAVEL(


);

-- 4. ADMINISTRADOR: subclasse de USUARIO. Gerencia os funcionários
CREATE TABLE ADMINISTRADOR(

);


-- 5. FUNCIONARIO: subclasse de USUARIO. Administra a agenda dos espaços (gerenciado por um ADMINISTRADOR)
CREATE TABLE FUNCIONARIO(


);

-- 6. USUARIO_COMUM: subclasse de USUARIO. Aluno que reserva e participa (pode ser um RESPONSAVEL)
CREATE TABLE USUARIO_COMUM(


);


-- 7. CURSO: curso de graduação da UFOP
CREATE TABLE CURSO(


);

-- 8. MATRICULA: relacionamento M:N entre USUARIO_COMUM e CURSO
--    (Num_Matricula, Data_Ingresso e Situacao ficam no relacionamento)
CREATE TABLE MATRICULA(


);

-- 9. ORGANIZACAO: atlética, DCE, centro acadêmico, departamento (pode ser um RESPONSAVEL)
CREATE TABLE ORGANIZACAO(


);

-- 10. TELEFONE_ORGANIZACAO: telefones da organização (multivalorado)
CREATE TABLE TELEFONE_ORGANIZACAO(


);

-- 11. CAMPUS: unidade da UFOP onde ficam os espaços esportivos
CREATE TABLE CAMPUS(


);

-- 12. ESPACO_ESPORTIVO: local disponível para reserva (superclasse de QUADRA e CAMPO). Fica em um CAMPUS
CREATE TABLE ESPACO_ESPORTIVO(


);

-- 13. QUADRA: subclasse de ESPACO_ESPORTIVO
CREATE TABLE QUADRA(


);

-- 14. CAMPO: subclasse de ESPACO_ESPORTIVO
CREATE TABLE CAMPO(


);


-- 15. MODALIDADE: esporte que pode ser praticado nos espaços
CREATE TABLE MODALIDADE(


);

-- 16. ESPACO_MODALIDADE: relacionamento M:N SUPORTA entre ESPACO_ESPORTIVO e
--     MODALIDADE (representa a agregação reservada pelos agendamentos)
CREATE TABLE ESPACO_MODALIDADE(



);



-- 17. HORARIO_FUNCIONAMENTO: entidade fraca de ESPACO_ESPORTIVO
--     (o funcionário abre o espaço em uma data; chave = espaço + data)
CREATE TABLE HORARIO_FUNCIONAMENTO(


);


-- 18. AGENDAMENTO: reserva de um par espaço-modalidade feita por um RESPONSAVEL
CREATE TABLE AGENDAMENTO(



);


-- 19. BLOCO_HORARIO: entidade fraca de HORARIO_FUNCIONAMENTO
--     (blocos de 1 hora; chave = espaço + data + hora de início;
--      cada bloco é ocupado por no máximo um AGENDAMENTO)
CREATE TABLE BLOCO_HORARIO(


);


-- 20. PARTICIPA: relacionamento M:N entre USUARIO_COMUM e AGENDAMENTO
CREATE TABLE PARTICIPA(


);

-- 21. CANCELAMENTO: subclasse de AGENDAMENTO (agendamentos cancelados)
--     (registra quem cancelou, a data e o motivo)
CREATE TABLE CANCELAMENTO(


);


-- 22. BLOQUEIO: período em que um espaço fica indisponível
--     (registrado por um FUNCIONARIO)
CREATE TABLE BLOQUEIO(



);


-- 23. CHAMADO_SUPORTE: pedido de ajuda aberto por um USUARIO
--     (pode ser atendido por um FUNCIONARIO)
CREATE TABLE CHAMADO_SUPORTE(




);
