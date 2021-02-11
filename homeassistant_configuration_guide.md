Vietbot hỗ trợ Home Assistant để điều khiển nhà thông minh bằng giọng nói Việt với hai tham số là Base URL & Long Lived Token

### STEP1. Lấy Base URL và Long Lived token

1.1. Base URL Internal

Có dạng: http://X.X.X.X:8123 với X.X.X.X là địa chỉ Private

1.2. Base URL External

Có dạng: http://abc.def:8123 (Có thể không có 8123) hoặc không với abc.def là Domain

1.3. Truy cập vào Web UI của Home Assistant để lấy Long Lived Token 

### STEP3.  Chỉnh sửa trong File config.yaml

3.1. Nhập giá trị tại 1.1 hoặc 1.2 vào file config

```sh
hass_url: http://X.X.X.X:8123
```

3.2. Nhập giá trị tại 1.3 vào file config.yaml

```sh
hass_token: sdsldfjsdlfj
```
3.3. Sửa dòng sau trong file config
```sh
use_hass: 1
```
3.4. Save file config.yaml

### STEP4. Chạy lại bot

4.1. Chạy lại bot theo hướng dẫn tại https://github.com/phanmemkhoinghiep/vietbot/blob/main/running_guide.md

4.2. Chờ khi nào có thông báo là: 'Đã kết nối thành công tới trung tâm điều khiển nhà' là kết nối với Hass thành công

4.3. Chờ tiếp đến khi nào có thông báo là: 'Sẵn sàng chờ lệnh" là có thể ra lệnh với Hass

### STEP4. Cách ra lệnh trên Hass

4.1. Cấu trúc lệnh: Trong lệnh cần có đủ các phần sau, không cần thứ tự:

4.1.1. Action

Có trong danh sách: request_on, request_off, request_check 

4.1.2. Đối tượng

là tên friendly name của entity tương ứng với thiết bị, đã khai báo trên Hass

4.1.3. Loại đối tượng

Có trong danh sách request_light, request_switch, request_socket, request_fan,  request_curtain, request_temperature, request_humidity

4.2. Sau khi ra lệnh, có hai tình huống

4.2.1. Thành công

Phản hồi từ thiết bị với các thiết bị có phản hồi (Ví dụ đèn, quạt, rèm) và  thông báo về việc ra lệnh thành công

Thông báo kết quả với các thiết bị không có phản hồi (Ví dụ cảm biến)

4.2.1. Không thành công

Thông báo kết quả ra lệnh không thành công
