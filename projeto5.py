# ESCREVA UM PROGRAMA QUE INVERTA OS CARACTERES DE UM STRING

def inverte_string(string):
    tamanho = len(string)
    nova_string = ''

    for i in range(tamanho):
        # Subtrai 1 do índice para inverter a string
        nova_string += string[tamanho - 1 - i]

    return nova_string

# Teste com uma string pré-definida
string = 'Hello, World!'
print(inverte_string(string))

# Teste com uma string informada pelo usuário
string = input('Digite uma string: ')
print(inverte_string(string))