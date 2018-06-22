from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inf452'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print(f'Message received: {message}')
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)