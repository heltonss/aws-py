from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP! Helton V@</h1>\nMBA! o/"

if __name__ == '__main__':
    application.run()
