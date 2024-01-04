import cv2
import matplotlib.pyplot as plt
import os

def display_image(image, title):
    plt.imshow(image, cmap=plt.get_cmap('gray'))
    plt.title(title)
    plt.show()

def print_image_info(image, title):
    print(f"Informasi Citra {title}:")
    print(f" - Dimensi: {image.shape}")
    print(f" - Tipe Data: {image.dtype}")
    print(f" - Nilai Pixel Min: {image.min()}")
    print(f" - Nilai Pixel Max: {image.max()}")

def save_image(image, filename, directory="."):
    path = os.path.join(directory, filename)
    cv2.imwrite(path, image)
    print(f"Gambar berhasil disimpan di: {path}")

def main():
    while True:
        print("Menu Pilihan:")
        print("1. Tampilkan Citra Warna")
        print("2. Tampilkan Citra Grayscale")
        print("3. Tampilkan Citra Negatif")
        print("4. Gabungkan Dua Gambar")
        print("5. Print Informasi Citra")
        print("6. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

        if choice == '1':
            citra_warna = cv2.imread("C:/Users/Bang Ojanx/Documents/Python/Foto/my.jpg")
            plt.imshow(cv2.cvtColor(citra_warna, cv2.COLOR_BGR2RGB))
            plt.title('Citra Warna')
            plt.show()
            save_option = input("Ingin menyimpan citra warna? (y/n): ")
            if save_option.lower() == 'y':
                filename = input("Masukkan nama file untuk menyimpan gambar (contoh: output.jpg): ")
                save_image(citra_warna, filename, directory="C:/Users/Bang Ojanx/Documents/Python/Foto/")

        elif choice == '2':
            citra_grayscale = cv2.imread("C:/Users/Bang Ojanx/Documents/Python/Foto/my.jpg", cv2.IMREAD_GRAYSCALE)
            display_image(citra_grayscale, 'Citra Grayscale')
            save_option = input("Ingin menyimpan citra grayscale? (y/n): ")
            if save_option.lower() == 'y':
                filename = input("Masukkan nama file untuk menyimpan gambar (contoh: output.jpg): ")
                save_image(citra_grayscale, filename, directory="C:/Users/Bang Ojanx/Documents/Python/Foto/")

        elif choice == '3':
            citra = cv2.imread("C:/Users/Bang Ojanx/Documents/Python/Foto/my.jpg", cv2.IMREAD_GRAYSCALE)
            citra_negatif = 255 - citra
            display_image(citra_negatif, 'Citra Negatif')
            save_option = input("Ingin menyimpan citra negatif? (y/n): ")
            if save_option.lower() == 'y':
                filename = input("Masukkan nama file untuk menyimpan gambar (contoh: output.jpg): ")
                save_image(citra_negatif, filename, directory="C:/Users/Bang Ojanx/Documents/Python/Foto/")

        elif choice == '4':
            citra1 = cv2.imread("C:/Users/Bang Ojanx/Documents/Python/Foto/foto1.jpg", cv2.IMREAD_GRAYSCALE)
            citra2 = cv2.imread("C:/Users/Bang Ojanx/Documents/Python/Foto/foto2.jpg", cv2.IMREAD_GRAYSCALE)
            combined_image = cv2.addWeighted(citra1, 0.5, citra2, 0.5, 0)
            display_image(combined_image, 'Gabungan Dua Gambar')
            save_option = input("Ingin menyimpan gambar gabungan? (y/n): ")
            if save_option.lower() == 'y':
                filename = input("Masukkan nama file untuk menyimpan gambar (contoh: output.jpg): ")
                save_image(combined_image, filename, directory="C:/Users/Bang Ojanx/Documents/Python/Foto/")
        elif choice == '5':
            print("Menu 5 hanya digunakan setelah menampilkan citra (Menu 1-4).")
            title = input("Masukkan judul citra yang ingin dicetak (contoh: Citra Warna/Citra Grayscale/Citra Negatif/Gabungan Dua Gambar): ")
            if title == 'Citra Warna':
                print_image_info(cv2.cvtColor(citra_warna, cv2.COLOR_BGR2RGB), title)
            elif title == 'Citra Grayscale':
                print_image_info(citra_grayscale, title)
            elif title == 'Citra Negatif':
                print_image_info(citra_negatif, title)
            elif title == 'Gabungan Dua Gambar':
                print_image_info(combined_image, title)
            else:
                print("Judul citra tidak valid.")
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, 4, 5, atau 6.")

if __name__ == "__main__":
    main()
