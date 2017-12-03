# Problemas
from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient
import sys

app = Flask(__name__)

# Crear un formulario que reciba los datos de una persona

# $context var for this session
c = {}
c["pass"] = c["user"] = c["apellido"] = c["nombre"] = None

# Procesar los datos del formulario con flask y guardarlos en un diccionario


@app.route("/")
def home():
    return render_template("signup.html")


@app.route("/signup")
def signin():
    return render_template("signup.html")


# Guardar el diccionario con los datos de la persona en mongo
def insert_dude_mongodb(user, pass, name, last):
    results = []
    client = None
    try:
        client = MongoClient()

        db = client.test
        prob10 = db.prob10

        results = prob10.insert_one({})
        print(results)
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: %s" % e)
    except pymongo.errors.BulkWriteError as bwe:
        print(bwe.details)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        client.close()
    return results


@app.route('/saveusr', methods=['POST'])
def save_dude():
    error = None
    if request.method == 'POST':
        print(request.form)
        if insert_dude_mongodb(request.form['usuario'], request.form['clave'], request.form['nombre'], request.form['apellido']):
            return redirect("/")
        else:
            error = 'Error @ mongo when inserting'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('signup.html', error=error)


# Proveer una ruta llamada /personas que devuelva un arreglo de diccionarios con los datos de todas las personas
def get_people_from_mongodb():
    results = []
    client = None
    try:
        client = MongoClient()

        db = client.test
        prob10 = db.prob10

        results = prob10.find()
        print(results)
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: %s" % e)
    except pymongo.errors.BulkWriteError as bwe:
        print(bwe.details)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        client.close()
    return results


@app.route("/personas")
def list_people():
    members = get_people_from_mongodb()
    return render_template("personas.html", members)


app.run()
