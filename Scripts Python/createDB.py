from cassandra.cluster import Cluster

#Arquivo para se conectar ao cassandra e criar cluster,keyspace e tabelas.

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS projetowidecolumn 
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3}
""")

session.set_keyspace('projetowidecolumn')

session.execute("""
    CREATE TABLE IF NOT EXISTS aluno_notas (
        id_aluno int,
        nome_aluno TEXT,
        id_disciplina int,
        nome_disciplina TEXT,
        id_curso int,
        curso_nome TEXT,
        semestre int,
        ano int,
        nota int,
        PRIMARY KEY ((id_aluno),id_disciplina, semestre, ano , nota)
    ) 
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS professor_aulas (
        id_professor int,
        nome_professor TEXT,
        id_disciplina int,
        nome_disciplinas TEXT,
        id_curso int,
        curso_nome TEXT,
        semestre int,
        ano int,
        PRIMARY KEY ((id_professor),id_disciplina, semestre, ano)
    ) 
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS alunos_graduados (
        id_aluno int,
        nome_aluno TEXT,
        id_curso int,
        nome_curso TEXT,
        id_disciplina int,
        nome_disc TEXT,
        ano int,
        semestre int,
        PRIMARY KEY((id_aluno) , id_curso, id_disciplina)
    ) 
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS departamento (
        id_professor int,
        nome_professor TEXT,
        id_chefe_departamento int,
        nome_chef_departamento TEXT,
        PRIMARY KEY ((id_professor), id_chefe_departamento)
    ) 
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS tccs (
        id_tcc int,
        id_aluno int,
        nome_aluno TEXT,
        id_professor int,
        nome_professor TEXT,
        PRIMARY KEY ((id_tcc), id_aluno, id_professor)
    ) 
""")

cluster.shutdown()

print("Sucesso criando DB.")
