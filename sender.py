import os 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
file = open("image.jpg", "rb")
client.send("received_image.jpg".encode('utf-8'))
data = file.read()
client.sendall(data)
client.send(b"<END>")
file.close()
client.close()

