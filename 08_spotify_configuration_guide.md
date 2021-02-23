
Vietbot hỗ trợ Playback Spotify trực tiếp trên loa hoặc ra lệnh cho các thiết bị khác:

### STEP1. Cài đặt Spotify

1.1 Nâng cấp tài khoản Spotify Free thành Premium

1.2. Vào trang Develop của Spotify https://developer.spotify.com/

1.3. Đăng nhập và tạo App theo hướng dẫn: 

1.3.1. Lưu lại các giá trị sau:

```sh
Client id
Client_secret 
```

1.3.2. Tạo giá trị Redirect URL
Có dạng 

```sh
http://localhost:xxxx
```

với xxxx là số port bất kỳ, ko trùng với port nào đang sử dụng trên Pi cài Raspbian Desktop

### STEP2. Lấy Cache trên Raspbian Desktop

2.1. Chuẩn bị Pi cài Raspbian Desktop

2.1.1. Cài đặt gói Python Spotipy 

```sh
python 3 -m pip install spotipy
```
2.1.2. Download file get_spotify_cache.py từ https://github.com/phanmemkhoinghiep/vietbot_sourcecode vào Desktop

2.1.3. Mở file get_spotify_cache.py, nhập các giá trị 

```sh
Client id
Client_secret 
Redirect URL
```
sau đó save lại

2.2. Lấy Cache

2.2.1. Trên Desktop, nháy đúp và chạy Terminal

2.2.2. Sử dụng các lệnh sau

```sh
cd /home/pi/Desktop
```
sau đó

```sh
python3 get_spotify_cache.py
```
App sẽ thông báo

```sh
Couldn't read cache at: .cache
```
Sau đó trình duyệt sẽ tự động mở ra Desktop, đăng nhập vào Spotity và làm theo các bước để đăng ký App

Sau khi đăng ký xong, File .cache sẽ được tạo

2.2.3. Copy file .cache
Copy file .cache s vừa tạo về lại thư mục vietbot trên phần cứng loa thông minh

### STEP3. Cài đặt Spotify Client trên Loa thông minh

3.1. Cài đặt Curl

```sh
sudo apt-get install apt-transport-https curl -y 
```

3.2. Cài đặt theo script sau

```sh
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
```

### STEP4. Chạy lại Vietbot

4.1. Chạy lại Vietbot theo hướng dẫn: https://github.com/phanmemkhoinghiep/vietbot/blob/main/06_running_guide.md

