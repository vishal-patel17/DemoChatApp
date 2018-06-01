from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room
from flask_session import Session
from flask_login import current_user

# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO(app, manage_session=False)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/signup.html', methods=['GET', 'POST'])
def sineup():
    return render_template('signup.html')


@app.route('/rooms.html', methods=['GET', 'POST'])
def rooms():
    return render_template('rooms.html')


@app.route('/ChatApp.html', methods=['GET', 'POST'])
def chatapp():
    username = request.form['uname']
    # print("User connected: ",)
    return render_template('ChatApp.html', name=username)


@app.route('/add', methods=['GET', 'POST'])
def add():

    print("Added into the Room!")
    return render_template('rooms.html')


def messageRecived():
    print('message was received!!!')


@socketio.on('join')
def on_join(data):
    print("Into join room function")
    username = "vishal"
    room = data
    join_room(room)
    socketio.emit(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = "vishal"
    room = data['room']
    leave_room(room)
    socketio.emit(username + ' has left the room.', room=room)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('recived my event: ' + str(json))
    socketio.emit('my response', json, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
