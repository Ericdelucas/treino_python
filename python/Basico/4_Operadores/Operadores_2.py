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

x = 6      # binário: 110
x &= 3     # 110 & 011 = 010 (2)
print(x)   # Saída: 2

#exemplo de uso para binario OR

x = 4      # binário: 100
x |= 3     # 100 | 011 = 111 (7)
print(x)   # Saída: 7

#exemplo de uso de Aplica o operador bitwise XOR 
# x = 5      # binário: 101
# x ^= 3     # 101 ^ 011 = 110 (6)
# print(x)   # Saída: 6

#exemplo Desloca os bits de x para a direita (divide por 2 elevado ao número de posições).
# x = 8      # binário: 1000
# x >>= 2    # 1000 >> 2 = 0010 (2)
# print(x)   # Saída: 2
