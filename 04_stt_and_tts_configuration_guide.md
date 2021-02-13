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

Mở file config.yaml bằng WinSCP và ứng dụng Notepad ++

1.1 Cấu hình STT

1.1.1. STT Engine

```sh
stt_engine: x
```
x có các giá trị sau: 0 (Ko sử dụng STT), 1 (Google STT Free (gTTS)), 2 (Google Cloud STT), 3 (VTCC STT), 4: (FPT STT)

1.1.2. STT Timeout

Điều chỉnh mục sau
```sh
stt_timeout: x
```
x đơn vị là ms

1.1.3. Google credentials

Điều chỉnh mục sau
```sh
google_application_credentials: file_name.json
```
file_name.json là file thu được từ bước cấu hình credential tạo Google tại: https://github.com/phanmemkhoinghiep/vietbot/blob/main/stt_and_tts_configuration_guide.md

1.1.4. VTCC AI WS

Điều chỉnh mục sau
```sh
stt_viettel_url: ws://abc.def
```
abc.def là địa chỉ WebSocket VTCC

1.2. Cấu hình TTS

1.2.1. TTS Engine

Điều chỉnh mục sau
```sh
tts_engine: x
```
x có các giá trị sau: 0 (Ko sử dụng STT), 1 (Google TTS Free (gTTS)), 2 (Google Cloud TTS), 3 (VTCC TTS), 4: (FPT TTS), 5: (Zalo TTS)

1.2.2. API của Google, Token của Viettel, API của FPT, Zalo của API

Điều chỉnh mục sau:

```sh
google_api: sfsljflsjfanwsn5Lu-LYqKSLJRLJGY
viettel_token: SysfdsfdsfadsjBFqq-jxLrWpxlyXxzdWỦKLDDRD
fpt_api: 7591A4mt9hBzp8kLJFLDLJRNLLDEORKDEELLR
zalo_api: 8sJJ39o7qhfSFDLJFLREOEOJGLLSLrrRILE
```
Các giá trị là giá trị đăng ký tại: https://github.com/phanmemkhoinghiep/vietbot/blob/main/stt_and_tts_configuration_guide.md

1.2.3. Tham số cho TTS Zalo
```sh
tts_zalo_voice_id: x
tts_zalo_speed: y
```
x có các giá trị sau: 1,2,3,4
y có các giá trị từ 0.1 tới 1.0

1.2.4. Giá trị âm lượng
```sh
volume: x
```
x có các giá trị từ 0.1 tới 1.0

