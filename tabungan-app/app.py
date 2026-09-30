from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index ():
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        harga = float(request.form['harga'])
        target_tanggal = request.form['target_tanggal']
        metode = request.form['metode']

        hari_ini = datetime.now().date()
        tanggal_tujuan = datetime.strptime(target_tanggal, '%Y-%m-%d').date()
        total_hari = (tanggal_tujuan - hari_ini).days

        if total_hari <= 0:
            return "Tanggal target harus lebih dari tanggal ini!"

        if metode == 'harian':
            nominal = harga / total_hari
            teks = f"Rp. {nominal:,.0f} setiap hari"
        elif metode == 'mingguan':
            total_minggu = total_hari / 7
            nominal = harga / max(total_minggu,1)
            teks = f"Rp. {nominal:,.0f} setiap minggu"
        elif metode == 'bulanan':
            total_bulan = total_hari / 30
            nominal = float(harga / max(total_bulan, 1))
            teks = f"Rp. {nominal:,.0f} setiap bulan"

        return render_template('hasil.html', barang = nama_barang, total_hari = total_hari, hasil_tabungan = teks)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)