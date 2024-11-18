from flask import Flask

def app_creator():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello from Flask on Vercel!"

    return app
