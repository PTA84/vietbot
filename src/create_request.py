import json

data = {}
data['all'] = []
data['all'].append({
    'content': 'tất cả',
    'is_active': True
})
data['all'].append({
    'content': 'hết cả',
    'is_active': True
})
data['all'].append({
    'content': 'toàn bộ',
    'is_active': True
})
data['all'].append({
    'content': 'toàn bộ',
    'is_active': True
})
data['all'].append({
    'content': 'đầy đủ',
    'is_active': True
})
data['single'] = []
data['single'].append({
    'content': 'duy nhất',
    'is_active': True
})
data['single'].append({
    'content': 'chỉ một',
    'is_active': True
})
data['single'].append({
    'content': 'riêng mỗi',
    'is_active': True
})
data['single'].append({
    'content': 'duy mỗi',
    'is_active': True
})
data['single'].append({
    'content': 'mỗi một',
    'is_active': True
})
data['single'].append({
    'content': 'duy nhất',
    'is_active': True
})
data['on'] = []
data['on'].append({
    'content': 'mở lên',
    'is_active': True
})
data['on'].append({
    'content': 'bật lên',
    'is_active': True
})
data['on'].append({
    'content': 'nối lên',
    'is_active': True
})
data['on'].append({
    'content': 'kích hoạt',
    'is_active': True
})
data['on'].append({
    'content': 'thực hiện',
    'is_active': True
})
data['on'].append({
    'content': 'thi hành',
    'is_active': True
})
data['off'] = []
data['off'].append({
    'content': '',
    'is_active': True
})
data['off'].append({
    'content': 'đóng đi',
    'is_active': True
})
data['off'].append({
    'content': 'tắt đi',
    'is_active': True
})
data['off'].append({
    'content': 'ngắt đi',
    'is_active': True
})
data['off'].append({
    'content': 'vô hiệu',
    'is_active': True
})
data['off'].append({
    'content': 'hủy bỏ',
    'is_active': True
})
data['light'] = []
data['light'].append({
    'content': 'bóng đèn',
    'is_active': True
})
data['light'].append({
    'content': 'bóng điện',
    'is_active': True
})
data['light'].append({
    'content': 'đèn điện',
    'is_active': True
})
data['switch'] = []
data['switch'].append({
    'content': 'công tắc',
    'is_active': True
})
data['socket'] = []
data['socket'].append({
    'content': 'ổ cắm',
    'is_active': True
})
data['socket'].append({
    'content': 'ổ điện',
    'is_active': True
})
data['fan'] = []
data['fan'].append({
    'content': 'quạt',
    'is_active': True
})
data['curtain'] = []
data['curtain'].append({
    'content': 'rèm',
    'is_active': True
})
data['curtain'].append({
    'content': 'mành',
    'is_active': True
})
data['curtain'].append({
    'content': 'màn',
    'is_active': True
})
data['cover'] = []
data['cover'].append({
    'content': 'cửa cuốn',
    'is_active': True    
})
data['gate'] = []
data['gate'].append({
    'content': 'cổng',
    'is_active': True    
})
data['door'] = []
data['door'].append({
    'content': 'cửa',
    'is_active': True    
})
data['television'] = []
data['television'].append({
    '1': 'tivi',
    '2': 'tivi',    
    '3': 'vô tuyến'
})
data['temperature'] = []
data['temperature'].append({
    '1': 'nhiệt độ',
    '2': 'mức nhiệt'
})
data['humidity'] = []
data['humidity'].append({
    '1': 'độ ẩm',
    '2': 'mức ẩm'
})
data['script'] = []
data['script'].append({
    '1': 'kịch bản',
    '2': 'chuỗi hành động'
})
data['automation'] = []
data['automation'].append({
    '1': 'tự động'
})
data['scene'] = []
data['scene'].append({
    '1': 'hoạt cảnh',
    '2': 'ngữ cảnh'    
})
data['adjust_incrase'] = []
data['adjust_incrase'].append({
    '1': 'tăng lên',
    '2': 'tăng thêm',
    '3': 'tăng đi'    
})
data['light_incrase'] = []
data['light_incrase'].append({
    '1': 'sáng lên',
    '2': 'sáng thêm',
    '3': 'sáng đi'    
})
data['volume_incrase'] = []
data['volume_incrase'].append({
    '1': 'to lên',
    '2': 'to thêm',
    '3': 'tăng âm lượng'    
})
data['temperature_incrase'] = []
data['temperature_incrase'].append({
    '1': 'ấm lên',
    '2': 'ấm thêm',
    '3': 'nóng thêm'    
})
data['humidity_incrase'] = []
data['humidity_incrase'].append({
    '1': 'ẩm lên',
    '2': 'ẩm thêm',
})
data['adjust_decrase'] = []
data['adjust_decrase'].append({
    '1': 'giảm xuống',
    '2': 'giảm thêm',
    '3': 'giảm đi'    
})
data['light_decrase'] = []
data['light_decrase'].append({
    '1': 'tối xuống',
    '2': 'tối đi'
})
data['volume_decrase'] = []
data['volume_decrase'].append({
    '1': 'bé xuống',
    '2': 'bé đi',
    '3': 'giảm âm lượng'    
})
data['temperature_decrase'] = []
data['temperature_decrase'].append({
    '1': 'lạnh xuống',
    '2': 'lạnh thêm',
    '3': 'lạnh đi'    
})
data['humidity_decrase'] = []
data['humidity_decrase'].append({
    '1': 'ẩm xuống',
    '2': 'khô đi'
})
data['check'] = []
data['check'].append({
    'content': 'kiểm tra',
    'is_active': True
})
data['check'].append({
    'content': 'hiển thị',
    'is_active': True
})
data['check'].append({
    'content': 'trạng thái',
    'is_active': True
})
data['check'].append({
    'content': 'thông tin',
    'is_active': True
})
data['check'].append({
    'content': 'tắt hay mở',
    'is_active': True
})
data['check'].append({
    'content': 'đóng hay mở',
    'is_active': True
})
data['check'].append({
    'content': 'bật hay tắt',
    'is_active': True
})
data['setup'] = []
data['setup'].append({
    '1': 'thiết lập',
    '2': 'cài đặt',
    '3': 'thiết đặt'    
})
data['speedtest'] = []
data['speedtest'].append({
    'content': 'đường truyền internet',
    'is_active': True
})    
data['speedtest'].append({
    'content': 'kết nối internet',
    'is_active': True
})
data['speedtest'].append({
    'content': 'đường internet',
    'is_active': True
})  
data['schedule'] = []
data['schedule'].append({
    '1': 'đặt giờ',
    '2': 'đặt lịch',
    '3': 'hẹn giờ'    
})


data['at_now'] = []
data['at_now'].append({
    '1': 'now',
    '2': 'bây giờ',    
    '3': 'lập tức'        
})
data['before'] = []
data['before'].append({
    '1': 'đến trước',
    '2': 'tới trước',    
})
data['after'] = []
data['after'].append({
    '1': 'từ sau',
    '2': 'tới sau',    
})
data['at_time'] = []
data['at_time'].append({
    '1': 'tại lúc',
    '2': 'vào lúc'    
})
data['hour_schedule'] = []
data['hour_schedule'].append({
    '1': 'một giờ',
    '2': 'hai giờ',    
    '3': 'ba giờ',
    '4': 'bốn giờ',
    '5': 'năm giờ',
    '6': 'sáu giờ',
    '7': 'bẩy giờ',
    '8': 'tám giờ',
    '9': 'chín giờ',
    '10': 'mười một giờ',    
    '11': 'mười một giờ',
    '12': 'mười hai giờ'  
})
data['minute_schedule'] = []
data['minute_schedule'].append({
    '1': 'năm phút',
    '2': 'mười phút',
    '3': 'mười năm phút',
    '4': 'hai mươi năm phút',
    '5': 'ba mươi phút',
    '6': 'ba mươi năm phút',
    '7': 'bốn mươi phút',
    '8': 'bốn mươi năm phút',
    '9': 'năm mươi phút',
    '10': 'năm mươi năm phút'
})
data['foreign_currency'] = []
data['foreign_currency'].append({
    'content': 'tỷ giá',
    'is_active': True
})   
data['gold_rate'] = []
data['gold_rate'].append({
    'content': 'giá vàng',
    'is_active': True
})
data['gold_rate'] = []
data['gold_rate'].append({
    'content': 'vàng miếng',
    'is_active': True
})
data['day'] = []
data['day'].append({
    '1': 'hôm qua',
    '2': 'hôm nay',    
    '3': 'ngày mai',        
    '3': 'ngày kia',            
    '4': 'ngày mốt'
})
data['news'] = []
data['news'].append({
    'content': 'đọc báo',    
    'is_active': True
})
data['news'].append({
    'content': 'đọc tin',    
    'is_active': True
})
data['news'].append({
    'content': 'tin tức',    
    'is_active': True
})
data['lunar_calendar'] = []
data['lunar_calendar'].append({
    'content': 'ngày âm',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': 'lịch âm',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': 'mùng mấy',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': 'âm lịch',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': 'mồng mấy',    
    'is_active': True
})
data['camera'] = []
data['camera'].append({
    '1': 'cam',
    '2': 'camera'
})
data['movement'] = []
data['movement'].append({
    '1': 'lên',
    '2': 'xuống',
    '3': 'phải',    
    '4': 'trái',
})

data['noted_name'] = []
data['noted_name'].append({
    'content': 'bao ngày',    
    'is_active': True
})
data['noted_name'].append({
    'content': 'nhiêu ngày',    
    'is_active': True
})
data['noted_name'].append({
    'content': 'bao lâu',    
    'is_active': True
})
data['noted_name'].append({
    'content': 'nhiêu lâu',    
    'is_active': True
})
data['funny_story'] = []
data['funny_story'].append({
    '1': 'truyện cười',
    '2': 'truyện vui'
})
data['lottery'] = []
data['lottery'].append({
    'content': 'xổ số',
    'is_active': True    
})    
data['lottery'].append({
    'content': 'vé số',
    'is_active': True    
})  
data['music'] = []
data['music'].append({
    '1': 'bài hát',
    '2': 'bản nhạc',
    '3': 'bài nhạc'
})
data['download'] = []
data['download'].append({
    '1': 'load xuống',
    '2': 'download',
    '3': 'tải xuống'
})
data['online'] = []
data['online'].append({
    '1': 'trực tuyến',
    '2': 'trên mạng',
    '3': 'online'    
})
data['offline'] = []
data['offline'].append({
    '1': 'cục bộ',
    '2': 'tại chỗ',
    '3': 'offline'    
})
data['spotify'] = []
data['spotify'].append({
    '1': 'spotify',
    '2': 'spot tify'
})
data['youtube'] = []
data['youtube'].append({
    '1': 'youtube',
    '2': 'your tube',
    '3': 'iu tube'    
})
data['input'] = []
data['input'].append({
    '1': 'nhập vào',
    '2': 'điền vào',
    '3': 'đầu vào'    
})
data['select'] = []
data['select'].append({
    '1': 'lựa chọn',
    '2': 'chọn mục',
    '3': 'lựa mục'    
})
data['play'] = []
data['play'].append({
    '1': 'phát',
})
data['pause'] = []
data['pause'].append({
    '1': 'tạm dừng',
    '2': 'tạm treo'    
})
data['continue'] = []
data['continue'].append({
    '1': 'tiếp tục'
})
data['reply'] = []
data['reply'].append({
    '1': 'phát lại',
    '2': 'chơi lại',
    '3': 'bật lại'
})
data['next'] = []
data['next'].append({
    '1': 'kế tiếp',
    '2': 'tiếp theo'    
})
data['exit'] = []
data['exit'].append({
    '1': 'exit',
    '2': 'thoát',
    '3': 'stop'
})
data['when'] = []
data['when'].append({
    '1': 'khi nào',
    '2': 'lúc nào',
    '3': 'thời điểm nào',    
})
data['who'] = []
data['who'].append({
    '1': 'ai là',
    '2': 'người nào',
    '3': 'là ai',    
    '4': 'là người',        
})
data['what'] = []
data['what'].append({
    '1': 'cái gì',
    '2': 'gì nào',
    '3': 'là gì'    
})
data['where'] = []
data['where'].append({
    '1': 'ở đâu',
    '2': 'nơi nào',
    '3': 'chỗ nào',    
    '4': 'khu vực nào',        
    '5': 'tại đâu',            
})
data['why'] = []
data['why'].append({
    '1': 'vì sao',
    '2': 'tại sao',
    '3': 'vì gì'
})
data['how'] = []
data['how'].append({
    '1': 'như nào',
    '2': 'ra sao',
    '3': 'thế nào',    
})
data['wishes'] = []
data['wishes'].append({
    '1': 'chúc tết',
    '2': 'chúc năm mới',
    '3': 'chúc mừng năm mới'
})
data['person_type'] = []
data['person_type'].append({
    '1': 'cụ',
    '2': 'ông',
    '3': 'bà',
    '4': 'bác',
    '5': 'cô',
    '6': 'chú',
    '7': 'dì',
    '8': 'dượng',
    '9': 'anh',
    '10': 'chị',
    '11': 'bạn',
    '12': 'em',
    '13': 'cháu',
    '14': 'cháu nhỏ'
})
with open('request.json', 'w') as outfile:
    json.dump(data, outfile)