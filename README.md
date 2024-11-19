# Projeto de Banco de Dados - Wide-Column Store

## Integrantes do Grupo

- Nome: Juan Caio Paronitti Galera
  - Matrícula: 22.122.067-6
- Nome: Murilo da Fonseca Guimarães
  - Matrícula: 22.122.079-1
- Nome: Rafael Leal Silva
  - Matrícula: 22.122.029-6
- Nome: Vitor Lucas Fujita Felício
  - Matrícula: 22.122.077-5
    

## Descrição

O projeto de Banco de Dados consiste na criação de um modelo de banco de dados do tipo Wide-column store, utilizando Cassandra, para ser usado por uma faculdade. Ele aborda diversos aspectos, desde a estruturação das tabelas até consultas.

## Para Executar o Código

1. Clone o repositório e baixe o arquivo "Import_data.py";

2. Crie uma conta no Astra DB (https://astra.datastax.com/);

3. Clique em "Database" → "Create Database". Lembre-se de escolher o servidor AWS;

4. Após criar a sua Database, clique no botão de "Connection Details", siga o passo-a-passo, alterando o código e token no início do "Import_data.py" pelo seu próprio código e token, lembre-se de não rodar o código em python ainda;
   
5. Retorne à tela da sua Database e clique no botão "CQL console", após isso copie o código em "create_tables.cql" e cole-o no "CQL console";

6. Inicie o programa "Import.py", após ele ter terminado você receberá uma mensagem de sucesso;

7. Execute as queries SQL para resolver problemas específicos:
   - **item 1:** Histórico escolar de qualquer aluno, retornando o código e nome da disciplina, semestre e ano que a disciplina foi cursada e nota final.
   - **item 2:** Histórico de disciplinas ministradas por qualquer professor, com semestre e ano (passe o ID do professor que deseja consultar).
   - **item 3:** Listar alunos que já se formaram (foram aprovados em todos os cursos de uma matriz curricular) em um determinado semestre de um ano.
   - **item 4:** Listar todos os professores que são chefes de departamento, junto com o nome do departamento.
   - **item 5:** Saber quais alunos formaram um grupo de TCC e qual professor foi o orientador.

### Informações Importantes
- O código do "**item 3:** Listar alunos que já se formaram (foram aprovados em todos os cursos de uma matriz curricular) em um determinado semestre de um ano." está mostrando todos os alunos que se formaram anteriormente ao ano de 2024, caso você queira saber de um ano em específico (Por estar randomizado) você pode realizar a ação a seguir:

1. Rodar o código
