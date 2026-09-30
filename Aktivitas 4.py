Buah = ["pisang", "semangka", "nanas"]
jawaban = input("Buah apa yang kamu inginkan? ").lower()

if jawaban in Buah:
    print("Buah ada dalam list")
else:
    print("Buah tidak ada dalam list")