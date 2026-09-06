from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Konfigurasi Koneksi Database MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="1234",
        database="db_penjualan"
    )

# Halaman Utama: Menampilkan daftar produk
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produk")
    produk_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', produk=produk_list)

# Route untuk Menambah Produk Baru
@app.route('/tambah', methods=['POST'])
def tambah_produk():
    nama = request.form['nama_produk']
    harga = request.form['harga']
    stok = request.form['stok']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produk (nama_produk, harga, stok) VALUES (%s, %s, %s)",
        (nama, harga, stok)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)