import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS TB_CLIENTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT, PESO REAL)')
cursor.execute('INSERT INTO TB_CLIENTES(NOME,PESO) VALUES ("TesteTeste",52.5)')
conexao.commit()

cursor.execute("SELECT * FROM TB_CLIENTES")
#cursor.execute("DELETE from TB_CLIENTES WHERE ID = 1")

registro = []

#for linha in cursor.fetchall():
   # registro.append(linha)
    
#procura = input()
#procura = int(procura)-1
#print(registro[int(procura)][1])

cursor.close()
conexao.close()

#funcao para deletar query
def deleteRecord(id):
    try:
        conexao = sqlite3.connect('basededados.db')
        cursor = conexao.cursor()
        print("Connected to SQLite")

        # Deleting single record now
        sql_delete_query = """DELETE from TB_CLIENTES where ID = ?"""
        cursor.execute(sql_delete_query,(id,))
        conexao.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if conexao:
            conexao.close()
            print("the sqlite connection is closed")

#id dinamico de inclusao
#deleteRecord(6)

#funcao para imprimir todas as querys um por uma
def readSqliteTable():
    try:
        conexao = sqlite3.connect('basededados.db')
        cursor = conexao.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from TB_CLIENTES"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Nome: ", row[1])
            print("Peso: ", row[2])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conexao:
            conexao.close()
            print("The SQLite connection is closed")

readSqliteTable()

#funcao para imprimir um query específica um por uma
def getDeveloperInfo(id):
    try:
        conexao = sqlite3.connect('basededados.db')
        cursor = conexao.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from TB_CLIENTES where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("Id = ", row[0])
            print("Nome  = ", row[1])
            print("Peso  = ", row[2])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conexao:
            conexao.close()
            print("The SQLite connection is closed")

getDeveloperInfo(10)