from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_view():
    return 'A random movie review will soon be here!'

if __name__ == '__main__':
    app.run()
