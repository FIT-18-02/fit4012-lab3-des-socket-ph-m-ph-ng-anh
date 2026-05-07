# Threat Model - Hệ thống gửi nhận dữ liệu DES qua Socket

## 1. Assets (Tài sản cần bảo vệ)
* **Dữ liệu người dùng (Plaintext):** Nội dung thông tin nhạy cảm được gửi đi.
* **DES Key & IV:** "Chìa khóa" dùng để mã hóa và giải mã.
* **Luồng giao tiếp:** Sự ổn định của kết nối TCP giữa Sender và Receiver.

## 2. Attacker Model (Mô hình kẻ tấn công)
* **Passive Attacker (Kẻ tấn công thụ động):** Nghe lén gói tin trên đường truyền (Sniffing) trong cùng mạng LAN hoặc Wi-Fi công cộng.
* **Active Attacker (Kẻ tấn công chủ động):** Chặn và thay đổi dữ liệu (Man-in-the-Middle), gửi các gói tin rác để làm treo hệ thống.

## 3. Threats (Mối đe dọa)
* **Lộ khóa (Key Exposure):** Do Key và IV được gửi dưới dạng plaintext ngay đầu gói tin, kẻ tấn công chỉ cần bắt được gói tin là có thể giải mã toàn bộ dữ liệu.
* **Mất tính toàn vẹn (Integrity Violation):** Kẻ tấn công có thể sửa đổi Ciphertext hoặc Header độ dài khiến Receiver giải mã ra dữ liệu sai hoặc bị crash.
* **Tấn công lặp lại (Replay Attack):** Kẻ tấn công bắt gói tin hợp lệ và gửi lại nhiều lần cho Receiver.

## 4. Mitigations (Biện pháp giảm thiểu)
* **Trao đổi khóa an toàn:** Sử dụng RSA hoặc Diffie-Hellman để trao đổi khóa thay vì gửi trực tiếp qua Socket.
* **Xác thực thông điệp:** Sử dụng HMAC hoặc chữ ký số để đảm bảo gói tin không bị sửa đổi.
* **Mã hóa kênh truyền:** Sử dụng TLS/SSL (HTTPS) để bảo vệ toàn bộ luồng dữ liệu.

## 5. Residual Risks (Rủi ro còn tồn tại)
* **Endpoint Security:** Nếu máy tính của Sender hoặc Receiver bị nhiễm mã độc, kẻ tấn công vẫn có thể lấy được bản rõ trước khi mã hóa hoặc sau khi giải mã.
* **DES yếu:** Thuật toán DES có độ dài khóa ngắn (56-bit), hiện nay có thể bị phá mã bằng phương pháp vét cạn (Brute-force) trong thời gian ngắn.