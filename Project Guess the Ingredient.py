import time

Bahan_Donat = ["tepung", "telur", "air", "mentega", "ragi", "gula"]
Skor = 0

print("Hai, kamu bisa menebak 3 bahan dari pembuatan donat, siap?? ")
time.sleep(5)

Bahan1 = input("Apa bahan pertama pilihamu? ")
if Bahan1 in Bahan_Donat:
    print("Kamu berhasil menebak " + Bahan1)
    Skor = Skor + 1
else:
    print("Sayang sekali jawabanmu tidak ada dalam daftar")
time.sleep(3)

Bahan2 = input("Apa bahan kedua pilihamu? ")
if Bahan2 in Bahan_Donat:
    print("Kamu berhasil menebak " + Bahan2)
    Skor = Skor + 1
else:
    print("Sayang sekali jawabanmu tidak ada dalam daftar")
time.sleep(3)

Bahan3 = input("Apa bahan ketiga pilihanmu? ")
if Bahan3 in Bahan_Donat:
    print("Kamu berhasil menebak " + Bahan3)
    Skor = Skor + 1
else:
    print("Sayang sekali jawabanmu tidak ada dalam daftar")
time.sleep(3)

print("Permainan selesai, kamu mendapat ", Skor, " poin")
print(Bahan_Donat)