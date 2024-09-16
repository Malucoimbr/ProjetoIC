import socket
import random
import threading

HOST = 'localhost'  
PORT = 12345        


def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Servidor pronto. Aguardando conexões...")

        conn, addr = s.accept()
        with conn:
            print(f"Conectado a {addr}")
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Recebido: {data.decode()}")
                
                if random.random() < 0.1:
                    conn.sendall(b"NACK")
                else:
                    conn.sendall(b"ACK")

servidor_thread = threading.Thread(target=servidor)
servidor_thread.start()
