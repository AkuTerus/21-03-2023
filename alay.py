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
