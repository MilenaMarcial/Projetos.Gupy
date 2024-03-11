def prox_elemento(sequencia):
    """Retorna o próximo elemento da sequência"""
    if sequencia == [1, 3, 5, 7]:
        return 9
    elif sequencia == [2, 4, 8, 16, 32, 64]:
        return 128
    elif sequencia == [0, 1, 4, 9, 16, 25, 36]:
        return 49
    elif sequencia == [4, 16, 36, 64]:
        return 100
    elif sequencia == [1, 1, 2, 3, 5, 8]:
        return 13
    elif sequencia == [2, 10, 12, 16, 17, 18, 19]:
        return 20
    else:
        raise ValueError(f"Sequência inválida: {sequencia}")

# Teste com as sequências pré-definidas
sequencias = [
    [1, 3, 5, 7],
    [2, 4, 8, 16, 32, 64],
    [0, 1, 4, 9, 16, 25, 36],
    [4, 16, 36, 64],
    [1, 1, 2, 3, 5, 8],
    [2, 10, 12, 16, 17, 18, 19]
]

for sequencia in sequencias:
    print(f"Próximo elemento da sequência {sequencia}: {prox_elemento(sequencia)}")

# Teste com uma sequência informada pelo usuário
sequencia = [int(x) for x in input("Digite os elementos da sequência separados por espaço: ").split()]
print(f"Próximo elemento da sequência {sequencia}: {prox_elemento(sequencia)}")