# backdoor_v1
This a backdoor i made with python modules like socket, subprocess and threading. The backdoor is injected in a code of a little python-game and obfusced.


The backdoor work with a tcp server and a tcp client. The tcp server is make with the socket moodule and implemented in the love_test code, made by haimagull https://github.com/Haimagull. With the subprocess module,
the backdoor (tcp server) treat command send by the attacker (tcp client). The server run as like daemon with the threading module, for more discretion.





|          Code Amélioration                 |                    Network Protocol                        |
| :---                                       |     :---:     
| More clear data treat by the client code | Use a ssh / ftp / telnet, or other secure protocol for communication between the backdoor and the attacker   |                                                           
| More efficiency during the process of the cmd send by the server  |  Use a tcp server like now, with encrypted packet          |                                                                                 
| Make a bakdoor directly in a protocol      script for more discretion and efficiancy   | Make an ftp connection for dowload or upload file in the   target machine    |
| Make a remote shell                        |                                                            |
| Make a keylogger or other options in the   backdoor     |                                                            |                                                                                             


