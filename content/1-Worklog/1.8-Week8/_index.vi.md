---
title: "Worklog Tuần 8"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 8:

* Phát triển quy trình Giỏ hàng (Cart) và lập trình các bước thanh toán đơn hàng.
* Tích hợp bản đồ địa lý Leaflet vào quy trình nhập thông tin giao nhận hàng (Shipping).
* Thiết kế trang tóm tắt và xác nhận đơn hàng PlaceOrder.
* **AWS Integration:** Kiểm thử luồng gửi dữ liệu đơn hàng phức tạp qua HTTPS tới dịch vụ ECS Backend thông qua Application Load Balancer (ALB).

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Xây dựng giao diện Giỏ hàng (Cart.jsx) quản lý danh sách sản phẩm chờ mua, thay đổi số lượng, xóa sản phẩm và áp dụng mã giảm giá (Coupon) | 08/06/2026 | 08/06/2026 | Tài liệu thiết kế NodeJ2Car |
| 3 | - Thiết kế trang nhập thông tin giao hàng (Shipping.jsx) thu thập thông tin khách hàng và hình thức nhận hàng | 09/06/2026 | 09/06/2026 | Tài liệu API NodeJ2Car |
| 4 | - Tích hợp bản đồ Leaflet (react-leaflet) vào trang Shipping để người dùng ghim vị trí địa lý giao hàng thuận tiện trên bản đồ trực quan | 10/06/2026 | 10/06/2026 | Hướng dẫn Leaflet API |
| 5 | - Thiết lập trang xác nhận đơn hàng (PlaceOrder.jsx) hiển thị tóm tắt chi phí, VAT và phí vận chuyển trước khi xác nhận đặt hàng | 11/06/2026 | 11/06/2026 | Tài liệu thiết kế Figma |
| 6 | - **AWS Integration:** Thiết lập và kiểm thử truyền nhận dữ liệu tạo đơn hàng phức tạp qua giao thức HTTPS gửi tới cụm ECS Backend nằm sau Application Load Balancer (ALB) | 12/06/2026 | 12/06/2026 | Hướng dẫn cấu hình AWS ALB |

### Kết quả đạt được tuần 8:

* Triển khai hoàn chỉnh module Giỏ hàng ở Client, tự động lưu thông tin giỏ hàng vào bộ nhớ để tránh mất dữ liệu khi F5.
* Tích hợp thành công bản đồ Leaflet cho phép định vị địa chỉ giao hàng chính xác, cải thiện đáng kể tốc độ điền form giao hàng.
* Giao diện PlaceOrder tính toán chi tiết chi phí hàng hóa chuẩn xác, đồng bộ hóa tốt với API thanh toán của Backend.
* Kết nối HTTPS qua ALB hoạt động ổn định, bảo vệ thông tin đơn hàng nhạy cảm của khách hàng trong quá trình truyền tải dữ liệu.


