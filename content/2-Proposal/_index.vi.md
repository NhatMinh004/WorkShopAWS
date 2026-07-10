---
title: "Bản đề xuất"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

Tại phần này, bạn cần tóm tắt các nội dung trong workshop mà bạn **dự tính** sẽ làm.

# Nền tảng Thương mại Điện tử Phụ tùng Ô tô NodeJ2Car  
## Giải pháp Điện toán Đám mây AWS Tối ưu hóa Hiệu năng, Bảo mật và Khả năng Mở rộng  

### 1. Tóm tắt điều hành  
Dự án **NodeJ2Car** xây dựng một hệ thống thương mại điện tử chuyên biệt cung cấp các phụ tùng ô tô cao cấp. Nền tảng nổi bật với ba tính năng đột phá: trình duyệt sơ đồ xe hơi 2D trực quan tương tác, hỗ trợ khách hàng thời gian thực qua WebSockets và quét hình ảnh chẩn đoán được hỗ trợ bởi AI để nhận dạng các bộ phận bị hỏng. Để đáp ứng các yêu cầu về giao dịch trực tuyến đồng thời cao, bảo vệ nghiêm ngặt dữ liệu người dùng và xử lý thanh toán bất đồng bộ đáng tin cậy (VNPay, MoMo, Stripe), toàn bộ hệ thống được triển khai trên AWS sử dụng kiến trúc lai giữa container và serverless. Giải pháp này giúp NodeJ2Car đạt được tính khả dụng cao, khả năng mở rộng linh hoạt và giảm thiểu chi phí vận hành tối đa.

### 2. Tuyên bố vấn đề  
*Vấn đề hiện tại*  
1.  **Điều hướng danh mục phụ tùng phức tạp:** Phụ tùng ô tô bao gồm hàng triệu mã bộ phận riêng biệt. Người dùng thông thường gặp phải nhiều trở ngại và sai sót khi cố gắng tìm kiếm các phụ tùng phù hợp cho các mẫu xe cụ thể của họ bằng cách tìm kiếm từ khóa truyền thống.
2.  **Hệ thống không ổn định dưới tải lượng thời gian thực:** Việc xử lý các kết nối chat Socket.io đồng thời và các webhook gọi lại thanh toán bên ngoài (IPN) trực tiếp trên máy chủ API chính có thể dẫn đến nghẽn cổ chai nghiêm trọng, hết thời gian chờ API hoặc mất mát giao dịch.
3.  **Lỗ hổng bảo mật:** Là một trung tâm giao dịch tài chính, nền tảng thương mại điện tử là mục tiêu có giá trị cao đối với các cuộc tấn công SQL injection, rò rỉ dữ liệu và tấn công từ chối dịch vụ (DDoS).

*Giải pháp*  
Hệ thống giải quyết các điểm nghẽn này bằng cách tích hợp thiết kế phần mềm hiện đại với các dịch vụ đám mây AWS mạnh mẽ:
*   **Sơ đồ 2D trực quan & Quét AI:** Đơn giản hóa quy trình xác định phụ tùng, loại bỏ nhu cầu khách hàng phải ghi nhớ các mã phụ tùng phức tạp.
*   **Xử lý thanh toán bất đồng bộ:** Kiến trúc phi tập trung sử dụng tiếp nhận serverless với **AWS Lambda** và hàng đợi **Amazon SQS**, bảo mật lịch sử giao dịch ngay cả khi các container API Backend gặp sự cố.
*   **Trạng thái WebSockets phi tập trung:** Sử dụng **Amazon ElastiCache Redis** như một bộ điều phối pub/sub để đồng bộ hóa các tin nhắn Socket.io thời gian thực trên tất cả các tác vụ tính toán.
*   **Lá chắn bảo mật toàn diện:** Ẩn các tài nguyên tính toán trong các mạng con riêng tư (Private Subnet) của VPC đằng sau **Application Load Balancer (ALB)**, được bảo vệ vòng ngoài bởi các quy tắc **AWS WAF** và **Amazon CloudFront CDN**.

*Lợi ích và hoàn vốn đầu tư (ROI)*  
*   **Tăng tỷ lệ chuyển đổi:** Giảm 70% thời gian tìm kiếm của người dùng, giúp giảm tỷ lệ bỏ giỏ hàng và tăng doanh số.
*   **Độ khả dụng dịch vụ 99.99%:** Triển khai container Multi-AZ thông qua ECS Fargate đảm bảo khả năng dự phòng và chuyển đổi dự phòng liền mạch.
*   **Tối ưu hóa chi phí:** Loại bỏ lãng phí tài nguyên máy chủ nhàn rỗi thông qua mô hình tính phí serverless dùng bao nhiêu trả bấy nhiêu. Thời gian hoàn vốn dự kiến trong vòng 6 tháng nhờ giảm chi phí bảo trì hạ tầng và không xảy ra sự cố mất giao dịch.

### 3. Kiến trúc giải pháp  
Nền tảng sử dụng **Amazon VPC** làm nền tảng bảo mật, phân chia tài nguyên thành các mạng con Công khai (Public Subnet) và Riêng tư (Private Subnet) trên hai Vùng khả dụng (Availability Zone - AZ) độc lập. Lưu lượng truy cập từ bên ngoài được kiểm tra ở biên bởi **AWS WAF** và được lưu bộ đệm toàn cầu bởi **Amazon CloudFront** trước khi đến bộ cân bằng tải.

*Các dịch vụ AWS sử dụng*  
- **Amazon VPC:** Bố cục mạng (Mạng con Công khai/Riêng tư, NAT Gateway).
- **Amazon ECS & AWS Fargate:** Máy chủ tính toán container co giãn linh hoạt để lưu trữ mã nguồn Backend Node.js.
- **Application Load Balancer (ALB):** Phân phối tải lưu lượng với tính năng Sticky Sessions được kích hoạt để đảm bảo kết nối Socket ổn định.
- **Amazon DocumentDB:** Công cụ cơ sở dữ liệu tương thích MongoDB hoạt động theo mô hình primary-replica.
- **Amazon ElastiCache Redis:** Bộ nhớ đệm phiên và nút đồng bộ hóa pub/sub cho Socket.io.
- **AWS Lambda & Amazon SQS:** Bộ xử lý webhook IPN serverless và hàng đợi giao dịch.
- **Amazon S3 & S3 Gateway Endpoint:** Lưu trữ tài nguyên tĩnh React SPA và các tệp đa phương tiện của sản phẩm, sử dụng các cổng kết nối riêng tư (private endpoint) để tránh phát sinh chi phí NAT Gateway.
- **Amazon CloudFront & AWS WAF:** CDN toàn cầu và các tập quy tắc Tường lửa ứng dụng Web.
- **Amazon ECR:** Kho lưu trữ container riêng tư cho các hình ảnh Docker.

*Thiết kế thành phần*  
- **Tầng Frontend:** React SPA tĩnh được lưu trữ trên S3 và phân phối qua CloudFront.
- **Tầng Backend:** Các tác vụ Express API trong mạng con riêng tư, định tuyến qua ALB.
- **Tầng tích hợp:** Webhook kích hoạt các hàm Lambda serverless, đưa các tin nhắn giao dịch vào hàng đợi SQS để các worker backend tiêu thụ.
- **Tầng dữ liệu:** Cụm DocumentDB chạy một nút ghi chính ở AZ1 và một nút đọc bản sao ở AZ2.

### 4. Triển khai kỹ thuật  
*Các giai đoạn triển khai*  
Dự án được chia thành bốn giai đoạn thực hiện chính:
1.  **Giai đoạn 1: Thiết kế mạng VPC & Lược đồ cơ sở dữ liệu (Tuần 1 - 2):** Khởi tạo VPC, mạng con, bảng định tuyến và nhóm bảo mật. Thiết lập các lược đồ cơ sở dữ liệu DocumentDB.
2.  **Giai đoạn 2: API lõi & Thiết lập thời gian thực (Tuần 3 - 5):** Xây dựng cơ chế xác thực, các thao tác CRUD danh mục sản phẩm, sơ đồ xe SVG và tích hợp Socket.io với bộ điều phối Redis.
3.  **Giai đoạn 3: Xử lý giao dịch bất đồng bộ (Tuần 6 - 8):** Lập trình Lambda webhook, tạo hàng đợi SQS, viết logic xử lý dữ liệu ở backend worker. Thiết lập các tệp Dockerfile.
4.  **Giai đoạn 4: Triển khai đám mây & Kiểm thử hiệu năng (Tuần 9 - 11):** Triển khai hạ tầng bằng ECS Fargate, ALB, S3, CloudFront và WAF. Chạy các bài kiểm thử tải lưu lượng mô phỏng (hơn 1.000 người dùng), tối ưu hóa chỉ mục và hoàn tất bàn giao dự án.

*Yêu cầu kỹ thuật*  
- **Môi trường:** Docker Engine để đóng gói, AWS CLI/CDK để thiết lập hạ tầng.
- **Frontend:** ReactJS + Vite + Tailwind CSS, `socket.io-client`.
- **Backend:** NodeJS + ExpressJS, thư viện Mongoose client, tích hợp cổng `vnpay`, thư viện HTTP `axios`.

### 5. Lộ trình & Mốc triển khai  
- **Mốc 1 (Tuần 1 - 2):** Hoàn thành hạ tầng VPC, khởi tạo cụm DocumentDB, các API xác thực người dùng hoạt động ổn định.
- **Mốc 2 (Tuần 3 - 5):** Hoàn thiện Trang chủ, trình duyệt sơ đồ xe tương tác và các phòng chat hỗ trợ trực tuyến.
- **Mốc 3 (Tuần 6 - 8):** Chức năng AI Image Scan hoạt động. Triển khai hàng đợi thanh toán IPN tự động qua Lambda và SQS.
- **Mốc 4 (Tuần 9 - 10):** Chế độ tự động co giãn ECS Fargate hoạt động, mã nguồn React SPA được tải lên S3 và phục vụ qua CloudFront + WAF.
- **Mốc 5 (Tuần 11):** Hoàn thành kiểm thử tải, tối ưu hóa chỉ mục truy vấn cơ sở dữ liệu và bàn giao dự án.

### 6. Ước tính ngân sách  
Ngân sách hạ tầng AWS hàng tháng ước tính cho môi trường sản xuất (Production):

| Dịch vụ AWS | Chi tiết cấu hình | Chi phí hàng tháng (Ước tính) |
| :--- | :--- | :--- |
| **Amazon ECS & Fargate** | 2 Tasks (0.5 vCPU, 1 GB RAM) | ~ $15.00 |
| **Application Load Balancer** | 1 ALB, 1 LCU | ~ $22.00 |
| **Amazon DocumentDB** | db.t3.medium Cluster (1 Primary + 1 Replica) | ~ $110.00 |
| **Amazon ElastiCache Redis** | cache.t3.micro Cluster (1 Primary + 1 Replica) | ~ $30.00 |
| **Amazon S3** | Static Hosting & Media Storage (~ 50 GB) | ~ $3.00 |
| **Amazon CloudFront** | Outbound data transfer (~ 150 GB) | ~ $12.00 |
| **AWS WAF** | 1 Web ACL + 3 Basic Rule Groups | ~ $10.00 |
| **NAT Gateways** | 2 NAT Gateways + phí truyền tải dữ liệu | ~ $65.00 |
| **AWS Lambda & SQS** | 50.000 giao dịch (nằm trong Free Tier) | ~ $0.00 |
| **Tổng chi phí hạ tầng** | **Môi trường chất lượng sản xuất** | **~ $267.00 / Tháng** |

### 7. Đánh giá rủi ro  
*Ma trận rủi ro & Chiến lược giảm thiểu*  
1.  **Độ trễ truy vấn cơ sở dữ liệu dưới tải cao:**
    *   *Rủi ro:* Chiến dịch flash sale quá tải CPU của DocumentDB với các yêu cầu đọc thông tin sản phẩm.
    *   *Giảm thiểu:* Định tuyến tất cả các truy vấn đọc đến các phiên bản bản sao (replica) của DocumentDB và lưu bộ nhớ đệm các sản phẩm phổ biến trong Redis.
2.  **Mất kết nối WebSocket trong quá trình tự động co giãn backend:**
    *   *Rủi ro:* Các sự kiện co giãn container làm gián đoạn các phiên chat hỗ trợ đang diễn ra.
    *   *Giảm thiểu:* Kích hoạt Sticky Sessions trong ALB để duy trì kết nối ổn định với endpoint, được hỗ trợ bởi bộ phối hợp Redis Pub/Sub để đồng bộ hóa trạng thái tin nhắn giữa các tác vụ.
3.  **Chi phí AWS vượt tầm kiểm soát:**
    *   *Rủi ro:* Lưu lượng truy cập tăng đột biến hoặc cấu hình sai thông số Fargate làm tăng vọt chi phí hàng tháng.
    *   *Giảm thiểu:* Cấu hình AWS Budgets để cảnh báo ngay lập tức cho quản trị viên khi chi phí dự kiến vượt quá 300 USD. Thiết lập quy tắc vòng đời (lifecycle rules) trên S3 để xóa các tệp nhật ký AI Scan cũ.

### 8. Kết quả kỳ vọng  
*   **Mục tiêu kỹ thuật:** Thời gian tải trang toàn cầu dưới 2 giây. Khả năng tự động co giãn (từ 2 đến 10 tác vụ) để xử lượng tăng đột biến. Độ khả dụng dịch vụ đạt 99.99%.
*   **Tác động kinh doanh:** Không xảy ra lỗi mất lịch sử giao dịch khi cổng thanh toán gặp sự cố quá hạn (timeout). Giảm thiểu tỷ lệ rời bỏ trang của khách hàng nhờ các tính năng giao diện hấp dẫn (Sơ đồ xe tương tác & Quét ảnh AI).