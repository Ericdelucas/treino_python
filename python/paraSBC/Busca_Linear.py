#exercicio : achar um livro em uma biblioteca desoranizada

#Entrada
    # livro: arranjo
    # qtd_livros  : numero de elementos em inteiro
    # proucurador : valor que busca

# saida
    # o indice com a posição do livro ou caso contrario Not

livro=["a","b","c","d","e","f","g","h"]

print("""
opçoes de livros:
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h"
""")

def busca_linear(livro,qtd_livros,proucurado):
    Retorna = -1
    for i in range(qtd_livros):
        if livro[i] == proucurado:
            Retorna = i
    return Retorna

qtd_livros = 8
proucurado =str(input("qual livro voce deseja: "))

resposta= busca_linear(livro,qtd_livros,proucurado)

print(resposta)