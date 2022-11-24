import sqlite3

conexao = sqlite3.connect("dc_universe.db")

cursor = conexao.cursor()

#Comando para inserir herois no BD
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

cursor.execute(sql)

conexao.commit()
conexao.close()