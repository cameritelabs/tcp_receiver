import socket
from collections.abc import Callable

HOST = "127.0.0.1"
PORT = 3003


def serve_tcp(handler: Callable[[bytes], None]):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = b""
                while True:
                    new_data = conn.recv(1024)
                    if not new_data:
                        break

                    data += new_data

                print("Received data:", data)
                handler(data)
