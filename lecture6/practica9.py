from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# $context var for this session
c = {}
c["pass"] = c["user"] = None


def is_logged_in():
    if c["user"] is None and c["pass"] is None:
        return False
    return True


@app.route("/hola")
def hola():
    return "Hola mundo"


@app.route("/hey/<nombre>")
def hey(nombre):
    return "Yo ->{}<-".format(nombre)


@app.route("/")
def home():
    return render_template("index.html", context=c)


@app.route("/signin")
def signin():
    if is_logged_in():
        return redirect("/")
    else:
        return render_template("signin.html")


@app.route("/render/<var_get_0>")
def rndr(var_get_0):
    return render_template("hola.html",
                           nombre_html=var_get_0)


def valid_login(username, password):
    c["pass"] = password
    c["user"] = username
    return True


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form)
        if valid_login(request.form['usuario'], request.form['clave']):
            return redirect("/")
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


app.run()
