import socket
import random
import time

HOST = 'localhost' 
PORT = 12345        

def cliente():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado ao servidor.")

        while True:
            modo_envio = input("Enviar um pacote (1) ou vários (2)? ")

            if modo_envio == '1':
                pacote = input("Digite o conteúdo do pacote: ")
                inserir_erro = input("Inserir erro de integridade (S/N)? ").lower()

                if inserir_erro == 's':
                    pacote = pacote[:-1] + random.choice('xyz')

                s.sendall(pacote.encode())
                print(f"enviei a mensagem para o servidor: {pacote}")
                resposta = s.recv(1024)
                print(f"Resposta do servidor: {resposta.decode()}")

            elif modo_envio == '2':
                numero_pacotes = int(input("Quantos pacotes deseja enviar? "))
                for i in range(numero_pacotes):
                    pacote = f"Pacote-{i}"
                    s.sendall(pacote.encode())
                    resposta = s.recv(1024)
                    print(f"Resposta do servidor para {pacote}: {resposta.decode()}")
                    time.sleep(0.1) 

            continuar = input("Continuar enviando pacotes (S/N)? ").lower()
            if continuar == 'n':
                break

cliente()
