from Livro import Livro
from Membro import Membro
from Biblioteca import Biblioteca

def menu():
    print("\n=========== Menu Bibioteca ===========")
    print("1. Adicionar Livro")
    print("2. Adicionar Membro")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Pesquisar Livro")
    print("6. Consultar Membro")
    print("0. Sair")



if __name__ == '__main__':
    biblioteca = Biblioteca()
    
    while True:
        menu()
        op=input('\n> Escolha uma opção: \n')
        
        if op == "1":
            id_livro = int(input("> Digite o ID do livro: "))
            titulo = input("> Digite o título do livro: ")
            autor = input("> Digite o autor do livro: \n")
            livro = Livro(id_livro, titulo, autor)
            biblioteca.addLivroCatalogo(livro)

        elif op == "2":
            id_membro = int(input("> Digite o ID do membro: "))
            nome = input("> Digite o nome do membro: \n")
            membro = Membro(id_membro, nome)
            biblioteca.addMembros(membro)

        elif op == "3":
            livro_id = int(input("> Digite o ID do livro a ser emprestado: "))
            membro_id = int(input("> Digite o ID do membro que está emprestando: \n"))
            biblioteca.emprestarLivro(livro_id, membro_id)

        elif op == "4":
            livro_id = int(input("> Digite o ID do livro a ser devolvido: "))
            membro_id = int(input("> Digite o ID do membro que está devolvendo: \n"))
            biblioteca.devolverLivro(livro_id, membro_id)

        elif op == "5":
            searchItem = input("> Digite o título, autor ou ID do livro a ser pesquisado: \n")
            biblioteca.pesquisarLivro(searchItem)

        elif op == "6":
            searchItem = input("> Digite o ID ou nome do membro a ser consultado: \n")
            biblioteca.consultarMembro(searchItem)
            
        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")