import time

Bahan_Donat = ["tepung", "telur", "air", "mentega", "ragi", "gula"]
Skor = 0

print("Hai, kamu bisa menebak 3 bahan dari pembuatan donat, siap?? ")
time.sleep(5)

for i in range(3):
    Bahan = input("Apa bahan  " + str(i+1) + " pilihanu?")
    if Bahan in Bahan_Donat:
        print("Kamu berhasil menebak " + Bahan)
        Skor += 1
    else:
        print("Sayang sekali jawabanmu tidak ada dalam daftar")
time.sleep(3)


print("Permainan selesai, kamu mendapat ", Skor, " poin")
print(Bahan_Donat)