def hitung_vokal(kalimat):
    vokal = 'aiueoAIUEO'#Siapkan daftar huruf vokal
    jumlah = 0
    for karakter in kalimat:
        if karakter in vokal:
            jumlah = jumlah+1
    return jumlah

def hitung_white_space(kalimat):
    jumlah = 0
    for karakter in kalimat:
        if karakter.isspace()==True:
            jumlah=jumlah+1
    return jumlah

def hitung_konsonan(kalimat):
    #konsonan = alfabet(a-z,A-Z) - vokal (aiueo,AIUEO) 
    vokal = 'aiueoAIUEO'
    jumlah = 0
    for karakter in kalimat:
        if karakter in kalimat:
            if karakter not in vokal and karakter.isalpha():
                jumlah=jumlah+1
    return jumlah


#Input
kalimat = input('masukan Sebuah kalimat: ')

#Proses
jumlah_vokal=hitung_vokal(kalimat)
jumlah_whitespace=hitung_white_space(kalimat)
jumlah_huruf_mati=hitung_konsonan(kalimat)

#Output
print(f'Jumlah Huruf vokal : {jumlah_vokal}')
print(f'Jumlah White Space : {jumlah_whitespace}')
print(f'Jumlah Huruf Konsonan : {jumlah_huruf_mati}')
