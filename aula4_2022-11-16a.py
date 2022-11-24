import sqlite3

conexao = sqlite3.connect("dc_universe.db")

cursor = conexao.cursor()

#Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#Executar o comando SQL no SQLlite (no cursor)
cursor.execute(sql)

#Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")