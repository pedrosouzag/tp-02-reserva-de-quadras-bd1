
-- 1. USUARIO
INSERT INTO USUARIO (CPF, PRIMEIRO_NOME, SOBRENOME, EMAIL, DATA_NASC) VALUES
 ('46258753906','Ana','Silva','ana.silva@ufop.edu.br','1980-03-10'),              -- administradora
 ('91557412073','Bruno','Costa','bruno.costa@ufop.edu.br','1990-07-22'),          -- funcionario (Ouro Preto)
 ('68514753835','Carla','Mendes','carla.mendes@ufop.edu.br','1988-11-02'),        -- funcionaria (Ouro Preto)
 ('06973133525','Diego','Lima','diego.lima@aluno.ufop.edu.br','2004-05-30'),      -- aluno
 ('63815374855','Elisa','Rocha','elisa.rocha@aluno.ufop.edu.br','2003-01-15'),    -- aluna
 ('01849787778','Felipe','Alves','felipe.alves@aluno.ufop.edu.br','2005-09-08'),  -- aluno
 ('09247413338','Gabi','Souza','gabi.souza@aluno.ufop.edu.br','2004-12-20'),      -- aluna
 ('27861542866','Hugo','Pereira','hugo.pereira@ufop.edu.br','1985-06-14'),        -- funcionario (Mariana)
 ('55956348712','Iara','Martins','iara.martins@aluno.ufop.edu.br','2005-02-11'),  -- aluna (Mariana)
 ('76673084626','Julia','Ferreira','julia.ferreira@ufop.edu.br','1992-04-18');    -- funcionaria (Joao Monlevade)

-- 2. TELEFONE_USUARIO
INSERT INTO TELEFONE_USUARIO (CPF, TELEFONE) VALUES
 ('06973133525','31999990001'),
 ('06973133525','31988880001'),
 ('63815374855','31999990002'),
 ('55956348712','31999990009');

-- 3. RESPONSAVEL
--    1 = Diego, 2 = Elisa, 3 = Atletica, 4 = DCE, 5 = Iara
INSERT INTO RESPONSAVEL DEFAULT VALUES;
INSERT INTO RESPONSAVEL DEFAULT VALUES;
INSERT INTO RESPONSAVEL DEFAULT VALUES;
INSERT INTO RESPONSAVEL DEFAULT VALUES;
INSERT INTO RESPONSAVEL DEFAULT VALUES;

-- 4. ADMINISTRADOR
INSERT INTO ADMINISTRADOR (CPF, NIVEL_ACESSO) VALUES
 ('46258753906','total');

-- 5. FUNCIONARIO
INSERT INTO FUNCIONARIO (CPF, COD_FUNCIONARIO, TURNO, CPF_ADMINISTRADOR) VALUES
 ('91557412073','F001','manha','46258753906'),   -- Ouro Preto
 ('68514753835','F002','tarde','46258753906'),   -- Ouro Preto
 ('27861542866','F003','noite','46258753906'),   -- Mariana
 ('76673084626','F004','manha','46258753906');   -- Joao Monlevade

-- 6. USUARIO_COMUM
INSERT INTO USUARIO_COMUM (CPF, ID_RESPONSAVEL) VALUES
 ('06973133525',1),
 ('63815374855',2),
 ('01849787778',NULL),
 ('09247413338',NULL),
 ('55956348712',5);

-- 7. CURSO
INSERT INTO CURSO (COD_CURSO, NOME) VALUES
 ('CCO','Ciencia da Computacao'),
 ('SIN','Sistemas de Informacao'),
 ('ENC','Engenharia de Controle e Automacao'),
 ('JOR','Jornalismo');

-- 8. MATRICULA
INSERT INTO MATRICULA (CPF_ALUNO, COD_CURSO, NUM_MATRICULA, DATA_INGRESSO, SITUACAO) VALUES
 ('06973133525','CCO','2210001','2022-03-01','ativa'),
 ('63815374855','SIN','2110002','2021-03-01','ativa'),
 ('01849787778','ENC','2310003','2023-03-01','ativa'),
 ('09247413338','CCO','2210004','2022-03-01','inativa'),
 ('09247413338','SIN','2410005','2024-03-01','ativa'),   -- mudou de curso
 ('55956348712','JOR','2510006','2025-03-01','ativa');

-- 9. ORGANIZACAO
INSERT INTO ORGANIZACAO (NOME, ID_RESPONSAVEL) VALUES
 ('Atletica Computacao', 3),
 ('DCE UFOP', 4);

-- 10. TELEFONE_ORGANIZACAO
INSERT INTO TELEFONE_ORGANIZACAO (COD_ORG, TELEFONE) VALUES
 (1,'3135590001'),
 (2,'3135590002');

-- 11. CAMPUS
INSERT INTO CAMPUS (NOME, CIDADE) VALUES
 ('Morro do Cruzeiro','Ouro Preto'),
 ('ICEA','Joao Monlevade'),
 ('ICSA','Mariana');

-- 12. ESPACO_ESPORTIVO
INSERT INTO ESPACO_ESPORTIVO (NOME, CAPACIDADE, SITUACAO, COD_CAMPUS) VALUES
('Ginasio Poliesportivo', 200, 'disponivel', 1),  
 ('Quadra Externa',         50, 'disponivel', 1),  
 ('Campo de Futebol',      300, 'disponivel', 1),  
 ('Quadra ICEA',            80, 'disponivel', 2), 
 ('Quadra ICSA',            60, 'disponivel', 3);  

-- 13. QUADRA
INSERT INTO QUADRA (COD_ESPACO, TIPO_PISO, COBERTA) VALUES
 (1,'madeira',TRUE),
 (2,'cimento',FALSE),
 (4,'cimento',TRUE),
 (5,'cimento',FALSE);

-- 14. CAMPO
INSERT INTO CAMPO (COD_ESPACO, TIPO_GRAMADO) VALUES
 (3,'natural');

-- 15. MODALIDADE
INSERT INTO MODALIDADE (NOME) VALUES
 ('Futsal'),
 ('Volei'),
 ('Basquete'),
 ('Futebol');

-- 16. ESPACO_MODALIDADE
INSERT INTO ESPACO_MODALIDADE (COD_ESPACO, COD_MODALIDADE) VALUES
 (1,1),(1,2),(1,3),
 (2,1),(2,3),
 (3,4),
 (4,2),
 (5,1),(5,2);

-- 17. HORARIO_FUNCIONAMENTO
INSERT INTO HORARIO_FUNCIONAMENTO (COD_ESPACO, DATA, HORA_ABERTURA, HORA_FECHAMENTO, CPF_FUNCIONARIO) VALUES
 (1,'2026-11-24','08:00','12:00','91557412073'),
 (3,'2026-11-24','14:00','18:00','68514753835'),
 (5,'2026-11-24','18:00','22:00','27861542866'),
 (4,'2026-11-24','08:00','12:00','76673084626'),
 (1,'2026-11-25','08:00','12:00','91557412073');

-- 18. AGENDAMENTO
INSERT INTO AGENDAMENTO (STATUS, ID_RESPONSAVEL, COD_ESPACO, COD_MODALIDADE) VALUES
 ('confirmado', 1, 1, 1),   -- 1: Diego, futsal no ginasio
 ('confirmado', 3, 3, 4),   -- 2: Atletica, futebol no campo
 ('cancelado',  2, 1, 2),   -- 3: Elisa, volei no ginasio (cancelado)
 ('confirmado', 5, 5, 2),   -- 4: Iara, volei na quadra ICSA (Mariana)
 ('confirmado', 4, 4, 2);   -- 5: DCE, volei na quadra ICEA (Joao Monlevade)

-- 19. BLOCO_HORARIO
INSERT INTO BLOCO_HORARIO (COD_ESPACO, DATA, HORA_INICIO, HORA_FIM, COD_AGENDAMENTO) VALUES
 (1,'2026-11-24','08:00','09:00',1),
 (1,'2026-11-24','09:00','10:00',1),
 (1,'2026-11-24','10:00','11:00',NULL),
 (1,'2026-11-24','11:00','12:00',NULL),
 (3,'2026-11-24','14:00','15:00',2),
 (3,'2026-11-24','15:00','16:00',2),
 (3,'2026-11-24','16:00','17:00',NULL),
 (3,'2026-11-24','17:00','18:00',NULL),
 (5,'2026-11-24','18:00','19:00',4),
 (5,'2026-11-24','19:00','20:00',4),
 (5,'2026-11-24','20:00','21:00',NULL),
 (5,'2026-11-24','21:00','22:00',NULL),
 (4,'2026-11-24','08:00','09:00',5),
 (4,'2026-11-24','09:00','10:00',5),
 (4,'2026-11-24','10:00','11:00',NULL),
 (4,'2026-11-24','11:00','12:00',NULL),
 (1,'2026-11-25','08:00','09:00',NULL),
 (1,'2026-11-25','09:00','10:00',NULL),
 (1,'2026-11-25','10:00','11:00',NULL),
 (1,'2026-11-25','11:00','12:00',NULL);

-- 20. PARTICIPA
INSERT INTO PARTICIPA (CPF_ALUNO, COD_AGENDAMENTO) VALUES
 ('06973133525',1),('63815374855',1),('01849787778',1),
 ('01849787778',2),('09247413338',2),
 ('55956348712',4),('09247413338',4),
 ('06973133525',5),('01849787778',5);

-- 21. CANCELAMENTO
INSERT INTO CANCELAMENTO (COD_AGENDAMENTO, DATA_CANCELAMENTO, MOTIVO, CPF_USUARIO) VALUES
 (3,'2026-11-20','Aluna desistiu da reserva','63815374855');

-- 22. BLOQUEIO
INSERT INTO BLOQUEIO (INICIO, FIM, MOTIVO, CPF_FUNCIONARIO, COD_ESPACO) VALUES
 ('2026-11-24 08:00','2026-11-26 18:00','Manutencao do piso','91557412073',2),
 ('2026-11-28 08:00','2026-11-28 12:00','Evento institucional','27861542866',5);

-- 23. CHAMADO_SUPORTE
INSERT INTO CHAMADO_SUPORTE (DESCRICAO, DATA_ABERTURA, STATUS, CPF_USUARIO, CPF_FUNCIONARIO) VALUES
 ('Nao consigo cancelar minha reserva','2026-11-21','resolvido','63815374855','91557412073'),
 ('Erro ao ver agenda do campo','2026-11-23','aberto','01849787778',NULL),
 ('Quadra ICSA sem iluminacao','2026-11-22','em andamento','55956348712','27861542866'),
 ('Rede de volei rasgada na quadra ICEA','2026-11-23','aberto','06973133525','76673084626');

