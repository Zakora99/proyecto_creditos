import sqlite3
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

DB = "creditos.db"

# Función para crear la tabla si no existe
def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS creditos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            monto REAL NOT NULL,
            tasa_interes REAL NOT NULL,
            plazo INTEGER NOT NULL,
            fecha_otorgamiento TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Llamamos a la función para inicializar la DB al iniciar la app
init_db()

@app.route('/creditos/nuevo', methods=['GET', 'POST'])
def nuevo_credito():
    if request.method == 'POST':
        cliente = request.form['cliente']
        monto = float(request.form['monto'])
        tasa_interes = float(request.form['tasa_interes'])
        plazo = int(request.form['plazo'])
        fecha = request.form['fecha_otorgamiento']

        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO creditos (cliente, monto, tasa_interes, plazo, fecha_otorgamiento)
            VALUES (?, ?, ?, ?, ?)
        ''', (cliente, monto, tasa_interes, plazo, fecha))
        conn.commit()
        conn.close()

        return redirect(url_for('listar_creditos'))

    return render_template('nuevo.html')


@app.route('/creditos')
def listar_creditos():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM creditos")
    creditos = cursor.fetchall()
    conn.close()
    return render_template('lista.html', creditos=creditos)


@app.route('/creditos/editar/<int:id>', methods=['GET', 'POST'])
def editar_credito(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    if request.method == 'POST':
        cliente = request.form['cliente']
        monto = float(request.form['monto'])
        tasa_interes = float(request.form['tasa_interes'])
        plazo = int(request.form['plazo'])
        fecha = request.form['fecha_otorgamiento']

        cursor.execute('''
            UPDATE creditos
            SET cliente=?, monto=?, tasa_interes=?, plazo=?, fecha_otorgamiento=?
            WHERE id=?
        ''', (cliente, monto, tasa_interes, plazo, fecha, id))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_creditos'))

    cursor.execute("SELECT * FROM creditos WHERE id=?", (id,))
    credito = cursor.fetchone()
    conn.close()
    return render_template('editar.html', credito=credito)


@app.route('/creditos/eliminar/<int:id>')
def eliminar_credito(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM creditos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_creditos'))


@app.route('/creditos/grafica')
def grafica_creditos():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT fecha_otorgamiento, SUM(monto) FROM creditos GROUP BY fecha_otorgamiento")
    data = cursor.fetchall()
    conn.close()

    fechas = [row[0] for row in data]
    totales = [row[1] for row in data]

    return render_template('grafica.html', fechas=fechas, totales=totales)

if __name__ == '__main__':
    app.run(debug=True)
