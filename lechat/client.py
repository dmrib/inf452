import socket
import select
import sys
import ui


class Client():
    def __init__(self):
        self.server = socket.socket()
        self.server.connect(('localhost', 4040))
    
    def chat(self):
        while True:
            sockets = [sys.stdin, self.server]
            r_sockets, w_sockets, e_sockets = select.select(sockets, [], [])
            for sock in r_sockets:
                if sock == self.server:
                    msg = sock.recv(4056).decode('utf-8')
                    print(msg)
                else:
                    msg = sys.stdin.readline()
                    self.server.send(bytes(msg, 'utf-8'))
                    print(ui.format_message(msg, 'Me')) 
                    sys.stdout.flush()


if __name__ == '__main__':
    client = Client()
    client.chat()