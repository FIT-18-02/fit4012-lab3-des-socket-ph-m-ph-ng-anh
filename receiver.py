import socket
import os
from des_socket_utils import parse_packet, decrypt_des_cbc

LISTEN_IP = "0.0.0.0" # Lang nghe moi ket noi den
LISTEN_PORT = int(os.getenv("RECEIVER_PORT", 6001))

def run_receiver():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((LISTEN_IP, LISTEN_PORT))
        s.listen(1)
        print(f"[RECEIVER] Dang cho ket noi tai cong {LISTEN_PORT}...")

        conn, addr = s.accept()
        with conn:
            print(f"[RECEIVER] Ket noi tu: {addr}")
            # Doc du lieu (Toi da 1024 byte cho bai lab nay)
            data = conn.recv(1024)
            if data:
                # 1. Rã gói tin
                key, iv, ciphertext = parse_packet(data)
                
                # 2. Giải mã
                try:
                    decrypted_msg = decrypt_des_cbc(ciphertext, key, iv)
                    print(f"\n[!] BAN TIN GIAI MA THANH CONG:")
                    print(f" >> {decrypted_msg.decode('utf-8')}")
                except Exception as e:
                    print(f"[ERROR] Loi giai ma hoac Padding: {e}")

if __name__ == "__main__":
    run_receiver()