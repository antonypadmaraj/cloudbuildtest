from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def show_current_time():

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return f"Your computer name is {hostname} and IP address is {IPAddr}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
