# Fungsi untuk enkripsi menggunakan Caesar Cipher dengan pergeseran berdasarkan nomor absen
def caesar_encrypt(plaintext, shift):
    ciphertext = []
    
    for letter in plaintext:
        if letter.isalpha():  # Hanya mengenkripsi huruf
            shift_base = ord('A') if letter.isupper() else ord('a')
            encrypted_letter = chr((ord(letter) - shift_base + shift) % 26 + shift_base)
            ciphertext.append(encrypted_letter)
        else:
            ciphertext.append(letter)  # Non-huruf tidak berubah
    
    return ''.join(ciphertext)

# Fungsi untuk dekripsi menggunakan Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    plaintext = []
    
    for letter in ciphertext:
        if letter.isalpha():  # Hanya mendekripsi huruf
            shift_base = ord('A') if letter.isupper() else ord('a')
            decrypted_letter = chr((ord(letter) - shift_base - shift) % 26 + shift_base)
            plaintext.append(decrypted_letter)
        else:
            plaintext.append(letter)  # Non-huruf tidak berubah
    
    return ''.join(plaintext)

# Nama yang akan dienkripsi
name = "Ammar Dzaki Naufal Ali"
# Kunci pergeseran berdasarkan nomor absen (1)
shift = 1

# Enkripsi nama
ciphertext = caesar_encrypt(name, shift)
print(f"Ciphertext: {ciphertext}")

# Dekripsi nama
decrypted_text = caesar_decrypt(ciphertext, shift)
print(f"Decrypted Text: {decrypted_text}")

# Penjelasan Program
#Fungsi caesar_encrypt mengenkripsi teks dengan Caesar Cipher, menggunakan pergeseran sesuai dengan nomor absen. Setiap huruf digeser ke kanan sejumlah nilai pergeseran (1 dalam hal ini).
#Fungsi caesar_decrypt mengembalikan teks terenkripsi ke teks asli dengan melakukan operasi kebalikan (menggeser huruf kembali ke kiri).
#Nama yang dienkripsi adalah "Ammar Dzaki Naufal Ali," dan kunci pergeseran adalah 1 karena nomor absen Naufal adalah 1.