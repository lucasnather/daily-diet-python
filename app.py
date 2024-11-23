from flask import Flask, request
from config.database import db

app = Flask(__name__)

app.config["SQLACHEMY_DATABASE_URI"] = "mysql://nather:podevermesmosotoestudando@localhost:3307/diet"

db.init_app(app)

@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)