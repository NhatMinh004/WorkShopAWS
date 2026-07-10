---
title: "Worklog Tuần 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 3:

* Hoàn thành triển khai mạng VPC, cấu hình định tuyến Internet qua NAT Gateway & IGW và thiết lập các nhóm bảo mật (Security Groups).
* Triển khai các máy chủ EC2 trong Subnet và cấu hình phương thức kết nối an toàn với EC2 Instance Connect Endpoint.
* Tìm hiểu và thiết lập giải pháp phân giải tên miền chéo Hybrid DNS giữa Cloud và On-premises sử dụng Route 53 Resolver.
* Thực hiện kết nối Remote Desktop qua RDGW, kiểm tra hoạt động phân giải DNS và dọn dẹp tài nguyên lab.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Cấu hình định tuyến và bảo mật VPC:** <br>&emsp; + Module 02-Lab03-03.3 - Create an Internet Gateway <br>&emsp; + Module 02-Lab03-03.4 - Create Route Table for Outbound Internet Routing via Internet Gateway <br>&emsp; + Module 02-Lab03-03.5 - Create security groups | 04/05/2026 | 04/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Triển khai máy chủ và định tuyến NAT:** <br>&emsp; + Module 02-Lab03-04.1 - Create EC2 Instances in Subnets <br>&emsp; + Module 02-Lab03-04.2 - Test connection <br>&emsp; + Module 02-Lab03-04.3 - Create NAT Gateway <br>&emsp; + Module 02-Lab03-04.5 - EC2 Instance Connect Endpoint | 05/05/2026 | 05/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Thiết lập hạ tầng Hybrid DNS:** <br>&emsp; + Module 02-Lab10-01 - Set up Hybrid DNS with Route 53 Resolver (Introduction) <br>&emsp; + Module 02-Lab10-02.1 - Generate Key Pair <br>&emsp; + Module 02-Lab10-02.2 - Initialize CloudFormation Template <br>&emsp; + Module 02-Lab10-02.3 - Configure Security Group | 06/05/2026 | 06/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Cấu hình RDGW và DNS Endpoint:** <br>&emsp; + Module 02-Lab10-03 - Connect to RDGW <br>&emsp; + Module 02-Lab10-05 - Set up DNS <br>&emsp; + Module 02-Lab10-05.1 - Create Route 53 Outbound Endpoint | 07/05/2026 | 07/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Cấu hình Resolver và kiểm tra kết quả:** <br>&emsp; + Module 02-Lab10-05.2 - Create Route 53 Resolver Rules <br>&emsp; + Module 02-Lab10-05.3 - Create Route 53 Inbound Endpoints <br>&emsp; + Module 02-Lab10-05.4 - Test results <br>&emsp; + Module 02-Lab10-06 - Clean up resources | 08/05/2026 | 08/05/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 3:

* Triển khai hoàn chỉnh hệ thống định tuyến VPC cho phép các tài nguyên trong Public Subnet giao tiếp với Internet qua Internet Gateway, và các tài nguyên trong Private Subnet đi ra ngoài qua NAT Gateway.
* Khởi tạo máy chủ EC2 trong các Subnet thành công.
* Cấu hình và sử dụng thành công EC2 Instance Connect Endpoint để quản trị SSH/RDP an toàn mà không cần public IP và Bastion Host.
* Sử dụng thành công AWS CloudFormation để tự động hóa việc triển khai cơ sở hạ tầng phục vụ lab Hybrid DNS.
* Xây dựng thành công giải pháp Hybrid DNS phân giải tên miền qua lại giữa môi trường On-Premises và AWS Cloud bằng Route 53 Resolver (Inbound/Outbound Endpoints & Rules).
* Kết nối từ xa qua Remote Desktop Gateway (RDGW) thành công.
* Dọn dẹp sạch sẽ toàn bộ tài nguyên lab sau khi hoàn thành để tối ưu hóa chi phí.


