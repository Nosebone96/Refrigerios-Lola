from flask import Flask

from config import Config

app = Flask(__name__)

from routes import bp as main_bp
app.register_blueprint(main_bp)

if __name__=="__main__":
    app.config.from_object(Config['develoment'])
    app.run()