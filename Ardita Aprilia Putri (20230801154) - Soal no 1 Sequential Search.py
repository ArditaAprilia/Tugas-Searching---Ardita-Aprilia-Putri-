def hitung_jumlah_kata(kalimat):
    kata = kalimat.split()
    jumlah_kata = len(kata)
    jumlah_karakter = sum(len(k) for k in kata)
    rata_rata_panjang_kata = jumlah_karakter / jumlah_kata if jumlah_kata > 0 else 0
    return jumlah_kata, jumlah_karakter, rata_rata_panjang_kata

print("========================================")
print("|       Program sequential Search      |   ")
print("========================================")

def cari_indeks_huruf(kalimat, huruf):
    indeks = [i for i, char in enumerate(kalimat) if char == huruf]
    return indeks

kalimat = input("Masukkan sebuah kalimat: ")
huruf_dicari = input("Masukkan huruf yang dicari: ")

jumlah_kata, jumlah_karakter, rata_rata_panjang_kata = hitung_jumlah_kata(kalimat)
indeks_huruf = cari_indeks_huruf(kalimat, huruf_dicari)

print(f"Jumlah kata dalam kalimat: {jumlah_kata}")
print(f"Jumlah karakter dalam kalimat (tanpa spasi): {jumlah_karakter}")
print(f"Rata-rata panjang kata: {rata_rata_panjang_kata:.2f}")

if indeks_huruf:
    print(f"Huruf '{huruf_dicari}' ditemukan pada indeks: {indeks_huruf}")
else:
    print(f"Huruf '{huruf_dicari}' tidak ditemukan dalam kalimat.")