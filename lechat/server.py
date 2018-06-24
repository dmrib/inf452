from datetime import datetime
import socket
import threading
import ui


class Server():
    def __init__(self):
        self.server = socket.socket()
        self.server.bind(('localhost', 4040))
        self.server.listen(1000)
        self.clients = []
    
    def client_session(self, connection, address):
        connection.send(bytes(ui.welcome_message('Welcome to LeChat!'), 'utf-8'))
        while True:
            try:
                msg = connection.recv(4096)
                if msg:
                    msg = str(msg, "utf-8").rstrip('\n')     
                    if msg == 'list':                        
                        self.forward_clients_list(connection, address[0])
                    elif msg == 'bye':
                        self.remove_client(connection, address[0])
                    else:
                        formated = ui.format_message(msg, address[0])
                        print(formated)
                        msg = bytes(formated, 'utf-8')
                        self.broadcast(msg, connection)
            except:
                continue

    def broadcast(self, msg, connection):
        for client in self.clients:
            if client != connection:
                try:
                    client.send(msg)
                except:
                    client.close()
                    if client in self.clients:
                        self.clients.remove(client)
    
    def forward_clients_list(self, connection, address):
        msg = ''
        for client in self.clients:
            if client != connection:
                msg += f'{address}\n'
        msg = ui.users_list(msg)
        connection.send(bytes(msg, 'utf-8'))

    def remove_client(self, connection, address):
        if connection in self.clients:
            msg = ui.status_message("You're good to go!")
            connection.send(bytes(msg, 'utf-8'))
            msg = ui.status_message(f'User {address} is gone.')
            self.broadcast(bytes(msg, 'utf-8'), connection)
            connection.close()
            self.clients.remove(connection)
            print(ui.status_message(f'{address} disconnected.'))

    def run(self):
        print(ui.welcome_message('LeChat server is running...'))
        while True:
            connection, address = self.server.accept()
            self.clients.append(connection)
            print(ui.status_message(f'{address[0]} connected.'))
            threading._start_new_thread(self.client_session, (connection, address))


if __name__ == '__main__':
    server = Server()
    server.run()