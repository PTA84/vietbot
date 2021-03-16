Vietbot sử dụng STT (Speed to Text) Online để nhận diện câu lệnh và TTS (Text to Speech) Online để phát câu phản hồi, Vietbot hỗ trợ các
STT và TTS sau:

### STEP1. Tạo STT & TTS Google
Vietbot hỗ trợ STT & TTS Google là Engine chính cho quá trình STT & TTS
1.1. Cấu hình STT

STT Google cần tạo file .json, làm theo các bước sau

1.1.1. Truy cập: https://console.cloud.google.com/

1.1.2. Đăng nhập với tài khoản Google và đồng ý với Terms of Service

1.1.3. Tạo 1 project với tên, sau đó mở Project

1.1.4. Chọn APIs & Service, sau đó chọn Library 

1.1.5. Lần lượt tìm Google Cloud Speech to Text và Googe Cloud Text to Speech và Enable cả 2 API này

1.1.6. Tạo Credentials bằng cách ấn Create new credentials

1.1.7. Chọn Service Account

Làm theo các bước hướng dẫn cho đến khi có nút download thì download file .json về và máy và đổi tên thành google.json

1.2. Cấu hình TTS Google

TTS Google cần sử dụng API, làm theo các bước sau

1.2.1 Lặp lại bước 1.1.6 ở trên, nhưng chọn API 

Làm theo các bước hướng dẫn cho đến khi tạo ra API thì copy và lưu lại API

### STEP2.  Tạo STT & TTS FPT, Viettel, ZALO

Trong trường hợp muốn sử dụng các Engine khác để phản hồi bằng giọng địa phương, Vietbot cũng hỗ trợ FPT, Viettel và Zalo theo các bước sau:

2.1. Đăng ký Acc FPT AI (Miễn phí) cho cả STT và TTS tại: https://fpt.ai/

2.2. Đăng ký Acc Viettel AI (Miễn phí) cho cả STT và TTS tại: https://viettelgroup.ai/en

2.3. Đăng ký Acc Zalo AI (Miễn phí) cho cả STT và TTS tại: https://zalo.ai/user-profile


Vietbot hỗ trợ File cấu hình các tham số của bot tại file config.yaml

### STEP3. Cấu hình STT &TTS

Mở file create_config.py bằng WinSCP và ứng dụng Notepad ++

3.1. Cấu hình STT

Tìm đến các giá trị tương ứng với các stt_engine và bổ sung thông tin phù hợp như token/api

Kích hoạt STT Engine nào thì sẽ đặt tham số is_active là True và ngược lại

3.2.1. TTS Engine

Tìm đến các giá trị tương ứng với các tts_engine và bổ sung thông tin phù hợp như token/api

Kích hoạt TTS Engine nào thì sẽ đặt tham số is_active là True và ngược lại
