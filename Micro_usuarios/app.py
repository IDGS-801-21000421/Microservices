from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuración MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'streaming'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json(force=True)  # Asegura que recibes JSON
        nombre = data['nombre']
        email = data['email']
        password = generate_password_hash(data['password'])

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO usuarios(nombre, email, password) VALUES (%s, %s, %s)', 
            (nombre, email, password)
        )
        mysql.connection.commit()

        return jsonify({"mensaje": "Usuario creado"}), 201

    except Exception as e:
        return jsonify({"mensaje": "Error al registrar usuario", "error": str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    email = datos['email']
    password = datos['password']

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
    usuario = cursor.fetchone()

    if usuario and check_password_hash(usuario[3], password):
        return jsonify({"mensaje": "Login exitoso"}), 200
    else:
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

if __name__ == "__main__":
    app.run(port=5001, debug=True)
