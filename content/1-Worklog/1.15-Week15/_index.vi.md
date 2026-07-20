---
title: "Worklog Tuần 15"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.15. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 15:

* Thực hiện kiểm thử toàn trình End-to-End (E2E Testing) tích hợp các chức năng từ Client tới Cloud Server.
* Tổ chức rà soát chi phí, dọn dẹp tài nguyên thử nghiệm dư thừa trên tài khoản AWS.
* Bàn giao sản phẩm phần mềm NodeJ2Car đạt chuẩn chất lượng.
* Tổng hợp toàn bộ dữ liệu, hoàn thiện tệp tài liệu báo cáo thực tập và kết thúc quá trình thực tập tại công ty.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tiến hành E2E testing luồng người dùng: Đăng ký/Đăng nhập -> Quét ảnh phụ tùng AI -> Chọn sản phẩm -> Điền bản đồ định vị giao nhận | 27/07/2026 | 27/07/2026 | Kế hoạch kiểm thử dự án |
| 3 | - Kiểm thử E2E tích hợp cổng thanh toán (Stripe, VNPay, MoMo) kết hợp nhận phản hồi IPN từ Webhook Lambda và tương tác qua Socket.io Chat | 28/07/2026 | 28/07/2026 | Hướng dẫn kiểm thử tích hợp |
| 4 | - **AWS Resource Cleanup:** Thu hồi các tài nguyên dùng thử (các DB cluster không dùng, bản lưu backup nháp, log lưu trữ cũ) để tối ưu chi phí | 29/07/2026 | 29/07/2026 | AWS Cost Optimization |
| 5 | - Thực hiện bàn giao mã nguồn dự án, cấu hình AWS và hoàn tất hồ sơ, tài liệu báo cáo thực tập trước ngày kết thúc 30/07/2026 | 30/07/2026 | 30/07/2026 | Tài liệu bàn giao dự án |

### Kết quả đạt được tuần 15:

* Đảm bảo hệ thống vận hành trơn tru thông qua chuỗi kiểm thử E2E thành công 100% không phát sinh lỗi nghiêm trọng.
* Tối ưu hóa và kiểm soát ngân sách AWS bằng cách dọn dẹp triệt để các dịch vụ phát sinh chi phí nháp.
* Đóng gói mã nguồn Frontend và Backend cùng tài liệu cấu trúc hạ tầng mạng Cloud gửi về đội ngũ dự án.
* Hoàn thành và nộp báo cáo thực tập đầy đủ nội dung, kết thúc thời gian thực tập thành công rực rỡ vào ngày 30/07/2026.
