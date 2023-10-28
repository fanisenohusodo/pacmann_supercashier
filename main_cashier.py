#Mendefinisikan variabel stop
stop = False

#Membuat list kosong untuk menampung belanjaan
item_list = []

#Menginput nama_item, jumlah_item, harga_item dari pengguna
while not stop:
  nama_item = input("Masukkan nama item yang dibeli: ")
  jumlah_item = input("Masukkan jumlah item yang dibeli: ")
  harga_item = input("Masukkan harga item (per pcs): ")

  #Menyimpan hasil input ke dalam list
  item_list.append((nama_item, int(jumlah_item), int(harga_item)))

  #Menampilkan menu untuk input barang selanjutnya atau lanjut menu berikutnya
  stop_input = input("Masukkan item selanjutnya? Ketik Y untuk tambah item atau N jika item sudah lengkap: ")

  #Jika stop_input == "N",program berhenti
  if stop_input == "N" or stop_input == "n":
    stop = True
    break

  # Jika stop_input != "Y", munculkan exception
  elif stop_input not in ("Y", "y"):
    raise Exception("Perintah yang anda masukkan salah")

#import pandas library
import pandas as pd

#membuat kolom total_harga untuk setiap item yang diinput
for i in range(len(item_list)):
    item_list[i] += (item_list[i][1] * item_list[i][2],)
# ubah item_list menjadi dataframe
df = pd.DataFrame(item_list, columns=['nama_item', 'jumlah_item', 'harga_item', 'total_harga'])
# Menampilkan isi keranjang belanja
print('Berikut ini adalah daftar barang yang ada di keranjang belanja anda:')
#tampilkan dataframe
print(df)

def update_items(item_list):
  # Membuat variabel untuk menyimpan list index item yang ingin diubah
  index_item_list = []

  # Menginput index item yang ingin diubah
  while True:
    index_item = input("Masukkan index item yang ingin diubah atau tekan X jika sudah tidak ada item yang ingin diubah: ")

    # Jika input adalah 'x' atau 'X', keluar dari loop
    if index_item == "X" or index_item == "x" :
      break
    
    # Konversi tipe data index_item menjadi integer
    try:
        index_item = int(index_item)
    except ValueError as e:
        # Buat pesan error yang lebih spesifik
        raise ValueError("Index yang Anda masukkan salah")
        continue
        
    # Validasi index item
    if index_item < 0 or index_item >= len(item_list):
      raise ValueError("Index yang Anda masukkan salah")

    # Menambahkan index item ke dalam list
    index_item_list.append(index_item)

  # Menginput nama_item baru, jumlah_item baru, dan harga_item baru untuk setiap index item yang diubah
  for index_item in index_item_list:
    nama_item_baru = input(f"Masukkan nama item baru untuk item di index {index_item}: ")
    jumlah_item_baru = input(f"Masukkan jumlah item baru untuk item di index {index_item}: ")
    harga_item_baru = input(f"Masukkan harga item baru untuk item di index {index_item}: ")

    # Mengubah nama_item, jumlah_item, dan harga_item untuk item di index yang sesuai
    item_list[index_item] = (nama_item_baru, int(jumlah_item_baru), int(harga_item_baru))
    # Menghitung total_harga ulang untuk item yang diubah
    item_list[index_item] = (item_list[index_item][0], item_list[index_item][1], item_list[index_item][2], item_list[index_item][1] * item_list[index_item][2])

  # Mengembalikan list item yang telah diubah
  return item_list

# Menjalankan fungsi update_items
item_list = update_items(item_list)

# Menampilkan hasil
print("Berikut ini isi keranjang belanja anda setelah pembaruan:")

# Membuat dataframe dari item_list hasil update
df = pd.DataFrame(item_list, columns=['nama_item', 'jumlah_item', 'harga_item', 'total_harga'])

# Menampilkan data frame
print(df)

# Menghitung total belanja
total_belanja = df['total_harga'].sum()

# Menampilkan total belanja
print(f'Total belanja anda adalah Rp {total_belanja}')

#Function untuk menghapus item list
def delete_item(item_list, index_delete):
    # Validasi input index yang didelete
    try:
        index_delete = int(index_delete)
        if index_delete < 0 or index_delete >= len(item_list):
            raise ValueError("Index yang Anda masukkan salah")
    except ValueError:
        print("Index yang Anda masukkan salah")

    # Hapus data di item_list
    item_list.pop(index_delete)
    return item_list

# Masukkan index yang akan di delete atau N jika lanjut ke function selanjutnay
index_delete = input('Masukkan index item yang ingin dihapus atau tekan N jika tidak ada item yang ingin dihapus: ')

# Looping agar memungkinkan menghapus beberapa index item sekaligus
while index_delete not in ("N", "n"):
    # Validasi index yang akan di delete
    try:
        index_delete = int(index_delete)
        if index_delete < 0 or index_delete >= len(item_list):
            raise ValueError("Index yang Anda masukkan salah")
    except ValueError:
        print("Index yang Anda masukkan salah")

    # Hapus data di item_list
    item_list = delete_item(item_list, index_delete)

    index_delete = input('Masukkan index item selanjutnya yang ingin dihapus atau tekan N jika sudah tidak ada item yang ingin dihapus: ')

# Menampilkan hasil
print("Berikut ini isi keranjang belanja anda setelah pembaruan:")

# Membuat dataframe dari item_list hasil update
df = pd.DataFrame(item_list, columns=['nama_item', 'jumlah_item', 'harga_item', 'total_harga'])

# Menampilkan data frame
print(df)

# Menghitung total belanja
total_belanja = df['total_harga'].sum()

# Menampilkan total belanja
print(f'Total belanja anda adalah Rp {total_belanja}')

#Function untuk menghapus transaksi
def reset_transaction(item_list):
    #Memasukkan perintah untuk membatalkan (menghapus) transaksi atau melanjutkan pembayaran
    in_reset = input("Lanjutkan pembayaran? tekan Y untuk melanjutkan atau N untuk membatalkan transaksi: ")

    if in_reset in ("N", "n"):
        item_list.clear()
        print("Transaksi anda telah dihapus dan dibatalkan")
        return None
    elif in_reset not in ("Y", "y"):
        raise Exception("Huruf yang anda masukkan salah")
    else:
        return item_list

# Menjalankan fungsi reset_transaction()
item_list = reset_transaction(item_list)

#Function untuk menghitung nilai yang harus dibayar konsumen
def total_price(item_list):
    #jika transaksi sudah dihapus, tidak akan memunculkan function ini
    if item_list is None:
        return None
    #mendefinsikan total belanja
    total_belanja = 0
    for item in item_list:
      total_belanja += item[1] * item[2]
    #menghitung diskon dan total bayar (nilai yang dibayarkan setelah dikurang diskon) sesuai dengan total belanja customer
    if total_belanja >200_000 and total_belanja <=300_000:
        #jika belanja >200_000 diskon 5%
        diskon = 5/100*total_belanja
        total_bayar = total_belanja-diskon
        print(f'Selamat anda mendapatkan diskon Rp {int(diskon)}')
    elif total_belanja >300_000 and total_belanja <=500_000:
        #jika belanja >300_000 diskon 8%
        diskon = 8/100*total_belanja
        total_bayar = total_belanja-diskon
        print(f'Selamat anda mendapatkan diskon Rp {int(diskon)}')
    elif total_belanja >500_000:
        #jika belanja >500_000 diskon 10%
        diskon = 10/100*total_belanja
        total_bayar = total_belanja-diskon
        print(f'Selamat anda mendapatkan diskon Rp {int(diskon)}')
    else:
        #total belanja selain itu tidak mendapat diskon
        diskon = 0
        total_bayar = total_belanja
    #Menampilkan nilai yang harus dibayar pelanggan setelah dikurangi diskon    
    print(f'Total yang harus anda bayar Rp {int(total_bayar)}')
    # Menampilkan data barang yang dibeli
    print('Berikut ini daftar item yang anda beli')
    print(df)

# Menjalankan fungsi total_price()
total_price(item_list)
