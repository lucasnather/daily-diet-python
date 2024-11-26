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

@app.route("/api/meals", methods=["GET"])
def get_meal():
    meals = Meals.query.all()

    meals_dict = [{ "id": meal.id, "name": meal.name, "description": meal.description, "isOnDiet": meal.isOnDiet } for meal in meals]

    return jsonify({
        "meals": meals_dict
    }), 200

@app.route("/api/meals/<int:meal_id>", methods=["GET"])
def get_meal_by_id(meal_id):
    meal = Meals.query.filter_by(id=meal_id).first()

    if not meal:
        return jsonify({"error": "Meal Not Found"})
    
    meal_to_dict = {
        "id": meal.id,
        "name": meal.name,
        "description": meal.description,
        "isOnDiet": meal.isOnDiet,
    }

    return jsonify({
        "meals": meal_to_dict
    }), 200

@app.route("/api/meals/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):
    meal = Meals.query.filter_by(id=meal_id).first()

    if not meal:
        return jsonify({"error": "Meal Not Found"})
    
    data = request.json
    
    name = data.get("name")
    description = data.get("description")
    isOnDiet = data.get("isOnDiet")
    
    meal.name = name
    meal.description = description
    meal.isOnDiet = isOnDiet

    db.session.commit()
    
    meal_to_dict = {
        "id": meal.id,
        "name": meal.name,
        "description": meal.description,
        "isOnDiet": meal.isOnDiet,
    }

    return jsonify({
        "meals": meal_to_dict
    }), 200

@app.route("/api/meals/on-diet/<int:meal_id>", methods=["PATCH"])
def update_meal_to_on_diet(meal_id):
    meal = Meals.query.filter_by(id=meal_id).first()

    if not meal:
        return jsonify({"error": "Meal Not Found"})    

    meal.isOnDiet = True

    db.session.commit()
    
    meal_to_dict = {
        "id": meal.id,
        "name": meal.name,
        "description": meal.description,
        "isOnDiet": meal.isOnDiet,
    }

    return jsonify({
        "meals": meal_to_dict
    }), 200


@app.route("/api/meals/<int:meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
    meal = Meals.query.filter_by(id=meal_id).first()

    if not meal:
        return jsonify({"error": "Meal Not Found"})
    
    meal_id = meal.id
    db.session.delete(meal)
    db.session.commit()

    return jsonify({
        "message": f"Meal {meal_id} delete"
    })

if __name__ == "__main__":
    app.run(debug=True)