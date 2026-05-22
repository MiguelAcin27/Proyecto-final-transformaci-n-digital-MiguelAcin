from flask import Flask, render_template, request, redirect, url_for
from modelo import ProductoModelo

app = Flask(__name__)

@app.route('/')
def index():
    productos = ProductoModelo.obtener_todos()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    categoria = request.form.get('categoria')
    precio = float(request.form.get('precio'))
    stock = int(request.form.get('stock'))
    if precio >= 0 and stock >= 0:
        ProductoModelo.guardar(nombre, categoria, precio, stock)
    return redirect(url_for('index'))

@app.route('/vender/<int:id_producto>')
def vender(id_producto):
    ProductoModelo.restar_stock(id_producto)
    return redirect(url_for('index'))

@app.route('/reponer/<int:id_producto>')
def reponer(id_producto):
    ProductoModelo.sumar_stock(id_producto)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_producto>')
def eliminar(id_producto):
    ProductoModelo.eliminar(id_producto)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)