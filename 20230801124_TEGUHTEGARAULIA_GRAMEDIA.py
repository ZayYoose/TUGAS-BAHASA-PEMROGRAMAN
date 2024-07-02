library = [
    {"title": "The legend of TB", "author": "Diki", "year": 1945},
    {"title": "The legend of Raflesia", "author": "Rafli", "year": 1999},
    {"title": "The legend of Elok", "author": "Kurniawan", "year": 2017},
    {"title": "The legend of Jatake", "author": "Aji", "year": 2000},
    {"title": "The legend of VERDE", "author": "Avrian", "year": 1893}
]

def add_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan nama penulis: ")
    year = input("Masukkan tahun terbit: ")
    
    book = {"title": title, "author": author, "year": int(year)}
    library.append(book)
    print(f"Buku '{title}' berhasil ditambahkan ke perpustakaan!")
    
def search_books(keyword):
    results = []
    for book in library:
        if (keyword.lower() in book["title"].lower() or
                keyword.lower() in book["author"].lower() or
                keyword.isdigit() and int(keyword) == book["year"]):
            results.append(book)
    return results

def display_books(books):
    if not books:
        print("Tidak ada buku yang ditemukan.")
    else:
        print("Buku yang ditemukan:")
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def display_all_books():
    if not library:
        print("Tidak ada buku dalam perpustakaan.")
    else:
        print("Daftar semua buku dalam perpustakaan:")
        for book in library:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def main():
    while True:
        print("\n===== GRAMEDIA CITRA RAYA =====")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Tampilkan Semua Buku")
        print("4. Keluar")
        choice = input("Pilih menu (1/2/3/4): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            keyword = input("Masukkan kata kunci (judul, penulis, atau tahun) buku yang ingin dicari: ")
            results = search_books(keyword)
            display_books(results)
        elif choice == '3':
            display_all_books()
        elif choice == '4':
            print("Terima kasih telah menggunakan perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

if __name__ == "__main__":
    main()