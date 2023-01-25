from flask import Flask, render_template, request, redirect

from usuarios import Usuario

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/usuarios')


@app.route('/usuarios')
def usuarios():
    return render_template("index.html", usuarios=Usuario.get_all())


@app.route('/usuario/nuevo')
def nuevo():
    return render_template("agregar.html")


@app.route('/usuario/agregar', methods=['POST'])
def agregar():
    print(request.form)
    Usuario.save(request.form)
    return redirect('/usuarios')


@app.route('/usuario/modificar/<int:id>')
def modificar(id):
    data = {
        "id": id
    }
    return render_template("modificar.html", usuario=Usuario.get_one(data))


@app.route('/usuario/mostrar/<int:id>')
def mostrar(id):
    data = {
        "id": id
    }
    return render_template("mostrar.html", usuario=Usuario.get_one(data))


@app.route('/usuario/actualizar', methods=['POST'])
def actualizar():
    Usuario.actualizar(request.form)
    return redirect('/usuarios')


@app.route('/usuario/eliminar/<int:id>')
def eliminar(id):
    data = {
        'id': id
    }
    Usuario.eliminar(data)
    return redirect('/usuarios')


if __name__ == "__main__":
    app.run(debug=True)
