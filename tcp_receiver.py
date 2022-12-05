from threading import Thread

from flask import Flask

from app.http_routes import routes
from app.message_handler import add_message
from app.tcp_server import serve_tcp

Thread(target=serve_tcp, args=(add_message,)).start()

app = Flask(__name__)
app.register_blueprint(routes, url_prefix="/")


@app.route("/")
def index():
    return ""


app.run("0.0.0.0", 9528)
