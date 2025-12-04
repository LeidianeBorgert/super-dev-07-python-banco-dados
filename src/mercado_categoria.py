from mysql.connector import connect


def executar():
    #criar_categoria()
    #listar_categoria()
    #editar_categoria()
    #apagar_categoria()
    print('Obrigada')


def criar_categoria():

    nome = input("Digite o nome da nova categoria: ")

    print("Abrindo conexão com o banco de dados")
    #abrir a conexao com o banco de dados

    conexao = connect(
        host="127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "mercado",
    )
    #criando uma cursose para poder executar comando no bd
    cursor = conexao.cursor()
    #definir qual comando sera executado

    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    dados = (nome,)
    cursor.execute(sql,dados)

    #confirmar o comando (concretizar o comando de insert)
    conexao.commit()

    #fechar a conexao com o banco de dados do cursos
    cursor.close()

    print("Categoria criada com sucesso")
    #py -m venv env
    #env\Scripts\activate
    #pip install -r requirements.txt
    #py main.py

def listar_categoria():
    conexao = connect(
        user = "root",
        password = "admin",
        port = "3306",
        host = "127.0.0.1",
        database = "mercado",
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT id,nome FROM categorias")

    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    for registro in registros:
        id = registro[0]
        nome = registro[1]
        print("ID:", id, "\tNOME:",nome)

def editar_categoria():
    listar_categoria()

    id = input("Digite o id que deseja editar: ")
    nome = input("Digite o novo nome: ")
    
    conexao = connect(
        user = "root",
        password = "admin",
        port = "3306",
        host = "127.0.0.1",
        database = "mercado",
    )

    cursor = conexao.cursor()

    sql = "UPDATE categorias SET nome = %s WHERE id = %s"
    dados = (nome, id)

    cursor.execute(sql,dados)
    
    conexao.commit()

    cursor.close()

    conexao.close()

    print("Categoria alterada com sucesso")

def apagar_categoria():
    listar_categoria()

    id = input("Digite o id que deseja apagar: ")

    print("Abrindo conexão com bd")

    conexao = connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "mercado",
        
    )
    print("Conexão aberta com sucesso")
    cursor = conexao.cursor()

    print("Apagando categoria")

    sql = "DELETE FROM categorias WHERE id = %s"
    dados = (id,)

    cursor.execute(sql,dados)

    conexao.commit()

    linhas_afetadas = cursor.rowcount
    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
         print("Categoria apagada com sucesso")

    cursor.close()
    conexao.close()

