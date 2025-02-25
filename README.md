# Backdoor v1

## Overview
This project is a simple backdoor written in Python for educational and testing purposes. It allows a user to remotely execute commands on a target system. The implementation includes networking, process handling, and threading.

## Features
- Remote command execution
- Uses `socket` for communication
- Multi-threaded for better handling of connections (for the backdoor implemented in the game)
- Basic obfuscation methods (for the backdoor implemented in the game)

## Installation
```bash
git clone https://github.com/Fournoy/backdoor_v1.git
cd backdoor_v1
```

## Usage
### Start the listener
Run the following command to start the listener on your attacking machine:
```bash
python3 client.py
```

### Deploy the backdoor
Run the backdoor script on the target machine:
```bash
python3 backdoor.py
```
### Usage in programme

Soon, i will update the backdoor to make a better obfuscation. Also, i will perform some automated escalation provileges for Linux systems and, after, windows systems.







|          Code enhancement idea                  |                    Network Protocol                        |
| :---                                       |     :---:     
| More clear data treat by the client code | Use a ssh / ftp / telnet, or other secure protocol for communication between the backdoor and the attacker   |                                                           
| More efficiency during the process of the cmd send by the server  |  Use a tcp server like now, with encrypted packet          |                                                                                 
| Make a bakdoor directly in a protocol      script for more discretion and efficiancy   | Make an ftp connection for dowload or upload file in the   target machine    |
| Make a remote shell                        |                                                            |
| Make a keylogger or other options in the   backdoor     |                                                            |                                                                                             


