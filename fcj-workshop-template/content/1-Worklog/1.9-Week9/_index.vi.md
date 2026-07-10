---
title: "Worklog Tuần 9"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 9:

* Tích hợp giao diện quét ảnh phụ tùng hỏng bằng AI (AI Scan UI) và kết nối camera thiết bị di động.
* Thiết kế trang chọn phương thức thanh toán, xử lý điều hướng sang cổng thanh toán MoMo, VNPay, Stripe.
* Xây dựng trang kết quả đơn hàng (OrderResult) hiển thị trạng thái thanh toán sinh động dựa trên Query Parameters.
* **AWS Integration:** Lưu trữ ảnh quét lên Amazon S3 Media Bucket và sử dụng AWS Lambda Webhook Handler đồng bộ hóa trạng thái IPN.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Thiết kế nút chụp/tải ảnh phụ tùng hỏng trên thanh tìm kiếm và trang sản phẩm <br> - Tích hợp camera thiết bị di động để chụp ảnh trực tiếp và gửi lên API | 15/06/2026 | 15/06/2026 | Hướng dẫn camera API |
| 3 | - Xây dựng hiệu ứng chờ Skeleton Loading & micro-animations trong quá trình AI phân tích ảnh <br> - Lập trình hiển thị nhãn phụ tùng phát hiện và các đề xuất mua hàng | 16/06/2026 | 16/06/2026 | Tài liệu thiết kế Figma |
| 4 | - **AWS Integration (S3):** Cấu hình đẩy ảnh quét chụp từ Frontend lưu trữ trực tiếp vào Amazon S3 Media Bucket để lưu vết lịch sử tìm kiếm hình ảnh | 17/06/2026 | 17/06/2026 | AWS S3 SDK Guide |
| 5 | - Xây dựng trang Lựa chọn hình thức thanh toán (Payment.jsx) <br> - Lập trình chuyển hướng (Redirect) sang cổng thanh toán ngoài (VNPay, MoMo, Stripe) | 18/06/2026 | 18/06/2026 | Hướng dẫn tích hợp cổng thanh toán |
| 6 | - Thiết kế trang kết quả đơn hàng (OrderResult.jsx) đón người quay lại từ cổng thanh toán và trích xuất dữ liệu query <br> - **AWS Integration (Lambda):** Kiểm thử luồng đồng bộ trạng thái đơn hàng qua AWS Lambda (Webhook IPN) giúp giao diện cập nhật ngay lập tức | 19/06/2026 | 19/06/2026 | Hướng dẫn AWS Lambda |

### Kết quả đạt được tuần 9:

* Hoàn thành giao diện AI Scan UI mượt mà, hỗ trợ camera trên mọi thiết bị di động chụp hình trực tiếp.
* Tích hợp thành công hiệu ứng Skeleton Loading đẹp mắt tạo trải nghiệm chờ tự nhiên cho người dùng.
* Lưu trữ thành công ảnh chụp phụ tùng hỏng lên S3 Media Bucket của AWS để phục vụ phân tích dữ liệu sau này.
* Quy trình điều hướng thanh toán VNPay, MoMo, Stripe hoạt động trơn tru, bảo mật.
* Trang OrderResult bắt chính xác mã giao dịch quay về. Kết nối đồng bộ với AWS Lambda Webhook hoạt động tức thời, đảm bảo khi người dùng quay lại web thì trạng thái đơn hàng đã được cập nhật là "Thành công" trên UI.


