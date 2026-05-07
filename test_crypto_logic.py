from des_socket_utils import *
import os

def test_logic():
    key = b"8bytekey" 
    iv = b"8byteivv"
    message = "Tin nhan bi mat cua Phuong Anh".encode('utf-8')

    print(f"--- Bat dau test logic Crypto ---")
    ciphertext = encrypt_des_cbc(message, key, iv)
    packet = build_packet(key, iv, ciphertext)
    
    r_key, r_iv, r_ciphertext = parse_packet(packet)
    decrypted_msg = decrypt_des_cbc(r_ciphertext, r_key, r_iv)
    
    print(f"Bản rõ gốc: {message.decode('utf-8')}")
    print(f"Bản rõ sau giải mã: {decrypted_msg.decode('utf-8')}")

    if message == decrypted_msg:
        print("=> KET QUA: THANH CONG!")
    else:
        print("=> KET QUA: THAT BAI!")

if __name__ == "__main__":
    test_logic()