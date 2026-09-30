import time

# Langkah 1 : Hari Kerja
JamTdr_Krj = int(input("Berapa jam tidurmu dihari kerja? " ))
JamKrj = int(input("Berapa jam kerjamu? "))
JamSnty_Krj = int(input("Berapa jam santaimu di hari kerja? "))
print("Jam belajarmu dihari kerja adalah ", 24 - JamTdr_Krj - JamKrj - JamSnty_Krj - 3, " jam")

time.sleep(5)

# Langkah 2 : Akhir Pekan
JamTdr_AP = int(input("Berapa jam tidurmu diakhir pekan? "))
JamSnty_AP = int(input("Berapa jam santaimu diakhir pekan? "))
print("Jam belajarmu diakhir pekan adalah ", 24 - JamTdr_AP - JamSnty_AP - 3, " jam")

time.sleep(5)

# Langkah 3 : Satu minggu penuh
print("Jam belajarmu selama satu minggu penuh adalah ", (5*(24 - JamTdr_Krj - JamKrj - JamSnty_Krj - 3)) + (2*(24 - JamTdr_AP - JamSnty_AP - 3)), " jam")