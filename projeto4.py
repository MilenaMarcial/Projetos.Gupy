import time

def liga_interruptor(numero):
    """Liga o interruptor número"""
    print(f"Ligando interruptor {numero}")

def desliga_interruptor(numero):
    """Desliga o interruptor número"""
    print(f"Desligando interruptor {numero}")

def checa_lampada(numero):
    """Retorna True se a lâmpada número estiver ligada, False caso contrário"""
    print(f"Checando lâmpada {numero}")
    return True  # Retorne True ou False dependendo do estado da lâmpada

def descobre_interruptores():
    # Liga o primeiro interruptor e espera um minuto
    liga_interruptor(1)
    time.sleep(60)

    # Desliga o primeiro interruptor e liga o segundo interruptor
    desliga_interruptor(1)
    liga_interruptor(2)

    # Vai até a sala das lâmpadas
    for i in range(1, 4):
        if checa_lampada(i):
            if liga_interruptor(i - 1):
                print(f"O interruptor {i - 1} controla a lâmpada {i}")
            else:
                print(f"O interruptor {i} controla a lâmpada {i}")
        else:
            print(f"O interruptor {i} não controla a lâmpada {i}")

descobre_interruptores()