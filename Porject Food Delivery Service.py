pizza_tersedia = ["Margeritha", "Calzone", "Four Cheese", "Peperoni", "Napoli"]
pesanan_pizza = []
total_harga = 0

print("Halo, berikut adalah menu pizza: ")

for i, pizza in enumerate(pizza_tersedia):
    print(str(i) + ". " + pizza)

melanjutkan_pesanan = True
while melanjutkan_pesanan:
    jawaban = input("Apakah kamu ingin pizza? (ya/tidak) ")
    if jawaban == "ya":
        valid_pizza_pilihan = False

        while not valid_pizza_pilihan:
            pizza_pilihan = int(input("Apa pizza yang kamu inginkan? (gunakan nomor) "))

            # Validasi input pengguna
            if (pizza_pilihan >= 0) and \
            (pizza_pilihan <= len(pizza_tersedia) - 1):
                pesanan_pizza.append(pizza_tersedia[pizza_pilihan])
                print("menambahkan " + pizza_tersedia[pizza_pilihan] + " Pizza kedalam pesanan")
                total_harga += 30000
                valid_pizza_pilihan = True

            else:
                print("Tolong masukkan nomor yang sesuai")

    else:
        melanjutkan_pesanan = False

print("Kamu telah memesan: ")
print(pesanan_pizza)
print("Kamu harus membayar Rp." + str(total_harga))

tip = 0
valid_tip = False
while not valid_tip:
    tip = int(input("Berapa persen tip yang ingin kamu berikan (0-25%)? "))
    if (tip >= 0) and (tip <= 25):
        valid_tip = True

    else:
        print("Tolong masukkan angka yang sesuai")

total_harga += total_harga * tip / 100
print("Terima kasih, total harga sekarang Rp." + str(total_harga) + ". Pizza sedang dalam pengantaran!" )