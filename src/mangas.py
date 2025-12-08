# 14.   MySQL Criar uma tabela de mangas com as colunas: id, nome, volume, autor, data de lançamento
# 15.   MySQL Criar registro na tabela de mangas do Naruto Volume 52
# 16.   MySQL Criar registro na tabela de mangas do Dragon Ball Volume 20
# 17.   Criar a função de listar
# 18.   Criar a função de editar
# 18.   Criar a função de apagar
# 19.   Criar a função de cadastrar 
from src.banco_dados import conectar
from src.repositorios import mangas_repositorio


def executar_manga():
    #cadastrar_manga()
    listar_manga()
    #editar_manga()
    #apagar_manga()
    

def listar_manga():
    mangas = mangas_repositorio.obter_todos()

    for manga in mangas:
        id = manga[0]
        nome = manga[1]
        volume = manga[2]
        autor = manga[3]
        data_lancamento = manga[4]
        print("ID:", id, "\tNOME:",nome, "\tVOLUME:",volume, 
              "\tAUTOR:",autor, "\tDATA DE LANÇAMENTO:",data_lancamento)

def editar_manga():
    listar_manga()

    id = input("Digite o ID do mangá que deseja editar: ")
    nome = input("Digite o nome do mangá : ")
    volume = input("Digite o nº do volume do mangá: ")
    autor = input("Digite o autor do mangá : ")
    data_lancamento = input("Digite a data de lançamento do mangá: ")

    mangas_repositorio.editar(id,nome,volume,autor,data_lancamento)

    print("Mangá alterado com sucesso")

def apagar_manga():
    listar_manga()

    id = input("Digite o ID  que deseja apagar: ")

    
    linhas_afetadas = mangas_repositorio.apagar(id)

    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
         print("Mangá apagado com sucesso")

  
def cadastrar_manga():

    nome = input("Informe o nome do mangá : ")
    volume = input("Informe o nº do volume do mangá: ")
    autor = input("Informe o autor do mangá : ")
    data_lancamento = input("Informe a data de lançamento do mangá: ") 

    mangas_repositorio.cadastrar(nome,volume,autor,data_lancamento)
    
    print("Mangá cadastrado  com sucesso")

