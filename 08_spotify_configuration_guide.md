
Vietbot hỗ trợ Playback Spotify trực tiếp trên loa Vietbot hoặc ra lệnh cho các thiết bị Spotify Player khác:

### STEP1. Cài đặt Spotify Client trên Loa thông minh

1.1. Cài đặt Curl

```sh
sudo apt-get install apt-transport-https curl -y 
```

1.2. Cài đặt theo script sau

```sh
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
```
1.3. Reboot lại Pi

```sh
sudo reboot
```

### STEP2. Cài đặt và lấy thông tin từ Spotify

2.1 Nâng cấp tài khoản Spotify Free thành Premium

2.2. Vào trang Develop của Spotify https://developer.spotify.com/

2.3. Tạo App theo hướng dẫn 

2.3.1. Tạo App

2.3.2. Tạo giá trị Redirect URL
Có dạng 

```sh
http://localhost:xxxx
```

với xxxx là số port bất kỳ, ko trùng với port nào đang sử dụng trên Pi cài Raspbian Desktop

2.3.3. Lưu lại các giá trị sau:

```sh
Client id
Client_secret 
Redirect URL
```
2.4. Lấy Device ID của Loa thông minh

2.4.1. Vào Console, Player

2.4.2. Chọn Mục  	Get a User's Available Devices

2.4.3. Tại mục Get a User's Available Devices thực hiện các thao tác

2.4.3.1. Click vào GET TOKEN

2.4.3.2. Click vào user-read-playback-state, Request Token

2.4.3.3. Click vào Try It

2.4.3.4. Tại cửa sổ bên phải tìm đến thiết bị có tên là raspotify

```sh
{
  "devices": [
    {
      "id": "sdfdsAD89349dsfd",
      "is_active": false,
      "is_private_session": false,
      "is_restricted": false,
      "name": "raspotify (raspberry)",
      "type": "Speaker",
      "volume_percent": 100
    }
  ]
}
```
Lưu lại giá trị của id

```sh
sdfdsAD89349dsfd
```

### STEP3. Lấy Cache trên Raspbian Desktop

3.1. Chuẩn bị Pi cài Raspbian Desktop

3.1.1. Cài đặt gói Python Spotipy 

```sh
python3 -m pip install spotipy
```
3.1.2. Tạo thư mục test (/home/pi/test)

3.1.3. Download file get_spotify_cache.py từ https://github.com/phanmemkhoinghiep/vietbot_sourcecode vào thư mục test 

3.1.4. Mở file get_spotify_cache.py, nhập các giá trị 

```sh
Client id
Client secret 
Redirect URL
```
vào các mục
```sh
spotify_client_id
spotify_client_secret
spotify_redirect_url: 
```

sau đó save lại

3.2. Lấy Cache

3.2.1. Trên Desktop, nháy đúp và chạy Terminal

3.2.2. Sử dụng các lệnh sau

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

3.2.3. Copy file .cache

Copy file .cache s vừa tạo về sang phần cứng cài vietbot và trong thư mục vietbot bằng WinSCP (Bật shortcut Ctrl + Alt + H để hiện file ẩn)

### STEP4. Chạy lại Vietbot

4.1. Cài đặt gói Python Spotipy 

```sh
python3 -m pip install spotipy
```
4.2. Mở file config.yaml, nhập các giá trị 

```sh
Client id
Client_secret 
Device ID: 
```
vào các mục
```sh
spotify_client_id
spotify_client_secret
spotify_device_id: 
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
