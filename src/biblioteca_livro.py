from mysql.connector import connect


#my sql: Criar um novo banco de dados de biblioteca
#my sql: criar uma tabela de livros com id e titulo
#criar um arquivo src/biblioteca_livro.py
#criar a função de cadastro
#criar a função apagar
#criar a função de editar
#criar a função de listar
# alterar a tabela adicionadno o autor preco isbn descrição text
# salvar o arquivo.sql dentro do projeto
# modicar create
# modificar o update
# modificar o list


def cadastrar():
    #cadastrar_livro()
    #listar_livros()
    editar_livros()
    #apagar_livro()

def cadastrar_livro():
    titulo = input("Informe o titulo do livro que deseja cadastrar: ")
    quantidade_paginas = input("Informe a quantidade de páginas do livro que deseja cadastrar: ")

    print("Abrindo conexão com o banco de dados")

    conexao = connect(
        user = "root",
        password = "admin",
        port = "3306",
        host = "127.0.0.1",
        database = "biblioteca"
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO livros (titulo,quantidade_paginas) VALUES (%s,%s)"
    dados = (titulo,quantidade_paginas)
    cursor.execute(sql,dados)

    conexao.commit()

    cursor.close()

    print("Livro cadastrado  com sucesso")

def listar_livros():

    conexao = connect(
        user = "root",
        password = "admin",
        port = "3306",
        host = "127.0.0.1",
        database = "biblioteca"
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT id,titulo,quantidade_paginas FROM livros")

    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    for registro in registros:
        id = registro[0]
        titulo = registro[1]
        quantidade_paginas = registro[2]
        print("ID:", id, "\tTITULO:",titulo, "\tPÁGINAS:",quantidade_paginas)

def editar_livros():
    listar_livros()

    id = input("Digite o id que deseja editar: ")
    titulo  = input("Digite o novo titulo: ")
    quantidade_paginas = input("Informe a nova quantidade de páginas " \
    "do livro que deseja cadastrar: ")
    
    conexao = connect(
        user = "root",
        password = "admin",
        port = "3306",
        host = "127.0.0.1",
        database = "biblioteca",
    )

    cursor = conexao.cursor()

    sql = "UPDATE livros SET titulo = %s, quantidade_paginas = %s WHERE id = %s"
    dados = (titulo,quantidade_paginas, id)

    cursor.execute(sql,dados)
    
    conexao.commit()

    cursor.close()

    conexao.close()

    print("Livro alterado com sucesso")
def apagar_livro():
    listar_livros()

    id = input("Digite o id que deseja apagar: ")

    print("Abrindo conexão com bd")

    conexao = connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "biblioteca",
        
    )
    
    print("Conexão aberta com sucesso")
    cursor = conexao.cursor()

    print("Apagando livros")

    sql = "DELETE FROM livros WHERE id = %s"
    dados = (id,)

    cursor.execute(sql,dados)

    conexao.commit()

    linhas_afetadas = cursor.rowcount
    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
         print("Livro apagada com sucesso")

    cursor.close()
    conexao.close()

