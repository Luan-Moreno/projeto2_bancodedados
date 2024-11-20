import connecting as con
from cassandra.cluster import Cluster

var = con.connection()

def insertAlunos():
    
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('projetowidecolumn')
    
    cur = var.cursor()
    cur.execute('SELECT a.id_alunos, a.nome_aluno , d.cod_disc ,d.nome_disc , c.cod_curso ,c.nome_curso ,ac.semestre ,ac.ano ,ac.nota  FROM aluno a join alunos_cursando ac on a.id_alunos = ac.id_aluno join disciplinas d  on d.cod_disc =ac.cod_disc join cursos c  on c.cod_curso = ac.id_curso ;')
    alunos_historico = cur.fetchall()
    
    for i in range(len(alunos_historico)):
        session.execute ( """
        INSERT INTO aluno_notas (id_aluno, nome_aluno, id_disciplina, nome_disciplina, id_curso, curso_nome, semestre, ano, nota)
        VALUES (%d,'%s',%d,'%s',%d,'%s',%d,%d,%d)""" % (alunos_historico[i][0], alunos_historico[i][1], alunos_historico[i][2], alunos_historico[i][3], alunos_historico[i][4], alunos_historico[i][5], alunos_historico[i][6], alunos_historico[i][7], alunos_historico[i][8])) 
    cluster.shutdown()
    
       
def insertProfessorDisc():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('projetowidecolumn')
    
    cur = var.cursor()
    cur.execute('select p.id_professor , p.nome_professor , d.cod_disc ,d.nome_disc , c.cod_curso ,c.nome_curso ,pa.semestre , pa.ano  from professor p join professor_aulas pa  on pa.id_professor = p.id_professor join disciplinas d  on d.cod_disc = pa.cod_disc join cursos c  on pa.id_curso = c.cod_curso;')
    professor_disc = cur.fetchall()
    
    for i in range(len(professor_disc)):
        session.execute("""
            INSERT INTO professor_aulas(id_professor, nome_professor, id_disciplina, nome_disciplinas, id_curso, curso_nome, semestre, ano)
            VALUES (%d, '%s', %d, '%s', %d, '%s', %d, %d)
        """ % (
            professor_disc[i][0],  
            professor_disc[i][1],  
            professor_disc[i][2],  
            professor_disc[i][3],  
            professor_disc[i][4],  
            professor_disc[i][5],  
            professor_disc[i][6],  
            professor_disc[i][7]
        ))

    cluster.shutdown()


def insertAlunosGraduados():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('projetowidecolumn')
    
    cur = var.cursor()
    cur.execute("""SELECT a.id_alunos ,a.nome_aluno,c.cod_curso ,c.nome_curso ,d.cod_disc ,d.nome_disc, ac.ano ,ac.semestre 
    FROM aluno a
    JOIN alunos_cursando ac ON ac.id_aluno = a.id_alunos
    JOIN disciplinas d ON d.cod_disc = ac.cod_disc
    JOIN cursos c ON c.cod_curso = ac.id_curso
    WHERE ac.id_aluno IN (
        SELECT AC.ID_ALUNO
        FROM alunos_cursando AC
        GROUP BY AC.ID_ALUNO
        HAVING MIN(AC.nota) >= 5
    );""")
    alunos_graduados = cur.fetchall()
    
    for i in range(len(alunos_graduados)):
        session.execute("""
        INSERT INTO alunos_graduados (id_aluno, nome_aluno, id_curso, nome_curso, id_disciplina, nome_disc, ano, semestre)
        VALUES (%d, '%s', %d, '%s', %d, '%s', %d, %d)""" % (alunos_graduados[i][0], alunos_graduados[i][1], alunos_graduados[i][4], alunos_graduados[i][5], alunos_graduados[i][2], alunos_graduados[i][3], alunos_graduados[i][6], alunos_graduados[i][7]))
    cluster.shutdown()

def insertDepartamento():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('projetowidecolumn')
    
    cur = var.cursor()
    cur.execute("""select p.id_professor , p.nome_professor , d.dep_id , d.nome_dep  from departamento d  join professor p  on d.chefe_dep_id = p.id_professor; 
                """)
    departamentos = cur.fetchall()
    
    for i in range(len(departamentos)):
        session.execute("""
        INSERT INTO departamento (id_professor,nome_professor,id_chefe_departamento,nome_chef_departamento)
        VALUES (%d, '%s', %d, '%s')""" % (departamentos[i][0] , departamentos[i][1] , departamentos[i][2], departamentos[i][3]))
    cluster.shutdown()
        
    
def insertTCC():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('projetowidecolumn')
    
    cur = var.cursor()
    cur.execute("""select at.id_tcc ,a.id_alunos ,a.nome_aluno ,p.id_professor ,p.nome_professor 
from alunos_tcc at join aluno a 
on a.id_alunos = at.id_aluno join professor p 
on p.id_professor = at.id_professor;
                """)
    tcc = cur.fetchall()
    
    for i in range(len(tcc)):
        session.execute("""
        INSERT INTO tccs (id_tcc,id_aluno,nome_aluno,id_professor,nome_professor)
        VALUES (%d, %d, '%s', %d, '%s')""" % (tcc[i][0] ,tcc[i][1] ,tcc[i][2] ,tcc[i][3] , tcc[i][4]))
    cluster.shutdown()
insertAlunos()
insertProfessorDisc()
insertAlunosGraduados()
insertDepartamento()
insertTCC()
