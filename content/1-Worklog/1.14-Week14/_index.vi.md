---
title: "Worklog Tuần 14"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.14. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 14:

* Đo đạc và nâng cao hiệu năng Frontend thông qua công cụ Google Lighthouse (Core Web Vitals).
* Cấu hình SEO tối ưu hóa trang web với các thẻ meta, Open Graph phục vụ việc chia sẻ mạng xã hội.
* Thiết lập chính sách bộ nhớ đệm Cache-Control cho CloudFront CDN nhằm tối ưu hóa tốc độ tải trang.
* Cấu hình các cơ chế tự động xóa bộ nhớ đệm (Cache Invalidation) khi triển khai phiên bản mới.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Chạy đánh giá Lighthouse ban đầu trên website, ghi nhận các chỉ số LCP, CLS, TBT để lập danh sách cải thiện | 20/07/2026 | 20/07/2026 | Google Lighthouse handbook |
| 3 | - Thực hiện tối ưu mã nguồn: nén ảnh định dạng WebP, thiết lập Lazy Loading cho các component phụ tùng nặng | 21/07/2026 | 21/07/2026 | Tối ưu Core Web Vitals |
| 4 | - Tích hợp thẻ tiêu đề động và thẻ Meta mô tả sản phẩm (SEO Meta Tags), cấu hình Open Graph cho liên kết chia sẻ | 22/07/2026 | 22/07/2026 | Tài liệu SEO Best Practices |
| 5 | - **AWS Cache-Control:** Thiết lập các Header Cache-Control trên S3 Metadata (tài nguyên JS/CSS cache lâu dài, index.html no-cache) | 23/07/2026 | 23/07/2026 | AWS Cache-Control guides |
| 6 | - **CloudFront Invalidation:** Tạo lệnh invalidation làm sạch cache trên CloudFront, kiểm tra cập nhật mã nguồn tức thời trên trình duyệt | 24/07/2026 | 24/07/2026 | Hướng dẫn CloudFront Caching |

### Kết quả đạt được tuần 14:

* Đạt điểm Lighthouse Performance vượt trên 92 cho cả hai phiên bản Desktop và Mobile.
* Hiển thị đầy đủ thông tin xem trước của sản phẩm (ảnh, tiêu đề, giá) khi chia sẻ đường dẫn trên mạng xã hội nhờ cấu hình Open Graph chuẩn.
* Giảm hơn 50% thời gian tải trang ở những lần truy cập sau nhờ cấu hình Cache-Control chuẩn xác trên CloudFront CDN.
* Đảm bảo trình duyệt luôn tự động nạp giao diện mới nhất nhờ luật cache no-store cho file index.html.
