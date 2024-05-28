from flask import Flask, render_template,request
from flask_socketio import SocketIO,send

app = Flask(__name__)


socketio = SocketIO(app,)

#socket messages
@socketio.on("message")
def handle_message(message):
    send(message,broadcast=True)

@socketio.on("user_connection")
def user_connection(username):
    return render_template("index.html",username=username)



#routes
@app.route("/")
@app.route("/chat", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/chat", methods=["POST"])
def index():
    username = request.form.get("username")
    return render_template("index.html",username=username)



if __name__ == "__main__":
    socketio.run(app,host="localhost",port=5000)
    