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

* Đóng gói mã nguồn React SPA (Vite) và triển khai lên AWS S3 hỗ trợ Static Website Hosting kết hợp SSL/HTTPS trên CloudFront.
* Tích hợp AWS WAF (Web Application Firewall) bảo vệ website khỏi tấn công DDoS và Bot quét tự động.
* Đo lường hiệu năng giao diện qua Google Lighthouse (Core Web Vitals) và tối ưu SEO.
* Cấu hình Cache-Control trên CloudFront, tiến hành kiểm thử End-to-End toàn hệ thống và bàn giao sản phẩm NodeJ2Car.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nén ảnh tĩnh, loại bỏ debug log, thực hiện phân tách mã (code splitting) <br> - Chạy câu lệnh `npm run build` đóng gói mã nguồn SPA ra thư mục `/dist` | 06/07/2026 | 06/07/2026 | Hướng dẫn build Vite |
| 3 | - **AWS S3 & CloudFront Deployment:** Đẩy tệp tĩnh lên S3 Web Bucket, bật Static Website Hosting. Tạo CloudFront Distribution trỏ Origin về S3, cấu hình Custom Error Response trỏ về index.html và gắn SSL từ ACM để chạy HTTPS | 07/07/2026 | 07/07/2026 | Hướng dẫn AWS S3/CloudFront |
| 4 | - **AWS WAF Integration:** Tạo và cấu hình chính sách AWS WAF gắn trực tiếp vào CloudFront Distribution để ngăn chặn các lượt quét tự động từ Bot và bảo vệ chống tấn công DDoS | 08/07/2026 | 08/07/2026 | Hướng dẫn AWS WAF |
| 5 | - Đo đạc cải thiện Core Web Vitals qua Google Lighthouse <br> - Cấu hình SEO: Tiêu đề động, các thẻ Meta sản phẩm và Open Graph phục vụ việc share link | 09/07/2026 | 09/07/2026 | Hướng dẫn SEO & Lighthouse |
| 6 | - **AWS Cache-Control:** Cấu hình Header Cache-Control cho CloudFront (tệp tĩnh cache lâu, index.html no-cache) <br> - Thực hiện End-to-End Testing toàn bộ hệ thống từ đăng ký, quét ảnh AI, đặt hàng, thanh toán đến chat và bàn giao dự án | 10/07/2026 | 10/07/2026 | Kế hoạch kiểm thử dự án |

### Kết quả đạt được tuần 12:

* Đóng gói mã nguồn SPA tối ưu, giảm hơn 35% kích thước gói tải ban đầu qua code splitting.
* Triển khai website chạy trực tiếp qua giao thức HTTPS bảo mật cao với tên miền tùy chỉnh qua CloudFront CDN.
* Thiết lập chính sách AWS WAF lọc sạch lưu lượng độc hại truy cập website.
* Đạt điểm Lighthouse Performance >92 trên cả Desktop và Mobile; SEO hiển thị thông tin hình ảnh sản phẩm sắc nét khi share mạng xã hội.
* Cấu hình Cache-Control chuẩn xác giúp trình duyệt lưu cache file CSS/JS lâu dài, trong khi tệp index.html luôn được làm mới để người dùng luôn nhận được Frontend cập nhật mới nhất.
* Bàn giao thành công dự án NodeJ2Car đạt chuẩn chất lượng yêu cầu.


