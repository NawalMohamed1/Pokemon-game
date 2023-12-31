from flask import Flask, render_template # Flask is a template for how to make a webserver
from helper import get_random_pokemon_selection, get_pokemon_info

app = Flask(__name__) # where app will be saved "Flask.()"


@app.get("/") # "/" is the home page- "base route"
def pokemon_selection():
    random_pokemon_selection = get_random_pokemon_selection()
    return render_template("pokemon_selection.html", random_pokemon_selection=random_pokemon_selection)


@app.get("/<name>") #<> treat whatever is between the angles as a variable
def pokemon_info(name):
    pokemon = get_pokemon_info(name)
    return render_template("pokemon_info.html", pokemon=pokemon)


app.run(debug=True) # Run the app, also adds in updates and gives better error messages