import socket

target_host = "0.0.0.0"
target_port = 9949

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("meow")

response = client.recv(4096)

print response
