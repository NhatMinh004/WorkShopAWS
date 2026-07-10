---
title: "Worklog Tuần 5"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 5:

* Nghiên cứu chi tiết các giải pháp lưu trữ nâng cao của AWS (S3 Access Points, Storage Classes, Glacier, Snow Family) và thực hành dịch chuyển máy chủ từ On-premises (VM Import/Export).
* Triển khai hệ thống tệp tin dùng chung hiệu năng cao Multi-AZ FSx cho Windows File Server (SSD/HDD FSx, Shadow copies, Quotas, Data deduplication) và AWS Storage Gateway.
* Nghiên cứu các khái niệm bảo mật AWS (Shared Responsibility Model, IAM, Cognito, AWS Organizations, Identity Center, KMS, Security Hub).
* Thực hành quản lý tài nguyên bằng AWS Tags và tự động hóa vận hành máy chủ (Lambda auto start/stop EC2 dựa trên tag, Slack notifications).
* Thực hành phân quyền chi tiết với IAM Policies/Roles, Switch Role có giới hạn dựa trên IP/thời gian, mã hóa KMS kết hợp giám sát bằng CloudTrail và truy vấn log bằng Amazon Athena.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Lưu trữ nâng cao và Dịch chuyển hạ tầng:** <br>&emsp; + Module 04-01 -> 04-04: Lý thuyết lưu trữ trên AWS <br>&emsp; + Module 04-Lab14-01 -> Lab14-05: VM Import/Export di chuyển máy ảo từ On-premises lên AWS <br>&emsp; + Module 04-Lab13-02.1 -> Lab13-06: AWS Backup nâng cao | 18/05/2026 | 18/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Hệ thống tệp tin doanh nghiệp:** <br>&emsp; + Module 04-Lab24-2.1 -> Lab24-3: Storage Gateway và mount File Shares cục bộ <br>&emsp; + Module 04-Lab25-2.2 -> Lab25-13: Cấu hình Multi-AZ FSx Windows File Server, shadow copy, quota, deduplication <br>&emsp; + Module 04-Lab57-2.1 -> Lab57-11: Cấu hình nâng cao S3 Static Website & CloudFront | 19/05/2026 | 19/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Bảo mật hạ tầng và Tự động hóa vận hành:** <br>&emsp; + Module 05-01 -> 05-08: Lý thuyết bảo mật AWS <br>&emsp; + Module 05-Lab18-02 -> Lab18-04: Đánh giá tuân thủ bảo mật bằng AWS Security Hub <br>&emsp; + Module 05-Lab22-2.1 -> Lab22-7: Viết Lambda tự động bật/tắt EC2 theo tag và gửi thông báo qua Slack Webhook | 20/05/2026 | 20/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Quản lý tài nguyên và Phân quyền IAM nâng cao:** <br>&emsp; + Module 05-Lab27-2.1.1 -> Lab27-4: Quản lý thẻ Tags & Resource Group <br>&emsp; + Module 05-Lab28-2.1 -> Lab28-6: IAM Policy, Role, Switch Roles <br>&emsp; + Module 05-Lab30-3 -> Lab30-6: Tạo tài khoản hạn chế quyền (Limited User) và kiểm tra chính sách <br>&emsp; + Module 05-Lab44-2 -> Lab44-5: Giới hạn Switch Role theo IP và Thời gian | 21/05/2026 | 21/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Mã hóa và Giám sát hoạt động:** <br>&emsp; + Module 05-Lab33-2.1 -> Lab33-7: Mã hóa KMS cho S3, ghi log với AWS CloudTrail và truy vấn log qua Amazon Athena <br>&emsp; + Module 05-Lab48-1.1 -> Lab48-4: Phân biệt Access Key vs IAM Instance Profile (IAM Role) trên EC2 | 22/05/2026 | 22/05/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 5:

* Di chuyển thành công máy ảo từ môi trường ảo hóa cục bộ (On-premises) lên chạy trực tiếp trên đám mây AWS thông qua quy trình VM Import/Export.
* Xây dựng thành công hệ thống lưu trữ tệp tin chuyên nghiệp FSx Windows File Server, kích hoạt tối ưu dung lượng ổ đĩa (Data deduplication) giúp tiết kiệm đến 50-60% bộ nhớ và cài đặt Shadow copies phục vụ khôi phục nhanh file cho người dùng.
* Thực hiện tự động hóa thành công việc bật/tắt máy chủ EC2 ngoài giờ làm việc bằng AWS Lambda được kích hoạt qua EventBridge Rule dựa vào Tag, đồng thời gửi thông tin thông báo trạng thái tức thời đến kênh chat Slack.
* Đánh giá và kiểm tra bảo mật tài khoản dựa trên các tiêu chuẩn thực hành tốt nhất bằng cách sử dụng AWS Security Hub.
* Triển khai phân quyền nâng cao trên IAM: thiết lập các điều kiện ngặt nghèo trong IAM Policy (Condition) để hạn chế quyền Switch Role theo dải IP nguồn và khoảng thời gian làm việc.
* Thực hiện mã hóa dữ liệu tĩnh S3 bằng AWS KMS, lưu trữ log hoạt động hệ thống chi tiết qua AWS CloudTrail và thực hiện phân tích, kiểm tra audit log dễ dàng bằng các truy vấn SQL trực tiếp trên Amazon Athena.
* Nắm vững nguyên tắc an toàn: luôn sử dụng IAM Role gán cho EC2 (IAM Instance Profile) thay vì cấu hình cứng Access Key/Secret Key trong code/máy chủ.


