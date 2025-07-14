# busca liear com sentinela 

print("""
    qual livro voce proucura:
      -a
      -b
      -c
      -d
      -e
      -f
""")
proucura=str(input(" didite a proucura: "))
livros=["a","b","c","d","e","f"]
n=6


def busca(livros):
    ultimo = livros[n-1]
    livros[n-1] = proucura 
    i=1
    while livros[i]!=proucura:
        i+=1
    livros[n-1] = ultimo
    if i<n or livros[n-1]==proucura:
        print("verificação ")
        return i
    else:
        return -1

resultado=busca(livros,n,proucura)
if resultado == -1:
    print("caramba ")