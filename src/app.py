from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
app.secret_key = 'prieba'

conexion = MySQL(app)

@app.route('/artistas', methods=['GET', 'POST'])
def artistas():
    if request.method == 'POST':
        nombre_artistico = request.form.get('nombreArtistico')
        genero_musical = request.form.get('generoMusical')
        descripcion = request.form.get('descripcion')

        if not nombre_artistico or not genero_musical or not descripcion:
            flash('Todos los campos son obligatorios', 'danger')
            return redirect(url_for('artistas'))

        cursor = conexion.connection.cursor()
        cursor.execute('INSERT INTO artistas (nombre, genero_musical, descripcion) VALUES (%s, %s, %s)', 
                       (nombre_artistico, genero_musical, descripcion))
        conexion.connection.commit()
        cursor.close()

        flash('Artista agregado exitosamente', 'success')
        return redirect(url_for('artistas'))

    return render_template('artistas.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)