import re

def fibonacci(n):
    """Retorna o n-ésimo elemento da sequência de Fibonacci"""
    if n < 0:
        raise ValueError("Número inválido: {}".format(n))
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def pertence_fibonacci(n):
    """Retorna True se o número n pertence à sequência de Fibonacci, False caso contrário"""
    try:
        fibonacci(n)
        return True
    except ValueError:
        return False

# Validação de entrada
def valida_entrada(numero):
    """Retorna True se o número for um inteiro não negativo, False caso contrário"""
    if not re.match(r'^-?[0-9]+$', numero):
        return False
    else:
        numero_int = int(numero)
        if numero_int < 0:
            return False
        else:
            return True

# Teste com números pré-definidos
numeros = [0, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55]
for numero in numeros:
    if pertence_fibonacci(numero):
        print("O número {} pertence à sequência de Fibonacci".format(numero))
    else:
        print("O número {} não pertence à sequência de Fibonacci".format(numero))

# Teste com um número informado pelo usuário
numero = input("Digite um número: ")
if valida_entrada(numero):
    numero_int = int(numero)
    if pertence_fibonacci(numero_int):
        print("O número {} pertence à sequência de Fibonacci".format(numero_int))
    else:
        print("O número {} não pertence à sequência de Fibonacci".format(numero_int))
else:
    print("Entrada inválida: {}".format(numero))