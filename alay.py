def translet_to_alay(kalimat):
    huruf_alay = 'aAiIeEoOjJgGbrRsSB'
    hasil_alay = '441133007799622558'
    hasil = ''
    for karakter in kalimat:
        if karakter in huruf_alay:#harus di ubah
            posisi = huruf_alay.index(karakter)
            hasil=hasil+hasil_alay[posisi]
        else:
            hasil= hasil+karakter
    return hasil

kalimat = input('Masukan Kalimat : ')
hasil = translet_to_alay(kalimat)
print(hasil)


class Queue :
    def __init__(self):
        self.data = []
    
    def enqueue(self, data) :
        self.data.append(data)

    def dequeue(self):
        if len(self.data) == 0:
            return
        else :
            return self.data.pop(0)

    def front(self):
        if len(self.data) == 0 :
            return 
        else :
            return self.data[0]
    
    def get_length(self) :
        return len(self.data)

    def write_all_data(self):
        print("DATA: ")
        for i, data in enumerate(self.data):
            print(f"{data}")



# Haram untuk menggunakan list
def get_min(queue):
    pass
def pop(queue):
    pass
    
# get_min('2')

if __name__ == "__main__":
    q : Queue = Queue()
    for i in [10, 8, 5, 60,1,2,3,4,100]:
        q.enqueue(i)
    print("==========")
    print("Data Awal")
    q.write_all_data()
    print("==========")
    print(f"Data terkecil = {get_min(q)}")
    print("==========")
    print()
    print("Pembuktian isi queue tidak berubah")
    print("==========")
    print("Data Akhir")
    q.write_all_data()
    print("==========")
    print()
    print("============")
    print("Percobaan Pop")
    print(f"pop - 1 = {pop(q)}")
    print(f"pop - 2 = {pop(q)}")
    print(f"pop - 3 = {pop(q)}")
    print("=============")
    print("Hasil Akhir: ")
    q.write_all_data()
    print("=============")
    # get_min(q)
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/zd2SoQbI)
# UG 8 QUEUE

## **TIDAK BOLEH MEMAKAI LIST**
## **HANYA BOLEH MEMAKAI METHOD YANG SUDAH DISEDIAKAN PADA QUEUE, TIDAK BOLEH AKSES DATA LANGSUNG**

## Ketentuan Tugas

Kerjakan pada file main.py, jangan di fie Kalian sendiri - sendiri karena akan menyusahkan diri Kalian sendiri. 

Di file main.py, kalian akan diberikan sebuah class bernama Queue yang merupakan pemodelan dari struktur data queue. class ini mempunyai fungsionalitas sebagai berikut:

- get_length() = Method ini mengembalikan banyak anggota yang ada dalam queueu.
- enqueue(data) = Method ini berfungsi untuk memasukkan sebuah data ke dalam queue.
- dequeue() = Method ini berfungsi untuk mengeluarkan data paling depan dari sebuah queue.
- front() = Method ini berfungsi untuk mengembalikan nilai paling depan dari sebuah queue.
- write_all_data() = menampilkan semua data pada queue

Tugas Kalian sekarang adalah melengkapi dua buah fungsi (ingat, fungsi ini berada di luar class), yaitu fungsi get_data(queue, index) dan fungsi get_min(queue). Penjelasan fungsi :


- get_min(queue) = Fungsi ini menerima parameter berupa sebuah objek Queue dan memiliki fungsi untuk mengembalikan nilai paling rendah dari queue tersebut
- pop(queue) = Queue hanya bisa melakukan pengeluaran data yang paling depan. Nah, sekarang, tugas kalian adalah untuk membuat fungsi bernama pop yang menerima parameter berupa sebuah objek Queue dan akan mengeluarkan data paling akhir serta sekaligus me-return data tersebut ke pengguna. Misal, ada sebuah Queue dengan data : 1,2,3,4,5. Jika pop() digunakan, maka data yang paling belakang, yaitu 5, akan dikeluarkan dan akan dikembalikan ke user.

Setelah melakukan kedua fungsi ini, queue **Tidak Boleh berubah isinya**. Ingat, jangan pakai list. Ketahuan pakai list maka konsekuensinya akan [isi sendiri]


### Test Case
```
if __name__ == "__main__":
    q : Queue = Queue()
    for i in [10, 8, 5, 60,1,2,3,4,100]:
        q.enqueue(i)
    print("==========")
    print("Data Awal")
    q.write_all_data()
    print("==========")
    print(f"Data terkecil = {get_min(q)}")
    print("==========")
    print()
    print("Pembuktian isi queue tidak berubah")
    print("==========")
    print("Data Akhir")
    q.write_all_data()
    print("==========")
    print()
    print("============")
    print("Percobaan Pop")
    print(f"pop - 1 = {pop(q)}")
    print(f"pop - 2 = {pop(q)}")
    print(f"pop - 3 = {pop(q)}")
    print("=============")
    print("Hasil Akhir: ")
    q.write_all_data()
    print("=============")
```
### Output
```
PS C:\Users\Gian\Documents\ukdw\ukdw smt5\asdos\minggu8> python .\kidung_jemaat.py
==========
Data Awal
DATA:
10
8
5
60
1
2
3
4
100
==========
Data terkecil = 1
==========

Pembuktian isi queue tidak berubah
==========
Data Akhir
DATA:
10
8
5
60
1
2
3
4
100
==========

============
Percobaan Pop
pop - 1 = 100
pop - 2 = 4
pop - 3 = 3
=============
Hasil Akhir:
DATA:
10
8
5
60
1
2
=============
PS C:\Users\Gian\Documents\ukdw\ukdw smt5\asdos\minggu8> 
```
