---
title: "Worklog Tuần 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 4:

* Tìm hiểu chi tiết các tính năng tính toán nâng cao của EC2 bao gồm: Instance Types, AMI, EBS, Instance Store, User Data, Metadata và Auto Scaling.
* Thực hành giải pháp sao lưu tự động cho hệ thống máy chủ bằng dịch vụ AWS Backup.
* Xây dựng giải pháp lưu trữ lai Hybrid Storage thông qua AWS Storage Gateway kết nối từ On-premises lên AWS S3.
* Triển khai website tĩnh bảo mật cao trên Amazon S3 kết hợp mạng phân phối nội dung Amazon CloudFront CDN.
* Tìm hiểu và cấu hình cơ chế quản lý phiên bản (Versioning) và sao chép đối tượng S3 giữa các Region khác nhau (Cross-Region Replication).

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Nghiên cứu EC2 chuyên sâu:** <br>&emsp; + Module 03-01 - Compute VM on AWS <br>&emsp; + Module 03-01-01 - Instance type <br>&emsp; + Module 03-01-02 - AMI / Backup / Key Pair <br>&emsp; + Module 03-01-03 - Elastic block store <br>&emsp; + Module 03-01-04 - Instance store <br>&emsp; + Module 03-01-05 - User data <br>&emsp; + Module 03-01-06 - Meta data <br>&emsp; + Module 03-01-07 - EC2 auto scaling <br>&emsp; + Module-03-02 - EC2 Autoscaling - EFS/FSx - Lightsail - MGN | 11/05/2026 | 11/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Thực hành Lab AWS Backup:** <br>&emsp; + Module 03-Lab13-01 - Deploy AWS Backup to the System - Introduction <br>&emsp; + Module 03-Lab13-02.2 - Deploy infrastructure <br>&emsp; + Module 03-Lab13-03 - Create Backup plan <br>&emsp; + Module 03-Lab13-05 - Test Restore <br>&emsp; + Module 03-Lab13-06 - Clean up resources | 12/05/2026 | 12/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Thực hành Lab Storage Gateway:** <br>&emsp; + Module 03-Lab24-01.1 - Create S3 Bucket <br>&emsp; + Module 03-Lab24-01.2 - Create EC2 for Storage Gateway <br>&emsp; + Module 03-Lab24-02.1 - Create Storage Gateway <br>&emsp; + Module 03-Lab24-02.2 - Create File Shares | 13/05/2026 | 13/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Xây dựng S3 Static Website:** <br>&emsp; + Module 03-Lab57-02.1 - Create S3 bucket <br>&emsp; + Module 03-Lab57-02.2 - Load data <br>&emsp; + Module 03-Lab57-03 - Enable static website feature <br>&emsp; + Module 03-Lab57-04 - Configuring public access block <br>&emsp; + Module 03-Lab57-05 - Configuring public objects <br>&emsp; + Module 03-Lab57-06 - Test website | 14/05/2026 | 14/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Cấu hình nâng cao S3 và CloudFront:** <br>&emsp; + Module 03-Lab57-07.1 - Block all public access <br>&emsp; + Module 03-Lab57-07.2 - Config Amazon CloudFront <br>&emsp; + Module 03-Lab57-07.3 - Test Amazon Cloudfront <br>&emsp; + Module 03-Lab57-08 - Bucket Versioning <br>&emsp; + Module 03-Lab57-09 - Move objects <br>&emsp; + Module 03-Lab57-10 - Replication Object multi Region <br>&emsp; + Module 03-Lab57-11 - Clean up resources | 15/05/2026 | 15/05/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 4:

* Hiểu sâu về thiết lập EC2: cách tối ưu hóa việc chọn loại Instance (tối ưu Compute, Memory, Storage...), cơ chế lưu trữ bền vững (EBS) so với lưu trữ tạm thời tốc độ cao (Instance Store).
* Biết cách sử dụng User Data để chạy các script cài đặt khởi tạo tự động, và lấy metadata hệ thống thông qua CLI.
* Xây dựng và kiểm tra thành công kế hoạch sao lưu (Backup plan) và khôi phục (Restore test) tự động bằng AWS Backup.
* Thiết lập hệ thống lưu trữ kết hợp lai (Storage Gateway File Share) cho phép lưu trữ dữ liệu cục bộ đồng bộ an toàn lên S3.
* Triển khai website tĩnh thành công trên S3; sau đó khóa truy cập công khai trực tiếp của Bucket và phân phối an toàn thông qua CloudFront CDN nhằm bảo vệ dữ liệu gốc và tối ưu hóa tốc độ tải trang.
* Cấu hình thành công Bucket Versioning giúp lưu trữ các phiên bản cũ của tệp và Cross-Region Replication (CRR) giúp tự động nhân bản dữ liệu sang Region khác phục vụ sao lưu dự phòng thảm họa (Disaster Recovery).


