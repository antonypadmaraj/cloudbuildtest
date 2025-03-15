from flask import Flask
from datetime import datetime

app = Flask(__name__)
story

@app.route('/')
def show_current_time():
    # Get the current time
    current_time = datetime.now()

    # Convert the datetime object to a string
    return f"The current date and time is: {current_time.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



