# app.py
from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.append("src")
from logic.payroll_calculator import Usuario
from controller.controlador_usuarios import Insertar, Actualizar, Borrar, BuscarPorCedula, CrearTabla

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_tabla')
def crear_tabla():
    try:
        CrearTabla()
        mensaje = "Tabla de usuarios creada exitosamente."
    except Exception as e:
        mensaje = f"Error al crear la tabla: {e}"
    return render_template('resultado.html', mensaje=mensaje)

@app.route('/insertar_usuario', methods=['GET', 'POST'])
def insertar_usuario():
    if request.method == 'POST':
        # Obtener datos del formulario
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        salario = float(request.form['salario'])
        dias_trabajados = int(request.form['dias_trabajados'])
        horas_trabajadas = int(request.form['horas_trabajadas'])
        comisiones = float(request.form['comisiones'])
        horas_extras = int(request.form['horas_extras'])

        # Crear objeto Usuario y guardar en la base de datos
        usuario = Usuario(nombre, cedula, salario, dias_trabajados, horas_trabajadas, comisiones, horas_extras)
        try:
            Insertar(usuario)
            mensaje = f"Usuario con cédula {cedula} insertado exitosamente."
            return render_template('resultado.html', mensaje=mensaje)
        except Exception as e:
            mensaje = f"Error al insertar usuario: {e}"
            return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('insertar_usuario.html')

@app.route('/actualizar_usuario', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'POST':
        # Obtener datos del formulario
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        salario = float(request.form['salario'])
        dias_trabajados = int(request.form['dias_trabajados'])
        horas_trabajadas = int(request.form['horas_trabajadas'])
        comisiones = float(request.form['comisiones'])
        horas_extras = int(request.form['horas_extras'])

        # Crear objeto Usuario y actualizar en la base de datos
        usuario = Usuario(nombre, cedula, salario, dias_trabajados, horas_trabajadas, comisiones, horas_extras)
        try:
            Actualizar(usuario)
            mensaje = f"Usuario con cédula {cedula} actualizado exitosamente."
            return render_template('resultado.html', mensaje=mensaje)
        except Exception as e:
            mensaje = f"Error al actualizar usuario: {e}"
            return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('actualizar_usuario.html')

@app.route('/borrar_usuario', methods=['GET', 'POST'])
def borrar_usuario():
    if request.method == 'POST':
        cedula = request.form['cedula']
        try:
            Borrar(cedula)
            mensaje = f"Usuario con cédula {cedula} borrado exitosamente."
            return render_template('resultado.html', mensaje=mensaje)
        except Exception as e:
            mensaje = f"Error al borrar usuario: {e}"
            return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('borrar_usuario.html')

@app.route('/buscar_usuario', methods=['GET', 'POST'])
def buscar_usuario():
    if request.method == 'POST':
        cedula = request.form['cedula']
        try:
            usuario = BuscarPorCedula(cedula)
            return render_template('mostrar_usuario.html', usuario=usuario)
        except Exception as e:
            mensaje = f"Error al buscar usuario: {e}"
            return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('buscar_usuario.html')

if __name__ == '__main__':
    # Crear la tabla de usuarios si no existe
    try:
        CrearTabla()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    app.run(debug=True)
