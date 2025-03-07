from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL

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

@app.route('/videos', methods=['GET'])
def obtener_videos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT titulo, descripcion, url FROM videos')
    data = cursor.fetchall()

    videos = [{'titulo': row[0], 'descripcion': row[1], 'url': row[2]} for row in data]

    return jsonify(videos), 200

@app.route('/videos', methods=['POST'])
def agregar_video():
    nuevo_video = request.json
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO videos (titulo, descripcion, url) VALUES (%s,%s,%s)',
                   (nuevo_video['titulo'], nuevo_video['descripcion'], nuevo_video['url']))
    mysql.connection.commit()

    return jsonify({"mensaje": "Video agregado"}), 201

if __name__ == "__main__":
    app.run(port=5002, debug=True)
