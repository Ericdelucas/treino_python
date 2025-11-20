# vamos tambem aorender uma forma de deixar publico uma variavel para todo cod 

def my():
    global x # colocando a variavel na função global toda vez que a função estiver ativa ela sera requisitada sempre 
    x = "como se fosse ontem"
my()

print(x)