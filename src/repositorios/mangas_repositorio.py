from src.banco_dados import conectar_mangas

def apagar(id:int) -> int:
    conexao = conectar_mangas()

    cursor = conexao.cursor()

    print("Apagando mangá")

    sql = "DELETE FROM mangas WHERE id = %s"
    dados = (id,)

    cursor.execute(sql,dados)

    conexao.commit()

    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas_afetadas

def cadastrar(nome:str,volume:int,autor:str,data_lancamento:str):
    conexao = conectar_mangas()

    cursor = conexao.cursor()

    sql = "INSERT INTO mangas (nome,volume,autor,data_lancamento) VALUES (%s,%s,%s,%s)"
    dados = (nome,volume,autor,data_lancamento)

    cursor.execute(sql,dados)
    
    conexao.commit()

    cursor.close()

def editar( id:int,nome:str,volume:int,autor:str,data_lancamento:str):
    conexao = conectar_mangas()
    
    cursor = conexao.cursor()

    sql = "UPDATE mangas SET nome = %s,volume = %s,autor = %s,data_lancamento = %s WHERE id = %s"
    dados = (nome,volume,autor,data_lancamento, id)

    cursor.execute(sql,dados)
    
    conexao.commit()

    cursor.close()

    conexao.close()

def obter_todos():

    conexao = conectar_mangas()
    cursor = conexao.cursor()

    cursor.execute("SELECT id,nome,volume,autor,data_lancamento FROM mangas")

    registros = cursor.fetchall()

    cursor.close()
    conexao.close()
    mangas = []

    for registro in registros:
        manga = {
           "id": registro[0],
           "nome": registro[1],
           "volume": registro[2],
           "autor": registro[3],
           "data_lancamento": registro[4],
        }
        mangas.append(manga)
        
    return mangas