def nilai_user():
    Nilai = []

    # mendapatkan nilai dari user
    tanya_nilai = True
    while tanya_nilai:
        nilai = float(input("nilai selanjutnya: "))
        if nilai == -1:
            tanya_nilai = False
        else:
            if nilai >= 0 and nilai <= 10:
                Nilai.append(nilai)
            else:
                print("nilai harus antara 0 sampai 10, dan memberikan -1 untuk berhenti")
    return Nilai

def hitung_list_minimum(angka_list):
    minimum = angka_list[0]
    for angka in angka_list:
        if angka < minimum:
            minimum = angka
    return minimum

def hitung_list_maximum(angka_list):
    maximum = angka_list[0]
    for angka in angka_list:
        if angka > maximum:
            maximum = angka
    return maximum

def hitung_list_rata_rata(angka_list):
    jumlah = 0
    for angka in angka_list:
        jumlah += angka
    rata_rata = jumlah / len(angka_list)
    return rata_rata

Nilai = nilai_user()
if len(Nilai) == 0:
    print("Kamu tidak memberikan nilai apapun.")
    exit()
print(Nilai)
print("Kamu memberikan " + str(len(Nilai)) + " nilai.")

minimum = hitung_list_minimum(Nilai)
maximum = hitung_list_maximum(Nilai)
rata_rata = hitung_list_rata_rata(Nilai)

print("Nilai minimum adalah: " + str(minimum))
print("Nilai maximum adalah: " + str(maximum))
print("Nilai rata-rata adalah: " + str(rata_rata))