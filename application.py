from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)
app.app_context().push()


class Drink(db.Model):
    """
    Represents a drink in the database.

    Attributes:
        id (int): Unique identifier for the drink.
        name (str): Name of the drink (unique and non-nullable).
        description (str): Description of the drink.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        """
        Returns a string representation of the drink.

        Returns:
            str: String representation of the drink.
        """
        return f"{self.name} - {self.description}"


@app.route("/")
def index():
    """Root route that returns a simple greeting."""
    return "Hello Drinks!"


@app.route("/drinks")
def get_drinks():
    """Route to retrieve a list of all drinks."""
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        drink_data = {
            "id": drink.id,
            "name": drink.name,
            "description": drink.description,
        }
        output.append(drink_data)

    return {"drinks": output}


@app.route("/drinks/<id>")
def get_drink(id):
    """Route to retrieve information about a specific drink by ID."""
    drink = Drink.query.get_or_404(id)
    return {"id": drink.id, "name": drink.name, "description": drink.description}


@app.route("/drinks", methods=["POST"])
def add_drink():
    """Route to add a new drink to the database."""
    drink = Drink(name=request.json["name"], description=request.json["description"])
    db.session.add(drink)
    db.session.commit()
    return {"id": drink.id}


@app.route("/drinks/<id>", methods=["DELETE"])
def delete_drink(id):
    """Route to delete a drink from the database by ID."""
    drink = Drink.query.get(id)
    if not drink:
        return {"error": f"ID: {id} Not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": f"ID: {id} - {drink.name} Deleted"}
