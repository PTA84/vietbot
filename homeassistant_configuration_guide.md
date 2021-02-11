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

4.2. Chờ khi nào có thông báo là: 'Đã kết nối thành công tới trung tâm điều khiển nhà'
