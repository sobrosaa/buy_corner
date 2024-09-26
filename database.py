import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

# Conexão ao Banco de Dados Buy Corner
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='buy_corner'
        )
        return connection
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

# Funções de manipulação de dados
def fetch_data(query, params=None):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        data = cursor.fetchall()
        connection.close()
        return data
    return []

def execute_query(query, params=None):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params or ())
            connection.commit()
            messagebox.showinfo("Sucesso", "Operação realizada com sucesso")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao executar a operação: {e}")
        finally:
            connection.close()
