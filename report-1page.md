# Report 1 page - Lab 3

## Thông tin nhóm
- Thành viên 1: Phạm Phương Anh - MSSV: 1871020062
- Thành viên 2: Vũ Quốc Anh - MSSV: 1871020066

## Mục tiêu
Mục tiêu của bài lab này là xây dựng một hệ thống truyền nhận dữ liệu an toàn thông qua kết nối TCP Socket. Nhóm tập trung vào việc áp dụng thuật toán mã hóa đối xứng DES (Data Encryption Standard) ở chế độ CBC (Cipher Block Chaining) để bảo vệ tính bí mật của bản tin. Thông qua đó, nhóm hiểu rõ quy trình đóng gói dữ liệu bao gồm Key, IV và Ciphertext, đồng thời nhận diện được các nguy cơ bảo mật trong việc quản lý khóa khi truyền tin trên mạng.

## Phân công thực hiện
- Phạm Phương Anh: Phụ trách chính phần Crypto (thiết lập thuật toán DES, xử lý padding PKCS#7) và viết kịch bản gửi tin cho sender.py.
- Vũ Quốc Anh: Phụ trách phần Socket (thiết lập Server/Client, quản lý cổng 6001) và xây dựng logic nhận tin cho receiver.py.
- Phần làm chung: Thực hiện kiểm thử (Testing), chụp ảnh log minh chứng, xây dựng Threat Model và hoàn thiện tài liệu báo cáo.
## Cách làm
Nhóm triển khai hệ thống gồm ba thành phần chính:

- des_socket_utils.py: Chứa các hàm bổ trợ để mã hóa/giải mã DES, tự động thêm/xóa padding và đóng gói gói tin.

- Sender: Tạo khóa (Key) và Vector khởi tạo (IV) ngẫu nhiên cho mỗi phiên, mã hóa bản tin gốc rồi gửi toàn bộ gói tin qua Socket.

- Receiver: Lắng nghe tại cổng 6001, bóc tách gói tin để lấy Key/IV nhằm giải mã chính xác bản tin nhận được.
 Hệ thống được kiểm thử bằng cách chạy song song hai Terminal trong VS Code để quan sát luồng dữ liệu thời gian thực.
## Kết quả
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/17c35ccb-7af5-49a7-862f-6bd7fa1c78eb" />
- Minh chứng: Phía Receiver đã giải mã thành công bản tin với nội dung: Xin chao FIT4012 - Day la tin nhan mat.

- Log: Các thông số Key, IV và Ciphertext được in ra chi tiết ở phía Sender trước khi gửi.

- Kiểm thử: Đã vượt qua các ca kiểm thử về tính toàn vẹn dữ liệu và logic giải mã.

## Kết luận
- Bài học kỹ thuật: Nắm vững kỹ thuật lập trình Socket đa luồng và cách xử lý dữ liệu nhị phân trong Python.

- Bài học bảo mật: Hiểu rằng việc gửi kèm Key và IV cùng với bản mã mà không có kênh truyền bảo mật (như TLS) là một rủi ro lớn, dễ bị tấn công nghe lén (Eavesdropping).
