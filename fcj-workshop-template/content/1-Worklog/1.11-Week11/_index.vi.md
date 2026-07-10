---
title: "Worklog Tuần 11"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 11:

* Phát triển Phân hệ Quản trị (Admin Dashboard) với các chức năng quản lý sản phẩm phụ tùng, đơn hàng và tạo mã giảm giá.
* Tích hợp các biểu đồ phân tích số liệu kinh doanh sử dụng thư viện Recharts.
* Thiết lập trang kiểm duyệt chat hỗ trợ khách hàng của quản trị viên.
* **AWS Integration:** Đảm bảo bảo mật phân hệ quản trị thông qua token JWT và định tuyến yêu cầu API qua ALB tới cụm ECS Backend.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Phát triển giao diện quản lý danh sách phụ tùng (thêm/sửa/xóa sản phẩm, cập nhật thông số kỹ thuật) | 29/06/2026 | 29/06/2026 | Tài liệu thiết kế NodeJ2Car |
| 3 | - Xây dựng chức năng quản lý đơn hàng: cập nhật trạng thái đơn hàng, theo dõi giao hàng cho khách | 30/06/2026 | 30/06/2026 | Tài liệu API NodeJ2Car |
| 4 | - Phát triển trang quản lý khuyến mãi, tạo và phân phối mã giảm giá (coupon) cho khách hàng | 01/07/2026 | 01/07/2026 | Tài liệu thiết kế Figma |
| 5 | - Tích hợp các biểu đồ phân tích doanh thu, tăng trưởng đơn hàng sử dụng thư viện Recharts để trực quan hóa số liệu | 02/07/2026 | 02/07/2026 | Recharts API Reference |
| 6 | - Thiết kế trang kiểm duyệt tin nhắn hỗ trợ khách hàng của Admin <br> - **AWS Integration:** Kiểm thử các API quản trị chuyên sâu trên ECS thông qua ALB, đảm bảo kiểm tra quyền admin nghiêm ngặt bằng JWT | 03/07/2026 | 03/07/2026 | Hướng dẫn phân quyền AWS |

### Kết quả đạt được tuần 11:

* Xây dựng phân hệ Admin Dashboard hoàn chỉnh với giao diện khoa học, quản trị dữ liệu dễ dàng.
* Nhúng biểu đồ trực quan Recharts biểu diễn doanh số bán hàng, giúp người dùng nắm bắt nhanh diễn biến tăng trưởng kinh doanh.
* Xây dựng thành công hệ thống kiểm duyệt chat của Admin, nhận tin từ khách hàng tức thời qua Socket.io.
* Đảm bảo an toàn tuyệt đối cho phân hệ quản trị nhờ lọc quyền JWT chặt chẽ từ Frontend và kiểm soát ở AWS ALB Gateway.


