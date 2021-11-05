# todo host tem um domínio válido, dá para reconhecê-los:
import socket
import sys


def enumeraDns(site, listaNomes):
    for name in listaNomes:
        dns = name + "." + site
        try:
            print(dns + " : " + socket.gethostbyname(dns))
        except socket.gaierror:
            print(f"Domínio inválido : {dns}")
            pass


if __name__ == '__main__':
    try:
        site = sys.argv[1]
    except IndexError:
        print("Você deve executar o programa da seguinte forma:")
        print("python3 enumeracaoDNS.py nomeDoDominio.com")
    else:
        listaNomes = ["ns1", "ns2", "www", "ftp", "intranet"]
        enumeraDns(site, listaNomes)
