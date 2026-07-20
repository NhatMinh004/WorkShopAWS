---
title: "Worklog Tuần 12"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.12 </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 12:

* Đóng gói mã nguồn React SPA (Vite) tối ưu hóa tài nguyên tĩnh.
* Triển khai lưu trữ web tĩnh lên Amazon S3 hỗ trợ Static Website Hosting.
* Tạo và cấu hình Amazon CloudFront Distribution để phân phối nội dung tĩnh tại biên.
* Đăng ký chứng chỉ bảo mật SSL/TLS từ AWS Certificate Manager (ACM) tích hợp HTTPS cho tên miền tùy chỉnh.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nén ảnh tĩnh, loại bỏ debug log, thực hiện phân tách mã (code splitting) <br> - Chạy câu lệnh `npm run build` đóng gói mã nguồn SPA ra thư mục `/dist` | 06/07/2026 | 06/07/2026 | Hướng dẫn build Vite |
| 3 | - **AWS S3 Deployment:** Đẩy tệp tĩnh lên S3 Web Bucket, kích hoạt tính năng Static Website Hosting và cấu hình Bucket Policy cho phép CloudFront OAI/OAC truy cập | 07/07/2026 | 07/07/2026 | Hướng dẫn AWS S3 |
| 4 | - **CloudFront CDN Setup:** Tạo CloudFront Distribution trỏ Origin về S3, cấu hình Custom Error Response (403/404) chuyển hướng về index.html phục vụ định tuyến React SPA | 08/07/2026 | 08/07/2026 | Hướng dẫn CloudFront |
| 5 | - **ACM SSL Certificate:** Yêu cầu chứng chỉ SSL/TLS miễn phí từ ACM cho tên miền phụ thực tập và cấu hình DNS CNAME validation | 09/07/2026 | 09/07/2026 | Tài liệu AWS ACM |
| 6 | - **Domain Binding & Verification:** Liên kết chứng chỉ ACM SSL và tên miền tùy chỉnh vào CloudFront Distribution, kiểm tra định tuyến truy cập HTTPS | 10/07/2026 | 10/07/2026 | Cấu hình DNS Route 53 |

### Kết quả đạt được tuần 12:

* Đóng gói mã nguồn SPA tối ưu, giảm hơn 35% kích thước gói tải ban đầu qua code splitting.
* Triển khai website chạy trực tiếp qua giao thức HTTPS bảo mật cao với tên miền tùy chỉnh qua CloudFront CDN.
* Cấu hình CloudFront Custom Error Response giúp React Router định tuyến trang con mượt mà, không gặp lỗi HTTP 403/404 khi tải lại trang (reload).
* Chứng chỉ SSL từ ACM được liên kết hoàn chỉnh, kích hoạt kết nối bảo mật toàn trình.


