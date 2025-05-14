

from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de usuarios para el ejercicio 2
usuarios_registrados = {
    'juan': {'password': 'admin', 'rol': 'administrador'},
    'pepe': {'password': 'user', 'rol': 'usuario'}
}


# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para el ejercicio 1 - Pinturas
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Procesar datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        # Cálculos
        precio_unitario = 9000
        total_sin_descuento = tarros * precio_unitario

        # Determinar descuento
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        # Pasar resultados a la plantilla
        return render_template('resultadoEjercicio1.html',
                               nombre=nombre,
                               total_sin=total_sin_descuento,
                               total_con=total_con_descuento,
                               descuento=int(descuento * 100))

    return render_template('ejercicio1.html')


# Ruta para el ejercicio 2 - Login
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar credenciales
        if username in usuarios_registrados and usuarios_registrados[username]['password'] == password:
            rol = usuarios_registrados[username]['rol']
            mensaje = f"Bienvenido {rol} {username}"
            return render_template('resultadoEjercicio2.html', mensaje=mensaje, success=True)
        else:
            return render_template('resultadoEjercicio2.html',
                                   mensaje="Usuario o contraseña incorrectos",
                                   success=False)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)