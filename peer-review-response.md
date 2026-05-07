# Peer Review Response

## Thông tin nhóm
- Thành viên 1: Phạm Phương Anh - MSSV: 1871020062
- Thành viên 2: Vũ Quốc Anh - MSSV: 1871020066

## Thành viên 1 góp ý cho thành viên 2
Quốc Anh đã triển khai phần Socket rất tốt, kết nối ổn định và xử lý dữ liệu nhị phân chính xác. Cần lưu ý thêm về việc đóng kết nối (close socket) ngay sau khi nhận đủ dữ liệu để tránh treo cổng.

## Thành viên 2 góp ý cho thành viên 1
Phương Anh xử lý logic mã hóa DES-CBC rất chắc chắn, phần Padding PKCS#7 viết rất chuẩn giúp việc giải mã không bị lỗi. Nên tối ưu thêm phần tạo Key/IV ngẫu nhiên để tăng tính bảo mật cho mỗi phiên gửi.

## Nhóm đã sửa gì sau góp ý
Sau khi review chéo, nhóm đã thực hiện các chỉnh sửa sau:

- Bổ sung lệnh conn.close() và s.close() vào cả hai file để quản lý tài nguyên tốt hơn.

- Tối ưu lại hàm pad và unpad trong file des_socket_utils.py để xử lý ngoại lệ khi dữ liệu rỗng.

- Cập nhật thêm các chú thích (comment) vào code để bạn cùng nhóm dễ đọc và hiểu luồng đi của dữ liệu hơn.
