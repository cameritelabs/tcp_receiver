import socket
from collections.abc import Callable

HOST = "0.0.0.0"
PORT = 9950


def serve_tcp(handler: Callable[[bytes], None]):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Binding TCP on {HOST} {PORT}...")
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening TCP on {HOST} {PORT}...")
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
