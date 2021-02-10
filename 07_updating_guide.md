
### STEP1. Theo dõi git

1.1. Theo dõi bằng git Desktop

Cài đặt Git Desktop trên PC và theo dõi git phanmemkhoinghiep/vietbot_source_code

Nếu có File cập nhật sẽ chuyển sang bước 2

Truy cập vào git phanmemkhoinghiep/vietbot_source_code 

Nếu phát hiện có file nào vừa cập nhật thì chuyển sang bước 2

### STEP2.  Lấy file vừa cập nhật về

2.1. Backup file

Backup 2 file google.json và config.yaml bằng lệnh

```sh
sudo cp /home/pi/vietbot/google.json /home/pi/google.json

```
và

```sh
sudo cp /home/pi/vietbot/config.yaml /home/pi/config.yaml

```

2.2. Download file update

2.2.1. Download bằng lệnh git
```sh
git clone phanmemkhoinghiep/vietbot_source_code

```
2.2.2 Đổi tên thư mục vietbot_source_code thành vietbot

2.3. Restore file

Restore 2 file google.json và config.yaml bằng lệnh

```sh
sudo cp /home/pi/google.json /home/pi/vietbot/google.json

```
và

```sh
sudo cp /home/pi/config.yaml /home/pi/vietbot/config.yaml

```
2.4. Chạy lại ứng dụng 

```sh
sudo supervisorctl restart vietbot

```
Chờ bot chạy
