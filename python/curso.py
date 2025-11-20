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

]
#_____________________________________________________________________________________________

#Tuplas
[
# Uma tubla e uma maneira de armazenar mas ao contrario das listas elas nao podem ser alteradas
 
# eras=("gelo","merdieval","paz","ouro","guerra","era eric")

# print(eras)

#--------------------------------------------------------------------------------------------

#para contar quantos itens tem em uma tupla
# print(len(eras))

#--------------------------------------------------------------------------------------------

#par verificar o se e uma tuple
# print(type(eras))

#--------------------------------------------------------------------------------------------

# para ver o item da lista com forme  lista
# print(eras[1])

#--------------------------------------------------------------------------------------------

#para vermos se um iten esta na lista por condição

# if "gelo" in eras:
#     print("este iten esta na lista")

#--------------------------------------------------------------------------------------------

#esta e uma forma diferente de add um iten em uma tupla com sitema operacional

# y = ("primavera",)
# eras += y
# print(eras)

#--------------------------------------------------------------------------------------------

#Outra forma de chamar a tupla e o * serve para pegar o resto 

# (a,b,*c)=eras
# print(a)
# print(b)
# print(c)
]
#_____________________________________________________________________________________________

#Dicionario
[
#um dicionario e definido por uma variavel e o seu inice

# dic = {
#     "um"    :1,
#     "dois"  :2,
#     "tres"  :3,
#     "quatro":4,
#     "quatro":5,
#     "cinco" :False,
#     "seis"  :"auto",
#     "sete"  :["red","blue","black"]
# }

# print(dic)

#--------------------------------------------------------------------------------------------

#uma forma de encontrar o indice o elemento e desta forma 

# print(dic["um"])

#--------------------------------------------------------------------------------------------

#quando temos dois indices indenticos mas com 2 variaveis ele ira pegar a ultima 

# print(dic["quatro"])

#--------------------------------------------------------------------------------------------

#como saber o tipo de item que estamos lidando 

# print(type(dic))

#--------------------------------------------------------------------------------------------

#para vermos apenas o indices da listas

# x=dic.keys()
# print(x)

#--------------------------------------------------------------------------------------------
# como podemos adicionar um item a lista 

# dic["oito"]="8"
# print(dic)

#--------------------------------------------------------------------------------------------

#para chamarmos apenas os valores do dicionario

# x=dic.values()
# print(x)

#--------------------------------------------------------------------------------------------

# aqui e como podemos monstrar os itens do dic sendo indice ou valores

# x=dic.items()
# print(x)

#--------------------------------------------------------------------------------------------

#diferente da lista nao e possivel usar o append 

# dic.update({"nove":9})
# print(dic)

#--------------------------------------------------------------------------------------------

#assim como o add e diferente da lista o dicionario tambem muda o remover

# dic.pop("dois")
# print(dic)# ira remover o indice e o valor

#--------------------------------------------------------------------------------------------
# aqui e removido o ultimo item da lista

# dic.popitem()
# print(dic)

]
#_____________________________________________________________________________________________

#if else
[
# condicionadores 

# x == y        e para quando um e ingual a outro
# x != y        e quando um tem que ser diferente 
# x < y         e quando y e menor que o x
# x <= y        e quando y for menor ou igual a x
# x > y         e quando y e maior que o x
# x >= y        e quando y for maior ou igual a x

#--------------------------------------------------------------------------------------------

# para colocarmos isso em pratica 

# a = 3
# b = 5
# if a < b:
#     print("e menor que ")

#--------------------------------------------------------------------------------------------

# tambem existe o elif que seria uma outra posibilidade

# a=int(input())
# b=int(input())

# if a > b:
#     print("1")
# elif a < b:
#     print("2")
# elif a == b:
#     print("3")

#--------------------------------------------------------------------------------------------

# E POR FIM temos o else para caso tudo de errado

# a=int(input())
# b=int(input())

# if a > b:
#     print("1")
# elif a < b:
#     print("2")
# else:
#     print("ia voce me quebra")

#--------------------------------------------------------------------------------------------

# tambem temos o and

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

#--------------------------------------------------------------------------------------------

# por fim podemos colocar um condição em uma condição

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

]
#_____________________________________________________________________________________________

#match
[
# ele serve para nao usar o if e else varias vezes 

# match uii:
#     case x:
#         code block
    
#--------------------------------------------------------------------------------------------

# exemplo de como usar match 

# day= int(input("digite o dia : "))

# match day:
#     case 1:
#         print("dia 1")
#     case 2:
#         print("dia 2")
#     case 3:
#         print("dia 3")
#     case 4:
#         print("dia 4")
#     case 5:
#         print("dia 5")
#     case 6:
#         print("dia 6")
#     case 7:
#         print("dia 7")

#--------------------------------------------------------------------------------------------

# mas quando nao a uma forma de preve a opção ou erra coloque _ como um else


# day= int(input("digite o dia : "))

# match day:
#     case 1:
#         print("dia 1")
#     case 2:
#         print("dia 2")
#     case 3:
#         print("dia 3")
#     case 4:
#         print("dia 4")
#     case 5:
#         print("dia 5")
#     case 6:
#         print("dia 6")
#     case 7:
#         print("dia 7")
#     case _:
#         print("nao foi previsto")

#--------------------------------------------------------------------------------------------

# mas as vezes e muito chatp escrever o mesmo caso varias vezes

# x=int(input("digite um dia :"))

# match x:
#     case 1|2|3|4|5 :
#         print("semanas de descanso")
#     case 6|7:
#         print("trabalhe")
#     case _:
#         print("ai tu me ferra")

#--------------------------------------------------------------------------------------------

# tambem podemos colocar um processo de verificação a mais com if

# y=int(input("digite outro numero de 1 a 10: "))

# match x:
#     case 1|2|3|4|5 if y==1|2|3|4|5:
#         print("os dados estao batendo 1")
#     case 6|7|8|9|10 if y==6|7|8|9|10:
#         print("os dados estao batendo 2")
]
#_____________________________________________________________________________________________

# while 
[
#o while e uma estrutura de repetição criada para fazer um loop em um cod 

# i=1
# while i<10:
#     print(i)
#     i += 1 #operador ternal para somar a cada vez que ele passar por aqui

#--------------------------------------------------------------------------------------------

# mas e claro que as vezes temos que para um loop mesmo a condição sendo verdadeira

#  declaração BREAK

# i=1
# while i < 10:
#     print(i)
#     if i == 8:
#         break
#     i += 1

#--------------------------------------------------------------------------------------------

# mas quando acondição nao for mais verdadeira podemos colocar em uma mensagem 

# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("a condição ja nao e mais valida ")

]
#_____________________________________________________________________________________________

# Laços for 
[
# Executado como um Loop como um while mas mais facil e controlavel

#podemos usar o for para percorrer uma lista

# frut=["eric","anna","chien","master","venus"]
# for x in frut:
#     print(x)

#--------------------------------------------------------------------------------------------

# Loop atraves de corda
# aqui nos vamos distrinchar uma palavra por letras 

# for x in "eric":
#     print(x)

#--------------------------------------------------------------------------------------------

# tambem podemos parar um loop com a função break 

# for x in frut:
#     print(x)
#     if x == "master":
#         break

#--------------------------------------------------------------------------------------------

# mas as veses eu preciso de um numero especifico de voltas 

# for x in range(3):
#     print(" 22 ")

#--------------------------------------------------------------------------------------------

# mas podemos ver que ele vai de 0 5 mas conta ate 4 e podemos corrigir colocando intervalo

# for x in range(1,5):
#     print(x)

#--------------------------------------------------------------------------------------------

# podemos colocar uma mensagem apos a função nao for verdadeira 

# for x in range(5):
#     print(x)
# else:
#     print("acabou a sequencia")

#--------------------------------------------------------------------------------------------

# podemos colocar um criterio e ainda uma forma de aviso caso a função nao for verdade

# for x in range(10):
#     if x == 5:
#         break
#     print(x)
# else:
#     print("mais uma sequencia")

#--------------------------------------------------------------------------------------------

# sendo um loop alinhado ele ira executar o loop acima e o loop embaixo

# frut=["eric","anna"]
# ass=["er","an","ch","ma","ve"]

# for x in frut:
#     for x in ass:
#         print(frut,ass)

#--------------------------------------------------------------------------------------------

# mas as vezes nos temos que evitar um erro para nao interromper o loop usando passe

# for x in [0,1,2,3]:
#     pass

]
#_____________________________________________________________________________________________

# funçoes 
[
#uma funcao e muito util para incurtar cod e melhorar cod

# def tri():
#     print("tri campeao mundial")

# tri()

#--------------------------------------------------------------------------------------------

# tambem podemos fazer uso de tecnicas de soma de caracteres para usos especiais 

# def x(fname):
#     print(fname + "eric")

# x("email de ")
# x("numero ")
# x("tamanho ")

#--------------------------------------------------------------------------------------------

# podemos fazer isso com duas tambem

# def x(tam,tim):
#     print(tam + " " + tim)

# x("eric","luna")

#--------------------------------------------------------------------------------------------

# return , muito usado como o exemplo a baixo como uma forma de ficar mais otimizado

# def tren(x):
#     return 5 * x

# print(tren(3))

#--------------------------------------------------------------------------------------------

# tambem podemos usar a funcao passa para nao dar erro no cod

# def x():
#     pass

#--------------------------------------------------------------------------------------------

# para argumentos chaves 

# def obs(* ,x):
#     print(x)

# obs(x = 3)

]
#_____________________________________________________________________________________________

# lambda
[
#Ele e uma funçao anonima que pode receber qualquer numero de argumentos

# x = lambda a : a + 10
# print(x(5))
#mas ele so pode receber uma expresao

#--------------------------------------------------------------------------------------------

#tambem podemos usar ele com duas variaveis nomeadas dentro do lambda

# x = lambda a,b: a*b
# print(x(2,10))

#--------------------------------------------------------------------------------------------

# tambem podemos fazer uma função para a funçao

# def meu(n):
#     return lambda a : a*n

# mais= meu(5)#primeiro nomeie o valor de n

# print(mais(3))# agora sim o de a

]
#_____________________________________________________________________________________________

# Datas
[
# se quisermos saber a data de hoje e a hora 

# import datetime

# x= datetime.datetime.now()
# print(x)

#--------------------------------------------------------------------------------------------

#para monstrar o ano e o mes 

# x=datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))

]
#_____________________________________________________________________________________________










