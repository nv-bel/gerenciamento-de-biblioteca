from Livro import Livro
from Membro import Membro

class Biblioteca:
    def __init__(self):
        self.catalogoLivros = []
        self.listaMembros = []
        
    def addLivroCatalogo(self, livro):
        self.catalogoLivros.append(livro)    
            
        
    def addMembros(self, membro):
        self.listaMembros.append(membro)    
    
        
    def emprestarLivro(self, SearchIdLivro, SearchIdMembro):
        for livro in self.catalogoLivros:
            if livro.id_livro == SearchIdLivro and not livro.emprestado:
                for membro in self.listaMembros:
                    if membro.id_membro == SearchIdMembro:
                        livro.emprestado = True
                        membro.historicoLivros.append(livro)
                        print(f'O livro {livro.titulo} foi emprestado a {membro.nome}')
                        return
        print('Livro não disponível ou membro não encontrado.')
        
    def devolverLivro(self, SearchIdLivro, SearchIdMembro):
        for membro in self.listaMembros:
            if membro.id_membro == SearchIdMembro:
                for livro in membro.historicoLivros:
                    if livro.id_livro==SearchIdLivro:
                        print(f"O livro {livro.titulo} foi devolvido por {membro.nome}")
                        livro.emprestado=False
                        
    def pesquisarLivro(self, searchItem):
        results = []
        for livro in self.catalogoLivros:
            if searchItem.lower() in livro.titulo.lower() or searchItem.lower() in livro.autor.lower() or searchItem == str(livro.id_livro):
                results.append(livro)
        if results:
            print("Resultados da pesquisa:")
            for livro in results:
                print(f"ID: {livro.id_livro} | Título: {livro.titulo} | Autor: {livro.autor} | Disponível: {'Sim' if not livro.emprestado else 'Não'}")
        else:
            print("Nenhum resultado encontrado")
            
    def consultarMembro(self, searchItem):
        results = []
        for membro in self.listaMembros:
            if str(searchItem) == str(membro.id_membro) or searchItem.lower() in membro.nome.lower():
                results.append(membro)
        if results:
            print("Resultados da consulta:")
            for membro in results:
                print(f"ID: {membro.id_membro} | Nome: {membro.nome}")
                if membro.historicoLivros:
                    print("Histórico de livros emprestados:")
                    for livro in membro.historicoLivros:
                        print(f"    - {livro.titulo}")
                else:
                    print("Este membro não possui histórico de livros emprestados.")
        else:
            print("Nenhum membro encontrado com esse ID ou nome.")
