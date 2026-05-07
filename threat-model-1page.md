# Threat Model - Lab 3

## Thông tin nhóm
- Thành viên 1: Phạm Phương Anh - MSSV: 1871020062
- Thành viên 2: Vũ Quốc Anh - MSSV: 1871020066

## Assets
- Bản tin gốc (Plaintext): Nội dung thông tin nhạy cảm cần trao đổi giữa Sender và Receiver.

- Khóa bí mật (Key): Dùng để mã hóa/giải mã dữ liệu, nếu mất key thì mọi bảo mật đều vô nghĩa.

- Vector khởi tạo (IV): Dùng trong chế độ CBC để đảm bảo các bản mã không bị trùng lặp khi nội dung giống nhau.

## Attacker model
Đối tượng tấn công là những kẻ nghe lén trên đường truyền mạng (Man-in-the-Middle - MitM). Kẻ tấn công có khả năng:

- Đọc trộm dữ liệu di chuyển qua các nút mạng (Sniffing).

- Thu giữ và chỉnh sửa gói tin trước khi nó đến đích (Tampering).

- Giả mạo gói tin để lừa Receiver giải mã thông tin sai lệch.

## Threats
- Eavesdropping (Nghe lén): Vì Key và IV được gửi kèm ngay trong gói tin trên cùng luồng TCP không mã hóa, kẻ tấn công có thể dễ dàng lấy được toàn bộ "chìa khóa" để giải mã bản tin.

- Data Tampering (Thay đổi dữ liệu): Kẻ tấn công có thể thay đổi các bit trong bản mã (Ciphertext), dẫn đến việc Receiver giải mã ra nội dung rác hoặc bị sai lệch ý nghĩa.

- Replay Attack (Tấn công phát lại): Kẻ tấn công có thể thu giữ gói tin hợp lệ và gửi lại nhiều lần cho Receiver để gây nhiễu hoặc thực hiện lại một hành động nào đó.

## Mitigations
- Key Exchange (Trao đổi khóa an toàn): Không gửi Key trực tiếp qua Socket. Thay vào đó, sử dụng các thuật toán như Diffie-Hellman hoặc bọc toàn bộ luồng dữ liệu trong TLS/SSL (HTTPS/WSS).

- Data Integrity (Kiểm tra tính toàn vẹn): Sử dụng thêm các hàm băm (Hash) hoặc mã xác thực bản tin (HMAC) để Receiver có thể kiểm tra xem gói tin có bị chỉnh sửa trên đường đi hay không.

- Encryption Layer: Sử dụng các thuật toán mã hóa mạnh hơn (như AES) thay cho DES vốn đã cũ và dễ bị tấn công vét cạn (Brute-force).

## Residual risks
Ngay cả khi đường truyền được bảo mật, vẫn còn rủi ro Endpoint Security: Nếu máy tính của Sender hoặc Receiver bị cài mã độc (Trojan/Keylogger), kẻ tấn công vẫn có thể đánh cắp bản tin ngay tại bộ nhớ RAM trước khi nó kịp mã hóa hoặc sau khi vừa giải mã xong.
