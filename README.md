# Projeto-2---Wide-column-Store

Vinicius henrique Silva 22.122.063-5

Luan Petroucic Moreno 22.122.076-7

Caue Jacomini Zanatti 22.122.024-7

# Como convertemos os dados do projeto do semestre passado?

Usamos as bibliotecas do psycopg2 para podermos fazer selects do projeto passado e agregar as informações a inserts no banco de não relacional.

Caso queira verificar o código, é o createInserts.

# PRÉ-REQUISITOS:

Ter as bibliotecas PSYCOPG2 e CASSANDRA instaladas.
Além de estar rodando um docker local conectado no Cassandra.

docker pull cassandra:latest

docker run --name Projeto cassandra:latest

# DESCRIÇÃO DE USO:

1. Abrir a pasta Scripts Python e rodar o arquivo createDB.

Esse arquivo irá criar o keyspace e todas as tabelas que serão utilizadas.

2. Rodar o arquivo createInserts.

Esse arquivo irá pegar todos os dados do banco relacional desenvolvido no semestre passado e realizar a desetruturação dos dados, inserindo-os nas tabelas criadas no passo anterior.

3. Rodar os seguintes comandos para iniciar o shell cqlsh:
docker exec -it {nome_do_container} cqlsh *Substituir nome do container pelo nome do container criado na docker.

USE projetowidecolumn;

4. Abrir o selects.txt e roda-los no shell do cqlsh
