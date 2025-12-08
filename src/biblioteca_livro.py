from src.banco_dados import conectar
from src.repositorios import biblioteca_livro_repositorio


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
    cadastrar_livro()
    listar_livros()
    #editar_livros()
    #apagar_livro()

def cadastrar_livro():
    titulo = input("Informe o titulo do livro que deseja cadastrar: ")
    quantidade_paginas = input("Informe a quantidade de páginas " \
    "do livro que deseja cadastrar: ")
    autor = input("Informe o autor do livro que deseja cadastrar: ") 
    preco = input("Informe o preço do livro que deseja cadastrar: R$ ") 
    isbn = input("Informe a ISBN do livro que deseja cadastrar: ") 
    descricao = input("Informe a descrição do livro que deseja cadastrar: ") 


    biblioteca_livro_repositorio.cadastrar(titulo,quantidade_paginas,autor,preco,isbn,descricao)

    print("Livro cadastrado  com sucesso")

def listar_livros():
    livros = biblioteca_livro_repositorio.obter_todos()

    for livro in livros:
        id = livro["id"]
        titulo = livro["titulo"]
        quantidade_paginas = livro["quantidade_paginas"]
        autor = livro["autor"]
        preco = livro["preco"]
        isbn = livro["isbn"]
        descricao = livro["descricao"]
        print("ID:", id, "\tTITULO:",titulo, "\tPÁGINAS:",quantidade_paginas,
              "\tAUTOR:",autor,"\tpreco:R$",preco,"\tISBN:",isbn,
              "\tDESCRIÇÃO:",descricao,)

def editar_livros():
    listar_livros()

    id = input("Digite o id que deseja editar: ")
    titulo  = input("Digite o novo titulo: ")
    quantidade_paginas = input("Informe a nova quantidade de páginas " \
    "do livro que deseja cadastrar: ")
    autor = input("Digite o novo autor do livro que deseja cadastrar: ") 
    preco = input("Digite o novo preço do livro que deseja cadastrar: R$ ") 
    isbn = input("Digite a nova ISBN do livro que deseja cadastrar: ") 
    descricao = input("Digite a nova descrição do livro que deseja cadastrar: ") 
    
    biblioteca_livro_repositorio.editar(id,titulo,quantidade_paginas,
                                        autor,preco,isbn,descricao)

    print("Livro alterado com sucesso")
def apagar_livro():
    listar_livros()

    id = input("Digite o id que deseja apagar: ")

    linhas_afetadas = biblioteca_livro_repositorio.apagar(id)

    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
         print("Livro apagada com sucesso")


