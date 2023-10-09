from socket import *

# Variable
serverName = 'localhost'
serverPort = 7

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Choose an operation:")
print("R. Random")
print("A. Add")
print("S. Subtract")

while True:
    choice = input("What would you like to do? (Random(R)/Add(A)/Subtract(S)): ").upper()

    if choice in ['R', 'A', 'S']:
        break
    else:
        print("Invalid choice. Please try again.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

data = f"{choice};{num1};{num2}".encode()

clientSocket.send(data)

dataBack = clientSocket.recv(2048)
sentenceBack = dataBack.decode()

print('Received text:', sentenceBack)
clientSocket.close()
