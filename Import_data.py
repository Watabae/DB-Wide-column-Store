from astrapy import DataAPIClient
import random
import uuid

# Inicializando o cliente do Astra DB
client = DataAPIClient("AstraCS:IYcXWMZfMNOzlZEEaPOiaLMo:9377c2adb39de34d087c68a00d1bfe246f2784dcb7fc04d177832ed9b787c2e4")
db = client.get_database_by_api_endpoint(
    "https://3f5fce31-d697-431b-827a-76bfbe7b09d6-us-east-2.apps.astra.datastax.com"
)

# Funções auxiliares
def random_year():
    return random.randint(2019, 2024)

def random_semester():
    return random.choice([1, 2])

def random_float():
    return round(random.uniform(0, 100), 2)

def random_choice(max_value):
    return random.randint(1, max_value)

# 1. Inserir alunos
alunos = []
for aluno_id in range(1, 11):
    nome_aluno = f"Aluno {aluno_id}"
    aluno_data = {
        'id_aluno': aluno_id,
        'nome': nome_aluno
    }
    alunos.append(aluno_data)

# Inserir os alunos em massa
db['alunos_historico'].insert_many(alunos)

# 2. Inserir professores
# Exemplo de inserção corrigida
professores = []
for professor_id in range(1, 6):
    nome_professor = f"Professor {professor_id}"
    
    # Para cada professor, inserimos várias disciplinas
    for disciplina_id in range(1, 9):
        disciplina_nome = f"Disciplina {disciplina_id}"
        semestre = random_semester()  # Semestre aleatório
        ano = random_year()  # Ano aleatório
        
        # Inserir os dados incluindo as duas colunas da chave primária: id_professor e id_disciplina
        professores.append({
            'id_professor': professor_id,
            'professor_nome': nome_professor,
            'id_disciplina': disciplina_id,
            'disciplina_nome': disciplina_nome,
            "semestre": semestre,
            "ano": ano
        })

# Inserção de todos os documentos de uma vez
db['professores_disciplinas'].insert_many(professores)

# 3. Inserir disciplinas
disciplinas = []
for professor_id in range(1, 6):
    for disciplina_id in range(1, 9):
        disciplina_nome = f"Disciplina {disciplina_id}"
        disciplina_data = {
            'id_professor': professor_id,
            'professor_nome': f"Professor {professor_id}",
            'id_disciplina': disciplina_id,
            'disciplina_nome': disciplina_nome
        }
        disciplinas.append(disciplina_data)

# Inserir as disciplinas em massa
db['professores_disciplinas'].insert_many(disciplinas)

# 4. Inserir departamentos, chefes e cursos
departamentos = []
for departamento_id in range(1, 4):
    nome_departamento = f"Departamento {departamento_id}"
    chefe_id = random_choice(5)  
    chefe_nome = f"Professor {chefe_id}"  

    departamentos.append({
        'id_departamento': departamento_id,
        'id_chefe_professor': chefe_id,
        'chefe_professor_nome': chefe_nome,  
        'nome': nome_departamento  
    })

# Inserir os departamentos
db['departamentos'].insert_many(departamentos)


# Inserir cursos e associá-los aos departamentos
cursos = []
for departamento_id in range(1, 4):
    for curso_id in range(1, 5):
        nome_curso = f"Curso {curso_id}"

        # Inserir apenas os dados correspondentes ao esquema
        cursos.append({
            'id_curso': curso_id,
            'id_departamento': departamento_id,
            'nome': nome_curso  # Nome do curso armazenado na coluna "nome"
        })

# Inserção de todos os cursos de uma vez
db['cursos'].insert_many(cursos)

# 5. Inserir matrizes curriculares
matrizes_curriculares = []
for curso_id in range(1, 5):
    for matriz_id in range(1, 3):
        matriz_data = {
            'id_curso': curso_id,
            'curso_nome': f"Curso {curso_id}",
            'id_matriz': matriz_id
        }
        matrizes_curriculares.append(matriz_data)

# Inserir matrizes curriculares em massa
db['matrizes_curriculares'].insert_many(matrizes_curriculares)

# 6. Inserir históricos escolares
historicos = []
for aluno_id in range(1, 11):
    for _ in range(random.randint(5, 10)):  # Cada aluno tem 5-10 históricos
        id_historico = str(uuid.uuid4())
        ano = random_year()
        semestre = random_semester()
        nota_final = random_float()
        disciplina_id = random_choice(8)
        disciplina_nome = f"Disciplina {disciplina_id}"
        professor_id = random_choice(5)
        professor_nome = f"Professor {professor_id}"

        historico_data = {
            'id_aluno': aluno_id,
            'id_historico': id_historico,
            'ano': ano,
            'semestre': semestre,
            'nota_final': nota_final,
            'id_disciplina': disciplina_id,
            'disciplina_nome': disciplina_nome,
            'id_professor': professor_id,
            'professor_nome': professor_nome
        }
        historicos.append(historico_data)

# Inserir os históricos em massa
db['alunos_historico'].insert_many(historicos)

# 7. Inserir grupos de TCC
grupos_tcc = []
for grupo_id in range(1, 6):
    tema = f"Tema {grupo_id}"
    aluno1_id = random_choice(10)
    aluno2_id = random_choice(10)
    professor_id = random_choice(5)
    professor_nome = f"Professor {professor_id}"
    
    grupo_data = {
        'id_grupo_tcc': str(uuid.uuid4()),
        'tema': tema,
        'id_aluno1': aluno1_id,
        'aluno1_nome': f"Aluno {aluno1_id}",
        'id_aluno2': aluno2_id,
        'aluno2_nome': f"Aluno {aluno2_id}",
        'id_professor': professor_id,
        'professor_nome': professor_nome
    }
    grupos_tcc.append(grupo_data)

# Inserir grupos de TCC em massa
db['grupos_tcc'].insert_many(grupos_tcc)

# Agora todos os dados foram inseridos em massa no banco de dados.
print("Dados inseridos com sucesso!")
