
### STEP1. Chạy Manual

1.1. Truy nhập vào thư mục Bot
Sử dụng lệnh sau

```sh
cd vietbot/src
```
1.2. Chạy boot bằng lệnh 

```sh
python3 start.py
```
1.3. Ra lệnh bằng từ khóa

Sau khi có kết quả thành công, ra lệnh bằng từ khóa đã có trong file confg.yaml sẽ có tiếng Ting và bắt đầu chờ để ra lệnh


### STEP2.  Chạy tự động khi khởi động Pi

2.1. Chạy bằng Supervisor (Hiện đang lỗi chưa cập nhật cách sửa)

2.2. Tự động bằng crontab

2.2.1. Tạo nơi lưu log

```sh
cd ~
mkdir logs
```
2.2.2. Khai báo crontab

```sh
crontab -e
```
Chọn 1 để edit bằng nano 
Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi gõ

```sh
@reboot sh /home/pi/vietbot/src/start.sh >/home/pi/logs/cronlog 2>&1
```
Bấm Ctrl + X, Y, Enter

2.2.3. Khởi động lại Pi 

```sh
sudo reboot
```
Bot sẽ tự động chạy khi khởi động Pi (Chú ý thời gian chạy của bot có thể lâu sau khi khởi động)

2.2.4. Xem log khi chạy

```sh
cat /home/pi/logs/cronlog
```
2.2.5. Gỡ tự động chạy khi khởi động Pi (Nếu cần)

```sh
crontab -e
```
Chọn 1 để edit bằng nano 

Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi xóa dòng sau

```sh
@reboot sh /home/pi/vietbot/src/start.sh >/home/pi/logs/cronlog 2>&1
```
Bấm Ctrl + X, Y, Enter

Khởi động lại Pi 

```sh
sudo reboot
```
Bot sẽ không tự động chạy khi khởi động Pi nữa
