# # =========================== POSTGRESQL ==============================

# import psycopg2

# try:
#     # Abrindo conexão
#     con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")

#     cur = con.cursor()

#     # Populando a tabela scripts
#     # cur.execute("insert into scripts(nome, conteudo) values('devops','projeto de python')")

#     # Atualizando o campo "nome" da tabela scripts
#     # cur.execute("update scripts set nome='devops_novo' where nome='devops'")
    
#     # Excluindo um registro
#     # cur.execute("delete from scripts where nome='devops_novo'")

#     # Mostrando todos os registros:
#     cur.execute("Select * from scripts")
#     print(cur.fetchall())

#     # Mostrando um registro:
#     # print(cur.fetchone())

#     con.commit()

#     print('Registro atualizado com sucesso')

# except Exception as e:

#     print(f'Erro: {e}')
#     print('Fazendo rollback')
#     con.rollback()

# finally:

#     print('Finalizando conexão com o banco de dados')
#     cur.close()
#     con.close()

# # =============================== MYSQL ====================================

# import MySQLdb

# try:

#     # Abrindo conexão
#     con = MySQLdb.connect(host="localhost", user="developer", passwd="4linux", db="projeto")

#     cur = con.cursor()

#     # Populando a tabela clientes 
#     # cur.execute("insert into clientes(nome, endereco) values ('novo_nome2', 'novo_endereco2')")
    
#     # Mostrando todos os dados da tabela
#     cur.execute("select * from clientes")
#     # print(cur.fetchall())

#     # Mostrando só um registro da tabela:
#     print(cur.fetchone())

#     con.commit()

#     print('Sucesso!')

# except Exception as e:

#     print(f'Erro: {e}')
#     con.rollback()

# finally:

#     print('Finalizando conexão...')
#     cur.close()
#     con.close()

# ================================ MONGODB ================================

from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']

def inserir_dado():

    try:

        # db.fila.insert é um comando do próprio mongo, que é reconhecido aqui após a importação que fizemos
        db.fila.insert({"_id":200,
                        "empresa":"4Linux",
                        "cursos":[{
                                   "nome":"Python Fundamentals",
                                   "carga horaria":40
                                  },
                                  {
                                    "nome":"Linux Fundamentals",
                                    "carga horaria":40
                                   }]
                        })

    except Exception as e:

        print(f"Erro: {e}")

def buscar_dados():

    for r in db.fila.find():

        print(f'Empresa: {r["empresa"]}')

        for c in r["cursos"]:

            print('---------------------')
            print(f'Nome: {c["nome"]}. Carga Horária: {c["carga horaria"]}')

        print('=========================')

buscar_dados()