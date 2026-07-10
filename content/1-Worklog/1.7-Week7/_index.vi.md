---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 7:

* Xây dựng giao diện các trang chủ chốt của cửa hàng gồm Trang chủ (Home), trang Cửa hàng (Shop) có bộ lọc và trang Sơ đồ xe tương tác (Schematic).
* Thiết kế trang Chi tiết phụ tùng (PartDetail), trang So sánh (Compare) và danh sách yêu thích (Wishlist).
* **AWS Integration:** Kết nối hiển thị ảnh sản phẩm từ Amazon S3 Media Bucket và cấu hình tối ưu tải ảnh qua Amazon CloudFront CDN.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Thiết kế Trang chủ (Home.jsx) hiển thị banner động giới thiệu sản phẩm nổi bật và thương hiệu đối tác | 01/06/2026 | 01/06/2026 | Tài liệu thiết kế NodeJ2Car |
| 3 | - Xây dựng trang Cửa hàng (Shop.jsx) tích hợp thanh bộ lọc thông minh (lọc theo giá, hãng xe, chủng loại phụ tùng) và phân trang dữ liệu | 02/06/2026 | 02/06/2026 | Tài liệu API NodeJ2Car |
| 4 | - Lập trình trang sơ đồ xe tương tác (Schematic.jsx) cho phép người dùng click trực quan vào các phần trên bản vẽ xe hơi (như phanh, bánh xe, động cơ) để chuyển hướng tìm phụ tùng | 03/06/2026 | 03/06/2026 | Bản vẽ SVG xe hơi |
| 5 | - Xây dựng trang Chi tiết phụ tùng (PartDetail.jsx) hiển thị chi tiết thông số lắp ráp, mô tả kỹ thuật và đánh giá sản phẩm | 04/06/2026 | 04/06/2026 | Tài liệu sản phẩm |
| 6 | - Phát triển chức năng so sánh (Compare.jsx) và danh sách yêu thích (Wishlist.jsx) sử dụng localStorage <br> - **AWS Integration:** Liên kết hiển thị ảnh sản phẩm từ Amazon S3 Media Bucket thông qua đường dẫn tối ưu CDN của Amazon CloudFront | 05/06/2026 | 05/06/2026 | Hướng dẫn Amazon CloudFront |

### Kết quả đạt được tuần 7:

* Hoàn thành giao diện Trang chủ bắt mắt và trang Cửa hàng có bộ lọc hoạt động chính xác với API Backend.
* Phát triển thành công trang Sơ đồ xe tương tác SVG (Schematic.jsx), nâng cao trải nghiệm người dùng khi tìm kiếm phụ tùng.
* Hoàn thiện trang Chi tiết phụ tùng đầy đủ thông tin kỹ thuật cùng các widget So sánh và Yêu thích.
* Liên kết thành công hệ thống lưu trữ hình ảnh trên Amazon S3 Media Bucket với giao diện Frontend.
* Cấu hình CloudFront CDN làm trung gian phân phối ảnh, giúp giảm đáng kể độ trễ tải trang và tiết kiệm băng thông cho S3 Bucket.


