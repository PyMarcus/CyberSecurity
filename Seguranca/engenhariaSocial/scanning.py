# interage com serviços e portas em busca de vulnerabilidades, banners, nomes e versões
import os
import netaddr
from colorama import Fore
from netifaces import ifaddresses, AF_INET


# ping sweeper = programa que dispara ping request em todos os hosts em busca de 'hosts vivos'
def scanning(choice=2):
    """
    Procura por ips válidos na rede, pode demorar um pouco
    :return:
    """
    network = "192.168.2.1/24"
    enderecos = netaddr.IPNetwork(network)  # gera uma lista nessa faixa de ip

    if choice == 1:
        """
        Scan completo
        """
        for host in enderecos:
            # broadcast = ultimo, network = primeiro
            if host == enderecos.network or host == enderecos.broadcast:
                continue
            encontrado = os.popen(f"ping -c1 {host}").read()
            if "Destination Host Unreachable" in str(encontrado):
                continue
            elif "100% packet loss" in str(encontrado):
                continue
            else:
                print(Fore.RED + f"Host ativo: {host}")

    elif choice == 2:
        """
        scan de 10 ips acima e abaixo do ip usado
        """
        contai = 0
        addr = ifaddresses('enp2s0') #interface de rede
        ipBase = addr[AF_INET][0]['addr']
        baseIp = ''
        numero = ''
        valor1 = 0
        valor2 = 0

        for i in ipBase:
            if i == '.':
                contai += 1
            if contai == 3:
                if i == '.':
                    pass
                else:
                    numero += i
            else:
                baseIp += i
        baseIp += '.'
        numero = int(numero)
        if numero >= 10:
            valor1 = numero - 10
        if numero <= 255 - 10:
            valor2 = numero + 10
        listaIp = [baseIp + str(x) for x in range(valor1, valor2 + 1)]
        print(f"Procurado hosts ativos na faixa de {baseIp + str(valor1)} até {baseIp + str(valor2)}...")
        for ips in listaIp:
            encontrado = os.popen(f"ping -c1 {ips}").readlines()
            if "Destination Host Unreachable" in str(encontrado):
                continue
            elif "100% packet loss" in str(encontrado):
                continue
            else:
                print(Fore.RED + f"Host ativo: {ips}")
        return listaIp
    else:
        print("Opção inválida")


if __name__ == '__main__':
    try:
        choice = int(input("1 - para scan completo(mais demorado)\n2 - para scan em uma breve faixa de ip\n>>> "))
    except ValueError:
        print("valor informado não é um número válido")
    else:
        scanning(choice)
