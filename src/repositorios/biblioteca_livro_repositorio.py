from src.banco_dados import conectar_livros

def apagar(id:int) -> int:
    
    conexao = conectar_livros()
   
    cursor = conexao.cursor()

    sql = "DELETE FROM livros WHERE id = %s"
    dados = (id,)
    cursor.execute(sql,dados)
    conexao.commit()

    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas_afetadas

def cadastrar(titulo:str,quantidade_paginas:int,autor:str,preco:float,isbn:int,descricao:str):

    conexao = conectar_livros()
    cursor = conexao.cursor()

    sql = "INSERT INTO livros (titulo,quantidade_paginas,autor,preco,isbn,descricao) VALUES (%s,%s,%s,%s,%s,%s)"
    dados = (titulo,quantidade_paginas,autor,preco,isbn,descricao)
    cursor.execute(sql,dados)

    conexao.commit()

    cursor.close()

def editar( id:int,titulo:str,quantidade_paginas:int,autor:str,preco:float,isbn:int,descricao:str):
    conexao = conectar_livros()

    cursor = conexao.cursor()

    sql = "UPDATE livros SET titulo = %s, quantidade_paginas = %s, " \
    "autor = %s,preco = %s,isbn = %s,descricao = %s WHERE id = %s"

    dados = (titulo,quantidade_paginas,autor,preco,isbn,descricao, id)

    cursor.execute(sql,dados)
    
    conexao.commit()

    cursor.close()

    conexao.close()

def obter_todos():
    conexao = conectar_livros()

    cursor = conexao.cursor()

    cursor.execute("SELECT id,titulo,quantidade_paginas,autor," \
    "preco,isbn,descricao FROM livros")

    registros = cursor.fetchall()

    cursor.close()
    conexao.close()
    livros = []

    for registro in registros:
        livro = {
           "id": registro[0],
           "titulo": registro[1],
           "quantidade_paginas": registro[2],
           "autor": registro[3],
           "preco": registro[4],
           "isbn": registro[5],
           "descricao": registro[6],
        }
        livros.append(livro)
        
    return livros





