
# Menginputkan Negara dan Usia dari user
Negara = input("Dimana kamu akan mengemudi? (Senegal, Meksiko, Indonesia, Prancis): ").capitalize()
Umur = int(input("Berapa usiamu saat ini?: "))

# Mengeksekusi kondisi yang telah dipilih user
if Negara == "Senegal" :
    if Umur >= 16 :
        print("Kamu boleh mengemudi")
    else:
        print("Kamu dilarang mengemudi")
elif Negara == "Meksiko" :
    if Umur >= 18 :
        print("Kamu boleh mengemudi")
    elif Umur >= 16 :
        print("Kamu boleh mengemudi dengan persetujuan orang tua kamu")
    elif Umur >= 15 : 
        print("Kamu boleh mengemudi dengan pengawasan orang tua kamu")
    else:
        print("Kamu dilarang mengemudi")
elif Negara == "Indonesia" :
    if Umur >= 17 :
        print("Kamu boleh mengemudi")
    else:
        print("Kamu dilarang mengemudi")
elif Negara == "Prancis" :
    if Umur >= 18 :
        print("Kamu boleh mengemudi")
    elif Umur>= 15 :
        print("Kamu boleh mengemudi dengan pengawasan orang tua kamu")
    else:
        print("Kamu dilarang mengemudi")
else:
    print("Pilihan negara tidak tersedia")