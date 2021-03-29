import json
data = {}
data['ask_wakeup'] = []
data['ask_wakeup'].append({
    '1': 'chờ khẩu lệnh',    
    '2': 'đọc khẩu lệnh đi'
})
data['time_out'] = []
data['time_out'].append({
    '1': 'không thấy lệnh, quay lại chờ lệnh'   
})
data['wait'] = []
data['wait'].append({
    'content': 'Xin vui lòng chờ trong giây lát',    
    'is_active': True
})
data['wait'].append({
    'content': 'Chờ trong giây lát nhé',    
    'is_active': True
})
data['wait'].append({
    'content': 'Xin chờ giây lát',    
    'is_active': True
})
data['response'] = []
data['response'].append({
    '1': 'ok nhé',    
    '2': 'sẵn sàng',
    '3': 'có ngay',
    '4': 'chờ chút',
    '5': 'chờ xíu',
    '6': 'chờ nhé'    
})
data['no_answer'] = []
data['no_answer'].append({
    '1': 'không trả lời được',    
    '2': 'không có câu trả lời',
    '3': 'không trả lời nhé'
})
data['no_music_source'] = []
data['no_music_source'].append({
    '1': 'chọn nguồn phát nhạc',    
    '2': 'chọn một trong các nguồn phát nhạc sau'
})
data['no_lottery_location'] = []
data['no_lottery_location'].append({
    'content': 'chọn một trong các khu vực',    
    'is_active': True
})   
data['no_lottery_location'].append({
    'content': 'cần chọn các khu vực',    
    'is_active': True
})   
data['no_news_source'] = []
data['no_news_source'].append({
    'content': 'xin mời chọn tên báo',    
    'is_active': True
})
data['no_news_source'].append({
    'content': 'chọn một trong các báo sau',    
    'is_active': True
})
data['no_lunar_day'] = []
data['no_lunar_day'].append({
    'content': 'chọn hôm qua, hôm nay, ngày mai hay ngày kia',    
    'is_active': True
})
data['no_lunar_day'].append({
    'content': 'hôm qua, hôm nay, ngày mai, ngày kia, chọn ngày nào đi',    
    'is_active': True
})
data['no_lunar_day'].append({
    'content': 'xin mời chọn hôm qua, hôm nay, ngày mai, ngày kia',    
    'is_active': True
})
data['no_lunar_day'].append({
    'content': 'hôm qua, hôm nay, ngày mai, ngày kia xin mời chọn',    
    'is_active': True
})

data['no_noted_name'] = []
data['no_noted_name'].append({
    'content': 'xin mời chọn ngày',    
    'is_active': True
})  
data['no_noted_name'].append({
    'content': 'chọn một ngày sau',    
    'is_active': True
})      
data['no_foreign_currency'] = []
data['no_foreign_currency'].append({
    'content': 'xin mời chọn ngoại tệ',    
    'is_active': True
})  
data['no_foreign_currency'].append({
    'content': 'chọn một ngoại tệ sau',    
    'is_active': True
})      
data['no_gold_rate_location'] = []
data['no_gold_rate_location'].append({
    'content': 'xin mời chọn khu vực',    
    'is_active': True
})  
data['no_gold_rate_location'].append({
    'content': 'chọn một khư vực sau',    
    'is_active': True
})
data['no_song_name'] = []
data['no_song_name'].append({
    'content': 'đọc tên bài hát hoặc tên bản nhạc',    
    'is_active': True
})
data['no_song_name'].append({
    'content': 'cần đọc tên bài hát hoặc bản nhạc',    
    'is_active': True
})
data['no_input_day'] = []
data['no_input_day'].append({
    'content': 'đọc ngày và tháng',    
    'is_active': True    
})
data['end_of_response'] = []
data['end_of_response'].append({
    '1': 'nhé',    
    '2': 'đó',
    '3': 'đấy'
})
data['choose_lose'] = []
data['choose_lose'].append({
    'content': 'chọn không đúng',    
    'is_active': True
})
data['choose_lose'].append({
    'content': 'chọn sai rồi',    
    'is_active': True
})
data['choose_lose'].append({
    'content': 'đã chọn sai',    
    'is_active': True
})
data['say_nothing'] = []
data['say_nothing'].append({
    'content': 'không nhận được lệnh quay lại',
    'is_active': True
})
data['say_nothing'].append({
    'content': 'quay lại vì không nhận được lệnh',
    'is_active': True
})    
data['say_nothing'].append({
    'content': 'quay lại chờ lệnh mới',
    'is_active': False
})    
data['no_choose'] = []
data['no_choose'].append({
    '1': 'sao không chọn',    
    '2': 'không chọn thì thôi'
})
data['seach_result'] = []
data['seach_result'].append({
    '1': 'tìm thấy các kết quả',    
    '2': 'thấy được các kết quả',
    '3': 'có các kết quả'
})
data['day_within_week'] = []
data['day_within_week'].append({
    'content': 'chưa tuần nữa là đến',
    'is_active': True
})
data['day_within_week'].append({
    'content': 'mấy ngày nữa là đến',
    'is_active': True
})  
data['day_within_month'] = []
data['day_within_month'].append({
    'content': 'chưa tháng nữa là đến',
    'is_active': True
})  
data['day_within_month'].append({
    'content': 'trong tháng là đến',
    'is_active': True
}) 
data['day_over:'] = []
data['day_over:'].append({
    'content': 'còn lâu lắm mới đến',
    'is_active': True
}) 
data['day_over:'].append({
    'content': 'xa lắm mới đến',
    'is_active': True
}) 
data['day_over:'].append({
    'content': 'chờ còn lâu mới đến',
    'is_active': True
}) 

data['no_wishes'] = []
data['no_wishes'].append({
    '1': 'cần chúc người nào',
    '2': 'chúc người nào nhỉ'
})    
data['best_wishes'] = []
data['best_wishes'].append({
    'new_year': ({
    '1': 'năm mới',
    '2': 'năm tân sửu',
    '3': 'trong năm mới',
    '4': 'trong năm tân sửu',
    '5': 'vào năm mới',
    '6': 'vào năm tân sửu'
    }),    
    'elder': ({
    '1': 'sống lâu trăm tuổi',
    '2': 'khỏe mạnh', 
    '3': 'minh mẫn mạnh khỏe'
    }),
    'midle': ({
    '1': 'may mắn',
    '2': 'thành công', 
    '3': 'làm ăn phát đạt',
    '4': 'sự ngiệp thăng tiến',
    }),    
    'youth': ({
        '1': 'hạnh phúc',    
        '2': 'may mắn',
        '3': 'vui vẻ'
    }),
    'teen': ({
        '1': 'học giỏi',    
        '2': 'xinh đẹp',    
        '3': 'ngoan ngoãn',
        '4': 'dễ thương'
    }),
    'small': ({
        '1': 'học giỏi',    
        '2': 'nghe lời',
        '3': 'xinh xắn',    
        '4': 'ngoan ngoãn',
        '5': 'dễ thương'
    }),
    'baby': ({
        '1': 'hay ăn chóng lớn',    
        '2': 'ngoan',
        '3': 'nhanh lớn'    
    })
})    


with open('response.json', 'w') as outfile:
    json.dump(data, outfile)