from flask import Flask, request, jsonify
from database import db
from model.Meals import Meals

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/api/meals", methods=["POST"])
def register_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    isOnDiet = data.get("isOnDiet")

    meal = Meals(name=name, description=description, isOnDiet=isOnDiet)
    db.session.add(meal)
    db.session.commit()

    mealToDict = meal.to_dict()

    return jsonify({
        "meals": mealToDict
    }), 201

if __name__ == "__main__":
    app.run(debug=True)