#Fundamental of Network Programming in Python

Everything is operating in a client-server manner nowadays, without us noticing

1)you hit facebook on your browser's address bar and it will send out a dns request to your name server 

2)After resolving the hostname to IP address, your system will send out a HTTP GET request to the ip address to retrieve content. 

You probably realise there is a pattern here, requesting certain information from another system, and fundamendally that is the raw concept of client-server model.

To have a full grasp of how communication is being handle for both parties, I will create two simple PY script to illustrate client-server 

tcp_client 
-obviously is the client (duhh)
-This script will import socket which is the low level networking interface lib for python-The flow of the script is to declare server details (ip and port), create a IPv4 client and connect to server and send our all time fav string "meow"
and wait for response for a bufsize of 4096 


tcp_server 
-nuff said server 
-First hald of the script is similar to client, while on second half I  have created Threads to handle multiple clients
and will print out any message sent by client and return a short and sweet message "Ack!" 

udp_client
-How can we leave out our udp friend. Udp client and tcp are very similar but because how both protocol work differently, udp_client doesnt require to authenticate destination before transmiting data.


Run both script on diffent terminal and you have the world's most simplest client-sever app.

