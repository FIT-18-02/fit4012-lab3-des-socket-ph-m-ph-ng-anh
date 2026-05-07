import socket
import os
from des_socket_utils import encrypt_des_cbc, build_packet

# Cấu hình kết nối
SERVER_IP = os.getenv("SERVER_IP", "127.0.0.1")
SERVER_PORT = int(os.getenv("SERVER_PORT", 6001))
MESSAGE = os.getenv("MESSAGE", "Xin chao FIT4012 - Day la tin nhan mat")

def run_sender():
    # 1. Khởi tạo Key (8B) và IV (8B) ngẫu nhiên
    key = os.urandom(8)
    iv = os.urandom(8)

    # 2. Mã hóa bản tin
    ciphertext = encrypt_des_cbc(MESSAGE.encode('utf-8'), key, iv)

    # 3. Đóng gói (Key + IV + Length + Ciphertext)
    packet = build_packet(key, iv, ciphertext)

    # 4. Gửi qua Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(packet)
            print(f"[SENDER] Da gui thanh cong!")
            print(f" - Key: {key.hex()}")
            print(f" - IV: {iv.hex()}")
            print(f" - Ciphertext: {ciphertext.hex()}")
        except ConnectionRefusedError:
            print("[ERROR] Khong the ket noi den Receiver. Hay chay receiver.py truoc!")

if __name__ == "__main__":
    run_sender()