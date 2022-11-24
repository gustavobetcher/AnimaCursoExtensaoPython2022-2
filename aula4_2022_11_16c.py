#Importar bibiloteca sqlite
import sqlite3


#Função conectar()
def conectar():
  #Conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #Criar um objeto do tipo cursor
  cursor = conexao.cursor()
  return conexao, cursor 