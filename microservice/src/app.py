from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    data_file_path = '/data/data.txt'

    if not os.path.exists(data_file_path):
        os.makedirs(os.path.dirname(data_file_path), exist_ok=True)
        with open(data_file_path, 'w') as f:
            f.write("Hello, Persistent World!")

    with open(data_file_path, 'r') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
