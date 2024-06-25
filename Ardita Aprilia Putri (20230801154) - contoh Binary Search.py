def binary_search(arr, x):
    
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

def main():
    arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))

    x = int(input("Masukkan elemen yang akan dicari: "))

    result = binary_search(arr, x)

    if result != -1:
        print(f"Elemen ditemukan pada indeks {result}")
    else:
        print("Elemen tidak ditemukan dalam daftar")

if __name__ == "__main__":
     main()
    