import socket
import threading


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    @staticmethod
    def client_connection(c_socket: socket.socket) -> None:
        while True:
            data = c_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f'Received {message}')
            response = f"Server received: {message}"
            c_socket.sendall(response.encode('utf-8'))
        c_socket.close()

    def listener(self) -> None:
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_socket.bind((self.host, self.port))
        s_socket.listen(5)
        print(f'Listening on {self.host}:{self.port}')

        while True:
            c_socket, c_address = s_socket.accept()
            print(f'Connection from {c_address} accepted')
            c_connection = threading.Thread(target=self.client_connection, args=(c_socket,))
            c_connection.start()


srv = Server('127.0.0.1', 5006)
srv.listener()
