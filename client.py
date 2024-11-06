import socket
import threading

class Client:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f'Connected to {self.host}:{self.port}')

            listen_thread = threading.Thread(target=self.receive_message)
            listen_thread.start()

            self.send_messages()
        except ConnectionRefusedError:
            print(f'Connection refused by {self.host}:{self.port}')
    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"S: {message}")
                else:
                    print(f'Connection closed from {self.host}:{self.port}')
                    break
            except ConnectionResetError:
                print(f'Connection reset by {self.host}:{self.port}')
            except ConnectionAbortedError:
                print(f'Connection aborted by {self.host}:{self.port}')
            except Exception as e:
                print(f'Error: {e}')
                break

    def send_messages(self):
        while True:
            message=input('Enter message: ')
            if message.lower() == "exit":
                print(f"Exiting chat...")
                self.client_socket.close()
                break
            self.client_socket.sendall(message.encode('utf-8'))



client = Client('127.0.0.1', 5006)
client.connect()

