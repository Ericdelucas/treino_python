# basico e introdução do python 
[
# a forma de imprimir uma frase no python uma função criada do proprio

# print("Ola mundo")

# no python o recuo e muito inmpo0rtante para a indentificação de uma funcao 
#ex: usando condicao com if ou se 

# if 2 < 5: # crindo uma condição para que se 2 for menor que cinco retorne print 
#     print("2 e menor que cinco")

# else: # caso isso nao seja verdade retornamos isso como se fosse se isso nao e e isso 
#     print("2 e maior que cinco")

#caso as duas condiçoes estejam certas deve se retornar as duas 

# if 2 < 5:
#     print("111")

# if 2 < 5:
#     print("222")
]
#_____________________________________________________________________________________________

#entendendo variaveis 
[
### Variaveis 

#[
# a forma de imprimir uma frase no python uma função criada do proprio
# print("Ola mundo")
#]


# As variaveis devem ser criadas de uma forma que possamos dar umn valor a uma entidade 

# x="Oi meu nome e Eric"
# y="E faço tecnico de inteligencia artificial"

# print(x)
# print(y)

# ou fazendo um tipo de mensclagem 
# print(x,y)

#----------------------------------------------------------------------------------------------
# Vamos nos aprofundar mais na arte das variaveis e vamos ver os tipos delas 

# X="Eric"    # STR que significa uma variavel tipo string ou escrita 
# Y=5         # INT que significa inteiro um numero sem estar quebrado
# Z=2.5       # Float que significa numero flutuante que esta quebrado 

# print(type(X)) # colocando um type colocamos de uma maneira uma forma de verificar as variaveis 
# print(type(Y))
# print(type(Z))

#---------------------------------------------------------------------------------------------
# tambem podemos fazer uma brincadeira interesante para economizar linhas 

# x,y,z= "borboleta" , 4, 4.6
# #desta maneira cada uma ira ter sua respequitiva variavel conforme sua posição sujerida

# print(x)
# print(y)
# print(z)
#---------------------------------------------------------------------------------------------

# #Da mesma forma podemos fazer com que todas estas variavaveis tenham o mesmo significado 
# eric=r=x = 1000
# print(r)
# print(eric)
# print(x)

#--------------------------------------------------------------------------------------------
# # com isso podemos aprende um processo de desempacotamento que
# frut = ["maça","alguma coisa" ," pedro "]
# # podemos separa variaveis de uma lista ou tupla pelo seu indice 
# x,y,z = frut

# print(x)
# print(y)
# print(z)

#--------------------------------------------------------------------------------------------

# tambem podemos fazer somas de variaveis dentro da função print 

# x=2
# y=3
# print(x+y)
# #tambem podemos fazer uma junção de variaveis com str
# a='eric'
# b=' de lucas'
# print(a+b)
#--------------------------------------------------------------------------------------------

# vamos avançar um pouco no conhecimento e criar uma função que faz esta soma para nos 

# x = " anestesia "

# def juntador():
#     print("ele esta"+x)

# juntador()# lembre-se tem que colocar uma () no final da funçao criada 
#-------------------------------------------------------------------------------------------
# devemos prestar atenção que uma variavel pode ser subistituida ou atualizada 
# x="fjg"

# def ah():
#     x="ola mundo"
#     print(" oi e " + x)

# ah()
#--------------------------------------------------------------------------------------------

# vamos tambem aorender uma forma de deixar publico uma variavel para todo cod 

# def my():
#     global x # colocando a variavel na função global toda vez que a função estiver ativa ela sera requisitada sempre 
#     x = "como se fosse ontem"
# my()

# print(x)
]
#_____________________________________________________________________________________________

#todos os tipos de variaveis 
[
# no capitulo acima demos uma revisada em tipos de variaveis mas agora vamos dar uma aprofundada melhor nesse tema 
#existem a seguintes variaveis 

# A="oi"              #variavel tipo STR
# B=5                 #variavel tipo INT numero inteiro  
# C=3.5               #Variavel tipo Float numero flutuante ou numero quebrado 
# D=1j                #variavel tipo complexo 
# F=["a","b"]         #variavel tipo lista para armazenar dados 
# G=("a","b")         #variavel tipo tuple
# H=range(6)          #variavel tipo range para estrutura de repetição
# I={"n":2,"t":3}     #variavel tipo dicionario para armazenar dados 
# J={"a","b","c"}     #variavel tipo set
# K=frozenset({"a"})  #variavel tipo frozenset
# L=True              #variavel tipo Bool
# N=b"ola"            #variavel tipo bytes

]
#_____________________________________________________________________________________________

# como manipular str 
[
    
#temos algumas coisas a se compreender neste capitulo 

# a primeira e:
# print("faço tecnico de 'inteligencia artificial'")
# # observe que podemos colocar '' em qualquer lugar para fazer esta esclamação

# #tambem podemos fazer uma forma de texto com tres """  """ que da para usar vairias linhas 

# print("""
# oi meu nome e eric
# faço tecnico de AI
# meu rob e programar
# """)

# # tambem podemos fazer assim 

# a='''
# oi meu nome e eric
# faço tecnico de AI
# meu rob e programar
# '''
# print(a)

#--------------------------------------------------------------------------------------------
# tambem podemos criar uma forma de sintax para selecionar as letras que desejamos

# b="meu nome"
# print(b[2:6])
# #desta forma ele iraa selecionar as letras que estao entre os indice 2 e 6

# tambem temos o caso que podemos pegar todo que tiver e colocar o limite ate o quinto indice
# print(b[:5])

#aqui poemos colocar tudo que esta fora deste quadrante seja desconiderado
# print(b[-5:-2])

#--------------------------------------------------------------------------------------------

# agora vamos aprender a modificar str

# a="     Eric de lúças,12354"

#por exemplo podemos colocar tudo em maiusculo
# print(a.upper())

#aqui colocamos tudo em minusculo
# print(a.lower())

#mas se voce proucura remover os espaços em branco use este
# print(a.strip())

#para modificar o texto de uma letra
# print(a.replace("E" , "He"))

#separa em uma estancia indicada no texto
# print(a.split(","))

#--------------------------------------------------------------------------------------------

#podemos tambem fazer uma brincadeira que e modificar um texto de dentro

# a="Eric"

# b=f"ola meu nome e {a}"#o f representa um format que e para modificar 

# print(b)

#tambem podemos fazer desta forma 

# a=input(str("digite seu nome:"))#input e uma função para o usuario escrever
# b=f"ou meu nome e {a} e estou no ensino medio"
# print(b)

#--------------------------------------------------------------------------------------------

#tambem temos as formas de modificar textos 

# \'	    Single Quote	
# \\	    Backslash	
# \n	    New Line	
# \r	    Carriage Return	
# \t	    Tab	
# \b	    Backspace	
# \f	    Form Feed	
# \ooo	    Octal value	
# \xhh	    Hex value
]
#_____________________________________________________________________________________________

# Boolean Values
[
#variaveis boolear são usadas para estruturas de decição como o if e demonstra vedadeiro ou falso

# print(10>9) # como 10 e maior que 9 ira retornar true que e verdadeiro 
# print(10<9) # false 
# print(10 == 9) #false

#--------------------------------------------------------------------------------------------

# e gracias a isso podemos usar as estrutura de decisao

# x=9
# y=10

# if x>y:
#     print("primeira opção")
# else:
#     print("segunda opção")

#--------------------------------------------------------------------------------------------

#tambem podemos usar isso isso no print para verificar se uma variavel e verdadeira 

# print(bool(1))# como e um numero retorna verdadeiro 
# print(bool("eric"))

#--------------------------------------------------------------------------------------------
#tipos de variaveis que resultam em false

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))
]
#_____________________________________________________________________________________________

# Operadores 
[
# +	    Addition	        x + y	
# -	    Subtraction	        x - y	
# *	    Multiplication	    x * y	
# /	    Division	        x / y	
# %	    Modulus	            x % y	    são para calcular a divisão sem a casa decimal para baixo
# **	Exponentiation	    x ** y	
# //	Floor division	    x // y	    Sao para calcular a divisão so que aredondando para cima

# ex:
# print(7%3)
# print(7//3)

#--------------------------------------------------------------------------------------------


# isso serve para dizer se uma coisa e verdadeira ou falsa como um contei e nao contei da matematica 

# in 	            Returns True if a sequence with the specified value 
#                 is present in the object	x in y

# not in	        Returns True if a sequence with the specified value 
#                 is not present in the object	x not in y

#muito ultiu para listas 
#--------------------------------------------------------------------------------------------
#operadores ternais muito uteis 

# =	    x = 5	    x = 5	    
# +=	x += 3	    x = x + 3	    fara a soma 
# -=	x -= 3	    x = x - 3	    fara a subtração
# *=	x *= 3	    x = x * 3	    multiplicação
# /=	x /= 3	    x = x / 3	    fara a divisão
# %=	x %= 3	    x = x % 3	    calcular o resto da divisão entre a variavel e o valor 
# //=	x //= 3	    x = x // 3	    calcular o valor descartando os numeros das casas decimais 
# **=	x **= 3	    x = x ** 3	    potencia
# &=	x &= 3	    x = x & 3	    calcula o valor em binario 
# |=	x |= 3	    x = x | 3	    esse e binario com OR 
# ^=	x ^= 3	    x = x ^ 3       Aplica o operador bitwise XOR 	    
# >>=	x >>= 3	    x = x >> 3	    Desloca os bits de x para a direita (divide por 2 elevado ao número de posições).
# <<=	x <<= 3	    x = x << 3	
# :=	print(x:=3)	x = 3


#exemplo de uso para calculo binario

# x = 6      # binário: 110
# x &= 3     # 110 & 011 = 010 (2)
# print(x)   # Saída: 2

#exemplo de uso para binario OR

# x = 4      # binário: 100
# x |= 3     # 100 | 011 = 111 (7)
# print(x)   # Saída: 7

#exemplo de uso de Aplica o operador bitwise XOR 
# x = 5      # binário: 101
# x ^= 3     # 101 ^ 011 = 110 (6)
# print(x)   # Saída: 6

#exemplo Desloca os bits de x para a direita (divide por 2 elevado ao número de posições).
# x = 8      # binário: 1000
# x >>= 2    # 1000 >> 2 = 0010 (2)
# print(x)   # Saída: 2

#--------------------------------------------------------------------------------------------

# Operator	    Name	                    Example	
#   ==	        Equal	                    x == y	
#   !=	        nao e igual	                x != y	
#   >	        maior que    	            x > y	
#   <	        menor que	                x < y	
#   >=	        Greater than or equal to	x >= y	
#   <=	        Less than or equal to	    x <= y 

]
#_____________________________________________________________________________________________

# Listas
[
#Uma lista e uma forma de guardar informações como um caixa 

# #uma çista pode er criada com um [] 
# mylist=["eric","anna","arthur"]
# print(mylist)

#--------------------------------------------------------------------------------------------

#para sabermos quantos tens a dentro de uma lista podemos usar a função len
# print(len(mylist))

#--------------------------------------------------------------------------------------------
#e podemos qualque variavel boolean dentro de uma lista 

# mylist2=[2,6,4,8,9]
# mylist3=[True,False,True]

# print(type(mylist))
# print(type(mylist2))
# print(type(mylist3))

#--------------------------------------------------------------------------------------------

# a outra forma de criar uma lista e é desse jeito list()
#esta forma exige que tenha dois parenteses 
# banco_de_dados=list(("eric","","isso","chaves"))

# print(banco_de_dados)#e devolve com [] como uma lista 

#--------------------------------------------------------------------------------------------

#e desta forma fazemos uma busca pelo indice
# mylist=["eric","olhar","isso","chaves","banco","chico","Anna"]

# print(mylist[1])
# print(mylist[-1])#quando colocamos - ele vai de tras para frente 
# print(mylist[1:4])#monstre apenas o que esta dentro do intervalo

#--------------------------------------------------------------------------------------------

#tambem podemons fazer uma estrutura no qual faz uma ação caso um item esteja na lista

# newlist=[2,6,4,7,98,5,9,5,9,4,50,5,7,7,6,57,]

# if 50 in newlist:#o in seria para falar se contem ou nao dentro de uma lista
#     print("nesta lista contem o numero 50")
# else:
#     print("esta lista no contem o numero 50")

#--------------------------------------------------------------------------------------------
#desta forma conseguimos fazer uma alteração substituindo pelo indice

# newlist[1]=100
# print(newlist)

#--------------------------------------------------------------------------------------------
#neste caso adiciona o item empurando o resto para frente 

# newlist.insert(3,"pikachu")
# print(newlist)

#--------------------------------------------------------------------------------------------

# Aqui vamos tambem adicionar um elemento a lista no final com a função append

# newlist.append("eric")
# print(newlist)

#--------------------------------------------------------------------------------------------
#e tambem podemos adicionar no final da lista outroa lista e juntalas 

# outros=["eric","anna","yang","savino","chien","stefanni"]

# newlist.extend(outros)
# print(newlist)

#--------------------------------------------------------------------------------------------
#podemos remover um item da lista 

# newlist.remove(50)
# print(newlist)

#--------------------------------------------------------------------------------------------
#outra forma de remover e usando o metodo pop que remove pelo indice 

# newlist.pop(4)#obs se deixar sem o indice ele removera o ultimo elemento 
# print(newlist)

#--------------------------------------------------------------------------------------------
# aqui ele dara Erro ´pois o metodo del deleta a lista em si

# del newlist
# print(newlist)

#--------------------------------------------------------------------------------------------

#mas caso queira apenas limpar a lista podemos usar o clear

# newlist.clear()
# print(newlist)

#--------------------------------------------------------------------------------------------
# tambem podemos fazer com que uma esstrutura de repetição corra atraves da lista 

# for x in newlist:
#     print(x)

#--------------------------------------------------------------------------------------------
# DESTA FORMA VC MONSTRA AS COISAS DA LISTA e repete com a quantidade de vezes de itens
# esta repetição se deve o fato por conta do renge
# for i in range(len(newlist)):
#     print(newlist[i])

#--------------------------------------------------------------------------------------------
#com isso voce consegue contar quantos itens a em uma lista com for

# for i in range(len(newlist)):
#     print(i)

#--------------------------------------------------------------------------------------------
# desta forma fazemos que a estrutura do while consiga corre a lista como um vetor da lucy 

# i= 0
# while i < len(newlist):
#     print(newlist[i])
#     i = i+1

#--------------------------------------------------------------------------------------------
# agoram aprendemos a como organizar uma lista e ordenalas seja em ordem cresente ou alfabetica

# newlist.sort()
# print(newlist)

#--------------------------------------------------------------------------------------------
#com a função reverso ligado ou seja = a True ela ira reverte a ordem de organização

# newlist.sort(reverse = True)
# print(newlist)

#--------------------------------------------------------------------------------------------

# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

]
#_____________________________________________________________________________________________
