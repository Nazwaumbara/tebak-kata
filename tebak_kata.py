import random  # Mengimpor modul random untuk memilih binatang secara acak dari daftar

list_binatang = ["kucing", "anjing", "penyu", "unta", "panda", "kuda", "axolotl", "sapi", "kambing", "kakaktua", "lebah", "ikan", "labalaba", "cumicumi"]  
# Daftar binatang yang akan dipilih secara acak untuk permainan

binatang = random.choice(list_binatang)  
# Memilih satu binatang secara acak dari list_binatang dan menyimpannya di variabel 'binatang'

pengganti = ""  
# Inisialisasi string kosong yang akan digunakan untuk menyimpan versi tersembunyi dari 'binatang'

panjang_huruf = len(binatang)  
# Menyimpan panjang (jumlah huruf) dari kata yang dipilih

for i in range(panjang_huruf):
    pengganti += "_"  
# Mengisi variabel 'pengganti' dengan huruf underscore (_) sebanyak jumlah huruf dalam kata 'binatang'
# Misalnya, jika binatang adalah "kuda", maka 'pengganti' akan menjadi "____"

print(pengganti)  
# Menampilkan string 'pengganti' yang berisi underscore di layar

kesempatan = 5  
# Menetapkan jumlah kesempatan (nyawa) untuk pemain, dimulai dengan 5

while kesempatan > 0:  
    # Memulai loop yang akan terus berjalan selama pemain masih memiliki kesempatan tersisa
    
    nebak = input("masukkan 1 huruf : ")  
    # Meminta pemain untuk memasukkan satu huruf sebagai tebakan
    
    if nebak in binatang:  
        # Mengecek apakah huruf yang ditebak ada di dalam kata 'binatang'
        for i in range(panjang_huruf):
            if binatang[i] == nebak:
                pengganti = pengganti[:i] + nebak + pengganti[i+1:]  
        # Jika huruf yang ditebak ada di dalam 'binatang', maka 'pengganti' diperbarui dengan huruf tersebut
        # Penggantian dilakukan dengan mengubah huruf underscore pada posisi yang sesuai dengan huruf yang ditebak
        print(pengganti)  
        # Menampilkan 'pengganti' yang telah diperbarui di layar
        
        if pengganti == binatang:  
            # Mengecek apakah 'pengganti' sekarang sama dengan kata asli 'binatang'
            print("kamu menang")  
            # Jika ya, menampilkan pesan bahwa pemain menang
            break  
            # Menghentikan loop karena permainan telah selesai
    else:
        kesempatan -= 1  
        # Jika tebakan salah, mengurangi jumlah kesempatan (nyawa) pemain
        print("kesempatan tersisa : ", kesempatan)  
        # Menampilkan jumlah kesempatan yang tersisa
        if kesempatan == 0:  
            # Mengecek apakah kesempatan pemain telah habis
            print("kamu kalah")  
            # Jika ya, menampilkan pesan bahwa pemain kalah
            print("kata yang dimaksud adalah : ", binatang)  
            # Menampilkan kata asli yang harus ditebak oleh pemain

