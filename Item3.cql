SELECT id_aluno, nome
FROM alunos_historico
WHERE ano = 2023 AND semestre = 2 AND nota_final >= 60
ALLOW FILTERING;
