---
title: "Worklog Tuần 10"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.10. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 10:

* Tích hợp hộp thoại Chat thời gian thực (Real-time Chat) và hệ thống thông báo tức thời (Notification System) sử dụng WebSockets.
* Xây dựng widget chat cho khách hàng và trang quản trị chat cho Admin.
* **AWS Integration:** Cấu hình kết nối WebSocket đi qua AWS Application Load Balancer (ALB) kết hợp Sticky Sessions để duy trì kết nối ổn định.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Cài đặt thư viện socket.io-client để kết nối thời gian thực với máy chủ WebSocket Backend | 22/06/2026 | 22/06/2026 | Hướng dẫn Socket.io Client |
| 3 | - Phát triển widget Chat nổi góc dưới màn hình cho khách hàng tương tác trực tiếp với quản trị viên | 23/06/2026 | 23/06/2026 | Tài liệu thiết kế NodeJ2Car |
| 4 | - Thiết kế giao diện trang nhắn tin quản trị (admin/chat) dành riêng cho nhân viên hỗ trợ xử lý nhiều luồng chat song song | 24/06/2026 | 24/06/2026 | Tài liệu giao diện Admin |
| 5 | - Lập trình luồng nhận tin nhắn và hiển thị huy hiệu thông báo (Notification Badge) tức thời ở thanh tiêu đề (Header) khi có tin nhắn mới hoặc thông báo ưu đãi từ Admin | 25/06/2026 | 25/06/2026 | Hướng dẫn State Management |
| 6 | - **AWS Integration:** Cấu hình Client-side tương thích với Application Load Balancer (ALB) sử dụng Sticky Sessions, đảm bảo kết nối WebSocket luôn được neo vào đúng container Backend ban đầu | 26/06/2026 | 26/06/2026 | Tài liệu AWS ALB Sticky Sessions |

### Kết quả đạt được tuần 10:

* Thiết lập thành công kết nối thời gian thực qua socket.io-client, giao tiếp hai chiều không bị trễ.
* Giao diện Chat của khách hàng và Admin hiển thị thân thiện, hỗ trợ gửi nhận tin nhắn văn bản và biểu tượng cảm xúc mượt mà.
* Huy hiệu thông báo đỏ cập nhật tức thời khi có sự kiện mới, kích thích tương tác của khách hàng.
* Duy trì kết nối WebSocket ổn định qua ALB nhờ cấu hình chuẩn xác Sticky Sessions, giải quyết hoàn toàn lỗi mất handshake WebSocket trong môi trường container tải động của ECS.


