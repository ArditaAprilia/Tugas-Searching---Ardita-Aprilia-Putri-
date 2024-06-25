def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1
print("========================================")
print("|       Program Pencarian Harga Buku   |")
print("========================================")


harga_produk = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

harga_dicari = int(input("Masukkan harga buku yang dicari: "))
hasil = binary_search(harga_produk, harga_dicari)

if hasil != -1:
    print(f"Harga {harga_dicari} ditemukan pada indeks {hasil}.")
else:
    print(f"Harga {harga_dicari} tidak ditemukan dalam daftar.")
