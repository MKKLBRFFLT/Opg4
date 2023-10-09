from socket import *
import threading
import random

def HandleClient(connectionSocket, address):
    print('Address:', address)

    data = connectionSocket.recv(2048)
    sentence = data.decode()

    # Beuger semikolon til at opdele beskeden
    parts = sentence.split(';')

    if len(parts) == 3:
        function = parts[0].upper()
        num1 = parts[1]
        num2 = parts[2]

        try:
            num1 = int(num1)
            num2 = int(num2)

            if function == "R" or function == "RANDOM":
                result = random.randint(num1, num2)
            elif function == "A" or function == "ADD":
                result = num1 + num2
            elif function == "S" or function == "SUBTRACT":
                result = num1 - num2
            else:
                result = "Invalid operation"

        except ValueError:
            result = "Invalid numbers"
    else:
        result = "Invalid format"

    response = str(result).encode()
    connectionSocket.send(response)

    connectionSocket.close()

# Variable
serverPort = 7

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to work for you')

while True:
    csock, addr = serverSocket.accept()
    threading.Thread(target=HandleClient, args=(csock, addr)).start()
