### HƯỚNG DẪN CÀI ĐẶT TÍNH NĂNG LOA THÔNG BÁO

### STEP1. Cài đặt bổ sung thư viện 

Cài đặt bổ sung thư viện Flask
```sh
python3 -m pip install Flask
```
### STEP2. Kích hoạt Webhook

Sử dụng các tính năng sau:
```sh
export FLASK_APP=speaker_skill.py
python3 -m flask run --host=X.X.X.X 
```
Với X.X.X là địa chỉ IP của Mạch phần cứng chạy Vietbot

Nếu hiện các thông báo sau:

```sh
 * Serving Flask app "speaker_skill.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
pygame 1.9.4.post1
Hello from the pygame community. https://www.pygame.org/contribute.html
 * Running on http://192.168.1.109:5000/ (Press CTRL+C to quit)
```
Là Webhook Server đã chạy thành công

### STEP3. Truyền tín hiệu vào Vietbot để phát thông báo

Tại nguồn truyền, sử dụng tính năng webhook, phát bản tin với định dạng json là {"data":"Nội dung cần phát"} vào địa chỉ là http://192.168.1.109:5000/webhook

```sh
[BOT-TTS-GOOGLE-CLOUD]: Cộng hòa xã hội chủ nghĩa Việt Nam. Độc lập tự do hạnh phúc
Delayed: 5(s)
192.168.1.106 - - [27/Apr/2021 10:16:04] "POST /webhook HTTP/1.1" 200 -
```
Trong trường hợp thành công, Vietbot sẽ trả về nội dung 'Playback OK', không thành công sẽ trả về nội dung 'Playback not OK' trên Client

Ví dụ với Home Assistant

Khai báo trong configuration.yaml
```sh
rest_command:
  vietbot_tts:
    url: http://192.168.1.109:5000/webhook
    method: POST
    payload: '{"data":"{{ data }}"}'
    content_type: 'application/json; charset=utf-8'
automation:
  alias: test
  description: ''
  trigger:
    - platform: device
      type: turned_off
      device_id: cc94e4e74c8e7bcf0a9f2649637d3734
      entity_id: switch.0x588e81fffede3767_switch_l2
      domain: switch
  condition: []
  action:
    - service: rest_command.vietbot_tts
      data:
        data: Đã tắt đèn rồi nhé anh 
  mode: single
```
