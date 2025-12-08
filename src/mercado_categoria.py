from src.banco_dados import conectar
from src.repositorios import mercado_categoria_repositorio

def executar():
    criar_categoria()
    listar_categoria()
    #editar_categoria()
    #apagar_categoria()
    print('Obrigada')


def criar_categoria():

    nome = input("Digite o nome da nova categoria: ")

    mercado_categoria_repositorio.cadastrar(nome)

    print("Categoria criada com sucesso")
    #py -m venv env
    #env\Scripts\activate
    #pip install -r requirements.txt
    #py main.py

def listar_categoria():
    categorias = mercado_categoria_repositorio.obter_todos()

    for categoria in categorias:
        id = categoria["id"]
        nome = categoria["nome"]
        print("ID:", id, "\tNOME:",nome)

def editar_categoria():
    listar_categoria()

    id = input("Digite o id que deseja editar: ")
    nome = input("Digite o novo nome: ")

    mercado_categoria_repositorio.editar(id,nome)
    
 
    print("Categoria alterada com sucesso")

def apagar_categoria():
    listar_categoria()

    id = input("Digite o id que deseja apagar: ")

    linhas_afetadas = mercado_categoria_repositorio.apagar(id)

    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
         print("Categoria apagada com sucesso")



