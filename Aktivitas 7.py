def penjumlahan():
    return angka1 + angka2

def pengurangan():
    return angka1 - angka2

def perkalian():
    return angka1 * angka2

def pembagian():
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan."

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (+, -, *, /): ")

if operasi == "+":
    hasil = penjumlahan()
elif operasi == "-":
    hasil = pengurangan()
elif operasi == "*":
    hasil = perkalian()
elif operasi == "/":
    hasil = pembagian()
else:
    hasil = "Operasi tidak valid."

print("hasil: ", hasil)