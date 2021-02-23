
Vietbot hỗ trợ Playback Spotify trực tiếp trên loa Vietbot hoặc ra lệnh cho các thiết bị Spotipy Player khác:

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
python3 -m pip install spotipy
```
2.1.2. Tạo thư mục test (/home/pi/test)

2.1.3. Download file get_spotify_cache.py từ https://github.com/phanmemkhoinghiep/vietbot_sourcecode vào thư mục test 

2.1.4. Mở file get_spotify_cache.py, nhập các giá trị 

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
cd /home/pi/test/
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

Sau khi đăng ký xong, File .cache sẽ được tạo tại thư mục  /home/pi/test/

2.2.3. Copy file .cache

Copy file .cache s vừa tạo về sang phần cứng cài vietbot và trong thư mục vietbot bằng WinSCP (Bật shortcut Ctrl + Alt + H để hiện file ẩn)

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

4.1. Cài đặt gói Python Spotipy 

```sh
python3 -m pip install spotipy
```

4.2. Mở file config.yaml, nhập các giá trị 

```sh
Client id
Client_secret 
```
vào các mục
```sh
spotify_client_id
spotify_client_secret

```
nhập giá trị
```sh
music_source: 2
 
```
 
sau đó save lại

4.2. Chạy lại Vietbot theo hướng dẫn: https://github.com/phanmemkhoinghiep/vietbot/blob/main/06_running_guide.md

4.3 Ra lệnh phát nhạc với nội dung bao gồm từ khóa trong request.yaml
```sh
request_music:
- PHÁT BÀI
- PHÁT NHẠC
- CHƠI NHẠC
 
```
