---
title: "Worklog Tuần 13"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.13. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 13:

* Tích hợp dịch vụ tường lửa ứng dụng web AWS WAF (Web Application Firewall) bảo vệ hệ thống khỏi các mối đe dọa trực tuyến.
* Cấu hình Web ACLs trên biên CloudFront để lọc lưu lượng truy cập xấu, ngăn chặn tấn công DDoS.
* Thiết lập các quy tắc (Rules) kiểm soát truy cập và bảo vệ chống tấn công Brute Force tài khoản.
* Triển khai bộ quy tắc AWS WAF Bot Control để loại bỏ các bot quét lỗ hổng tự động.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu tài liệu lý thuyết về AWS WAF, các khái niệm Web ACL, Rule Groups và cách thức hoạt động của WAF | 13/07/2026 | 13/07/2026 | AWS WAF documentation |
| 3 | - Khởi tạo Web ACL trên vùng Global (phạm vi CloudFront) và thiết lập liên kết trực tiếp vào CloudFront Distribution của dự án | 14/07/2026 | 14/07/2026 | Hướng dẫn liên kết WAF |
| 4 | - **Rate Limiting Rule Setup:** Xây dựng quy tắc giới hạn tần suất yêu cầu (Rate Limit Rule) chặn các địa chỉ IP gửi yêu cầu quá mức để phòng chống DDoS lớp ứng dụng | 15/07/2026 | 15/07/2026 | AWS WAF Rate Limiting guides |
| 5 | - **Bot Control Policy:** Bật cấu hình bộ quy tắc AWS Managed Rules Bot Control để phân loại và tự động chặn đứng bot độc hại | 16/07/2026 | 16/07/2026 | AWS Bot Control reference |
| 6 | - **Log Monitoring & Tinh chỉnh:** Phân tích lưu lượng bị chặn thông qua biểu đồ WAF, tinh chỉnh các luật để giảm thiểu tối đa hiện tượng chặn nhầm (False Positives) | 17/07/2026 | 17/07/2026 | Giám sát AWS WAF |

### Kết quả đạt được tuần 13:

* Triển khai hoàn tất tường lửa AWS WAF bảo vệ đầu vào biên CloudFront CDN của hệ thống.
* Bảo vệ thành công trang web trước các đòn tấn công spam hoặc DDoS tần suất cao thông qua luật giới hạn IP tự động.
* Phát hiện và ngăn chặn hiệu quả các lượt rà quét bảo mật tự động từ bot xấu, bảo vệ an toàn cho cấu trúc dữ liệu và API Backend.
* Tối ưu hóa các chính sách loại trừ (exclusions) giúp hệ thống lọc chính xác các tác vụ độc hại mà vẫn đảm bảo tốc độ phản hồi cực tốt cho khách hàng thật.
