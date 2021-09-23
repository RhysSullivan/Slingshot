import socket
import sys
fileName = sys.argv[1]
while True:
    with open(fileName, mode='rb') as file: # b is important -> binary    
        fileContent = file.read()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 50000))
        s.listen(1)
        conn, addr = s.accept()    
        print("Sending Data")
        conn.sendall(fileContent)
        conn.close()        
        break