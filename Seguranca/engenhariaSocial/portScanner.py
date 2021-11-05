# port scanner para identificar portas abertas e serviços
import socket
import threading
import time

ip = ''


def scannerPort(port):
    """
    procura portas abertas
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = s.connect_ex((ip, port))
    if res == 0:  # resultado ok
        print(f"Porta aberta encontrada: {port}, ou seja, pode-se tentar uma conexão nela :)...boa sorte!")
    s.close()
    return port


def searchPort():
    """
    procura pelas portas
    :return:
    """
    global ip
    ip = str(input("Informe o endereço ip:\nex:192.168.0.2\nip: "))
    print()
    for port in range(1, 65535):
        # para cada passada no loop, uma threading será aberta para chamar a função e rodar o scan
        if threading.active_count() > 700:
            time.sleep(1)
        t = threading.Thread(target=scannerPort, args=(port,))
        t.setDaemon(True)  # elimina as threadings assim que terminam
        t.start()
    print("Scan concluído!")


if __name__ == '__main__':
    searchPort()
