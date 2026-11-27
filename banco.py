
import mysql.connector

# Construir a conexão com o servidor MYSQL
def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="app_esportivo",
        password="SuaSenhaNova2026",
        database="loja_esportiva"
    )
    return conexao


# Cadastrar produtos esportivos
def cadastrar(nome, categoria, preco):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO produto (nome, categoria, preco) VALUES (%s, %s, %s)",
        (nome, categoria, preco)
    )

    conexao.commit()
    cursor.close()
    conexao.close()
