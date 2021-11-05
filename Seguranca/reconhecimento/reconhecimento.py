# objetivo: reconhecer informações básicas de um alvo com domínio na rede
import whois
import sys
from colorama import Fore


def infoSite(site):
    """
    Dá informações sobre o domínio buscado, por exemplo, o email, ip, país, responsável,data de criação, data
    de atualização
    :param site:
    :return void:
    """
    dominio = site
    consulta = whois.whois(dominio)
    print(Fore.YELLOW + "***" * 30)
    print(Fore.RED + f"O e-mail desse domínio é : {consulta.email}\n")
    print(Fore.LIGHTBLUE_EX + f"INFORMAÇÕES COLETADAS:\n{consulta.text}")
    print(Fore.YELLOW + "***" * 30)


if __name__ == '__main__':
    try:
        site = sys.argv[1]
    except IndexError:
        print(Fore.GREEN + "Você deve executar o programa da seguinte forma:")
        print("python3 reconhecimento.py nomeDoDominio.com")
    else:
        infoSite(site)
