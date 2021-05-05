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
    'content': 'bật',
    'is_active': True
})
data['on'].append({
    'content': 'mở',
    'is_active': True
})
data['download_music'] = []
data['download_music'].append({
    'content': 'download bài',
    'is_active': True
})
data['download_music'].append({
    'content': 'download nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'download bài hát',
    'is_active': True
})
data['download_music'].append({
    'content': 'download bài nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'download bản nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải bài',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải bài hát',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải bài nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải bản nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải xuống bài',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải xuống nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải xuống bài hát',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải xuống bài nhạc',
    'is_active': True
})
data['download_music'].append({
    'content': 'tải xuống bản nhạc',
    'is_active': True
})

data['search_document'] = []
data['search_document'].append({
    'content': 'tra cứu văn bản',
    'is_active': True
})
data['search_document'] = []
data['search_document'].append({
    'content': 'tìm kiếm văn bản',
    'is_active': True
})

data['play_music'] = []
data['play_music'].append({
    'content': 'phát bài',
    'is_active': True
})
data['play_music'].append({
    'content': 'phát bài hát',
    'is_active': True
})
data['play_music'].append({
    'content': 'phát nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'phát bài nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'phát bản nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'play bài',
    'is_active': True
})
data['play_music'].append({
    'content': 'play bài hát',
    'is_active': True
})
data['play_music'].append({
    'content': 'play nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'play bài nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'play bản nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'chơi bài',
    'is_active': True
})
data['play_music'].append({
    'content': 'chơi bài hát',
    'is_active': True
})
data['play_music'].append({
    'content': 'chơi nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'chơi bài nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'chơi bản nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'bật bài',
    'is_active': True
})
data['play_music'].append({
    'content': 'bật bài hát',
    'is_active': True
})
data['play_music'].append({
    'content': 'bật nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'bật bài nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'bật bản nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'hát bài',
    'is_active': True
})
data['play_music'].append({
    'content': 'hát bài hát',
    'is_active': True
})
data['play_music'].append({
    'content': 'hát nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'hát bài nhạc',
    'is_active': True
})
data['play_music'].append({
    'content': 'hát bản nhạc',
    'is_active': True
})

data['enable'] = []
data['enable'].append({
    'content': 'kích hoạt',
    'is_active': True
})
data['enable'].append({
    'content': 'thực hiện',
    'is_active': True
})
data['enable'].append({
    'content': 'thi hành',
    'is_active': True
})
data['off'] = []
data['off'].append({
    'content': 'tắt',
    'is_active': True
})
data['off'].append({
    'content': 'ngắt',
    'is_active': True
})
data['disable'] = []
data['disable'].append({
    'content': 'vô hiệu',
    'is_active': True
})
data['disable'].append({
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
data['incrase_volume'] = []
data['incrase_volume'].append({
    'content': 'to lên',
    'is_active': True
})
data['incrase_volume'].append({
    'content': 'to thêm',
    'is_active': True
})
data['incrase_volume'].append({
    'content': 'tăng âm lượng',
    'is_active': True
})
data['decrase_volume'] = []
data['decrase_volume'].append({
    'content': 'bé xuống',
    'is_active': True
})
data['decrase_volume'].append({
    'content': 'bé đi',
    'is_active': True
})
data['decrase_volume'].append({
    'content': 'giảm âm lượng',
    'is_active': True
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
data['noted_name_what'] = []
data['noted_name_what'].append({
    'content': 'ngày nào',    
    'is_active': True
})
data['noted_name_what'].append({
    'content': 'ngày mấy',    
    'is_active': True
})
data['noted_name_what'].append({
    'content': 'hôm nào',    
    'is_active': True
})
data['noted_name_what'].append({
    'content': 'ngày hôm nào',    
    'is_active': True
})
data['noted_name_distance'] = []
data['noted_name_distance'].append({
    'content': 'bao ngày',    
    'is_active': True
})
data['noted_name_distance'].append({
    'content': 'nhiêu ngày',    
    'is_active': True
})
data['noted_name_distance'].append({
    'content': 'bao lâu',    
    'is_active': True
})
data['noted_name_distance'].append({
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
    'content': 'bài hát',
    'is_active': True    
})
data['music'].append({
    'content': 'nhạc',
    'is_active': True    
})
data['download'] = []
data['download'].append({
    'content': 'load xuống',
    'is_active': True    
})  
data['download'].append({
    'content': 'download',
    'is_active': True    
})  
data['download'].append({
    'content': 'tải xuống',
    'is_active': True    
})      
data['online'] = []
data['online'].append({
    'content': 'trực tuyến',
    'is_active': True    
})
data['online'].append({
    'content': 'trên mạng',
    'is_active': True    
})
data['online'].append({
    'content': 'online',
    'is_active': True    
})
data['online'].append({
    'content': 'qua mạng',
    'is_active': True    
})  
data['online'].append({
    'content': 'internet',
    'is_active': True    
})     
data['offline'] = []
data['offline'].append({
    'content': 'offline',
    'is_active': True    
})    
data['offline'].append({
    'content': 'cục bộ',
    'is_active': True    
})    
data['offline'].append({
    'content': 'tại chỗ',
    'is_active': True    
})
data['offline'].append({
    'content': 'local',
    'is_active': True    
})    
data['spotify'] = []
data['spotify'].append({
    'content': 'spotify',
    'is_active': True    
})
data['spotify'].append({
    'content': 'spoti fy',
    'is_active': True    
})
data['youtube'] = []
data['youtube'].append({
    'content': 'youtube',
    'is_active': True    
})
data['youtube'].append({
    'content': 'your tube',
    'is_active': True    
})
data['youtube'].append({
    'content': 'iu tube',
    'is_active': True    
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
data['pause'] = []
data['pause'].append({
    'content': 'tạm dừng',
    'is_active': True
})
data['continue'] = []
data['continue'].append({
    'content': 'tiếp tục',
    'is_active': True
})
data['reply'] = []
data['reply'].append({
    'content': 'phát lại',
    'is_active': True
})
data['reply'].append({
    'content': 'bật lại',
    'is_active': True
})
data['next'] = []
data['reply'].append({
    'content': 'kế tiếp',
    'is_active': True
})
data['reply'].append({
    'content': 'tiếp theo',
    'is_active': True
})
data['exit'] = []
data['exit'].append({
    'content': 'exit',
    'is_active': True
})
data['exit'].append({
    'content': 'thoát',
    'is_active': True
})
data['exit'].append({
    'content': 'stop',
    'is_active': True
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
data['translate'] = []
data['translate'].append({
    'content': 'dịch tự động',
    'is_active': True
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
    'wishes': 'lời chúc',
    'is_active': True    
})
data['wishes'].append({
    'wishes': 'chúc mừng',
    'is_active': True    
})
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

data['speaker'] = []
data['speaker'].append({
    'content': 'loa thông báo',
    'is_active': True    
})
data['speaker'] = []
data['speaker'].append({
    'content': 'smart speaker',
    'is_active': True    
})

with open('request.json', 'w') as outfile:
    json.dump(data, outfile)
