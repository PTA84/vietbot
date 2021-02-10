
### STEP1. Chạy Manual

1.1. Truy nhập vào thư mục Bot
Sử dụng lệnh sau

```sh
cd vietbot
```
1.2. Chạy boot bằng lệnh 

```sh
python3 main_process.py
```

### STEP2.  Chạy tự động khi khởi động Pi

1.1. Thiết lập tự động chạy bot khi bật nguồn, và tự chạy lại khi lỗi
Sử dụng lần lượt các lệnh sau

```sh
sudo apt-get install supervisor -y

```
sau khi cài đặt xong supervisor, gõ lệnh sau:

```sh
sudo nano /etc/supervisor/conf.d/vietbot.conf

```
Tại cửa sổ nano, gõ các dòng sau

```sh
[program:vietbot]
directory=/home/pi/vietbot
command=/bin/bash -c 'cd /home/pi/vietbot && python3 main_process.py'
numprocs=1
autostart=true
autorestart=true
user=pi
```
Bấm Ctrl + X, Y, Enter

Sau đó gõ tiếp các lệnh sau
```sh
sudo supervisorctl update
```
Chờ sau khi có thông báo update, khởi động lại Pi 

```sh
sudo reboot
```

Bot sẽ tự động chạy (Chú ý thời gian chạy của bot khá lâu sau khi khởi động)

1.2. Stop quá trình tự chạy lại bot này, sử dụng các lệnh sau

```sh
sudo supervisorctl stop vietbot
```

1.3. Gỡ vietbot ra khỏi tự động chạy

```sh
sudo supervisorctl remove vietbot
```
1.4. Khởi động lại

Chờ sau khi có thông báo update, khởi động lại Pi 

```sh
sudo reboot
```
Bot sẽ không tự chạy lại nữa
