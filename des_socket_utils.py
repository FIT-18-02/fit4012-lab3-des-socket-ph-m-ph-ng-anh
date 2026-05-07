from Crypto.Cipher import DES
import struct

def pad_pkcs7(data):
    padding_len = 8 - (len(data) % 8)
    return data + bytes([padding_len] * padding_len)

def unpad_pkcs7(data):
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_des_cbc(plaintext_bytes, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_data = pad_pkcs7(plaintext_bytes)
    return cipher.encrypt(padded_data)

def decrypt_des_cbc(ciphertext_bytes, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext_bytes)
    return unpad_pkcs7(decrypted_padded)

def build_packet(key, iv, ciphertext):
    header = struct.pack("!I", len(ciphertext))
    return key + iv + header + ciphertext

def parse_packet(packet_bytes):
    key = packet_bytes[0:8]
    iv = packet_bytes[8:16]
    header = packet_bytes[16:20]
    ciphertext_len = struct.unpack("!I", header)[0]
    ciphertext = packet_bytes[20 : 20 + ciphertext_len]
    return key, iv, ciphertext