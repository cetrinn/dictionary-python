# 1. Ujian hari pertama - nama jadi key, nilai jadi value
nilai_hari_pertama = {
    "Mady": 8,
    "Roger": 5,
    "Paul": 5,
    "Lucy": 7
}
print("1. Hari pertama:", nilai_hari_pertama)

# 2. Ujian susulan hari kedua - dictionary baru
nilai_susulan = {
    "Ken": 8,
    "Andrea": 7,
    "Smith": 6
}
print("2. Susulan:", nilai_susulan)

# 3. Gabungkan susulan ke hari pertama
nilai_hari_pertama.update(nilai_susulan)
print("3. Setelah digabung:", nilai_hari_pertama)

# 4. Remidi - Roger, Paul, Smith jadi 8
nilai_hari_pertama["Roger"] = 8
nilai_hari_pertama["Paul"] = 8
nilai_hari_pertama["Smith"] = 8
print("4. Setelah remidi:", nilai_hari_pertama)

# 5. Tampilkan yang nilainya >= 8 saja
print("5. Yang nilainya >= 8:")
for nama, nilai in nilai_hari_pertama.items():
    if nilai >= 8:
        print("-", nama, "=", nilai)