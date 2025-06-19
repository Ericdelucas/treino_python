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
pooii

