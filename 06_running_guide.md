
### STEP1. Chạy Manual

1.1. Truy nhập vào thư mục Bot
Sử dụng lệnh sau

```sh
cd vietbot/src
```
1.2. Chạy boot bằng lệnh 

```sh
python3 main.so
```
1.3. Ra lệnh bằng từ khóa

Sau khi có kết quả thành công, ra lệnh bằng từ khóa đã có trong file confg.yaml sẽ có tiếng Ting và bắt đầu chờ để ra lệnh


### STEP2.  Chạy tự động khi khởi động Pi

2.1. Chạy bằng Supervisor

Thiết lập tự động chạy bot khi bật nguồn, và tự chạy lại khi lỗi

2.1.1. Cài đặt Supervisor

```sh
sudo apt-get install supervisor -y

```
2.1.2. Edit file config 

```sh
sudo nano /etc/supervisor/conf.d/vietbot.conf

```
Tại cửa sổ nano, gõ các dòng sau

```sh
[program:vietbot]
directory=/home/pi/vietbot/src
command=/bin/bash -c 'cd /home/pi/vietbot/src && python3 start.py'
numprocs=1
autostart=true
autorestart=true
user=pi
```
Bấm Ctrl + X, Y, Enter

2.1.3. Update supervisor
```sh
sudo supervisorctl update
```
2.1.4. Khởi động lại Pi 

```sh
sudo reboot
```

Bot sẽ tự động chạy (Chú ý thời gian chạy của bot có thể lâu sau khi khởi động)

2.1.5. Stop quá trình tự chạy lại bot này (Nếu cần)

```sh
sudo supervisorctl stop vietbot
```

Gỡ vietbot ra khỏi tự động chạy

```sh
sudo rm -rf /etc/supervisor/conf.d/vietbot.conf 
```
sau đó

```sh
sudo supervisorctl update
```
Chờ sau khi có thông báo update

Khởi động lại

```sh
sudo reboot
```
Bot sẽ không tự chạy lại nữa


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
@reboot sh /home/pi/vietbot/start.sh >/home/pi/logs/cronlog 2>&1i
```
Bấm Ctrl + X, Y, Enter

2.2.3. Khởi động lại Pi 

```sh
sudo reboot
```
Bot sẽ tự động chạy (Chú ý thời gian chạy của bot có thể lâu sau khi khởi động)

2.2.4. Xem log khi chạy

```sh
cat /home/pi/logs/cronlog
```
2.2.5. Gỡ tự động

```sh
crontab -e
```
Chọn 1 để edit bằng nano 

Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi xóa dòng sau

```sh
@reboot sh /home/pi/vietbot/start.sh >/home/pi/logs/cronlog 2>&1i
```
Bấm Ctrl + X, Y, Enter

Khởi động lại Pi 

```sh
sudo reboot
```
Bot sẽ không tự động chạy nữa


