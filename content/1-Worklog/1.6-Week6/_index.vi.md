---
title: "Worklog Tuần 6"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}


### Mục tiêu tuần 6:

* Khởi tạo cấu trúc dự án React (Vite) và thiết lập thiết kế Tailwind CSS cùng hệ thống định tuyến (Routing).
* Xây dựng giao diện Đăng nhập & Đăng ký tối ưu hóa Responsive cho di động.
* Thiết lập hệ thống quản lý đăng nhập toàn cục sử dụng AuthContext và Axios Interceptors với Token JWT.
* Kiểm thử kết nối và phân giải CORS qua AWS Application Load Balancer (ALB).

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Khởi tạo dự án React với công cụ build Vite <br> - Cấu hình Tailwind CSS, components.json, thiết lập hệ thống màu sắc và kiểu chữ (typography) đặc thù cho thương hiệu NodeJ2Car | 25/05/2026 | 25/05/2026 | Tài liệu dự án NodeJ2Car |
| 3 | - Thiết lập cấu trúc định tuyến tĩnh và động bằng react-router-dom <br> - Xây dựng các layout cơ bản (Header, Footer, Sidebar) <br> - Cấu hình tệp .env.development và các tham số môi trường | 26/05/2026 | 26/05/2026 | Tài liệu dự án NodeJ2Car |
| 4 | - Xây dựng giao diện đăng ký (Register.jsx) và đăng nhập (Login.jsx) đáp ứng responsive hoàn toàn trên các thiết bị di động | 27/05/2026 | 27/05/2026 | Tài liệu thiết kế Figma |
| 5 | - Tích hợp thư viện Axios thực hiện các cuộc gọi API <br> - Cấu hình Axios Interceptors tự động đính kèm mã JWT vào Header của các yêu cầu HTTP | 28/05/2026 | 28/05/2026 | Tài liệu API NodeJ2Car |
| 6 | - Lập trình quản lý trạng thái đăng nhập toàn cục bằng AuthContext <br> - **AWS Integration:** Kiểm thử gọi API xác thực qua Application Load Balancer (ALB) của AWS để đảm bảo cấu hình CORS chuẩn xác | 29/05/2026 | 29/05/2026 | Hướng dẫn AWS ALB |

### Kết quả đạt được tuần 6:

* Khởi tạo thành công Boilerplate dự án React/Vite với cấu trúc thư mục tối ưu và tích hợp Tailwind CSS ổn định.
* Hoàn thiện cấu trúc định tuyến Client-side Routing và các layout cơ bản của trang web.
* Giao diện Đăng nhập và Đăng ký hiển thị mượt mà trên cả máy tính và di động, bắt lỗi biểu mẫu đầu vào (Form Validation) chặt chẽ.
* Triển khai hệ thống lưu trữ Token JWT an toàn trong AuthContext, tự động đính kèm Token cho mọi API gọi sau đó bằng Axios Interceptor.
* Xử lý thành công lỗi CORS khi gọi API từ Frontend đến cụm EC2/ECS Backend nằm sau Application Load Balancer (ALB).


