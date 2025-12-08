from src.banco_dados import conectar

def cadastrar(nome: str):

    #abrir a conexao com o banco de dados
    conexao = conectar()
    #criando uma cursor para poder executar comando no bd
    cursor = conexao.cursor()
    #definir qual comando sera executado

    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    dados = (nome,)
    cursor.execute(sql,dados)

    #confirmar o comando (concretizar o comando de insert)
    conexao.commit()

    #fechar a conexao com o banco de dados do cursos
    cursor.close()

def editar(id: int, nome: str):
    
    conexao = conectar()

    cursor = conexao.cursor()

    sql = "UPDATE categorias SET nome = %s WHERE id = %s"
    dados = (nome, id)

    cursor.execute(sql,dados)
    
    conexao.commit()

    cursor.close()

    conexao.close()

def apagar(id:int) -> int:
    
   # print("Abrindo conexão com bd")
    conexao = conectar()
  #  print("Conexão aberta com sucesso")
    cursor = conexao.cursor()
   # print("Apagando categoria")
    sql = "DELETE FROM categorias WHERE id = %s"
    dados = (id,)
    cursor.execute(sql,dados)
    conexao.commit()

    linhas_afetadas = cursor.rowcount

    cursor.close()
    conexao.close()
    return linhas_afetadas

def obter_todos():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("SELECT id,nome FROM categorias")

    registros = cursor.fetchall()

    cursor.close()
    conexao.close()
    categorias = []

    for registro in registros:
        categoria = {
            "id":registro[0],
            "nome":registro[1]
        }
        categorias.append(categoria)
        
    return categorias

