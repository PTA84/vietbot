import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'None Respeaker Mic',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False            
})
data['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker 4-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Mic Array v2.0',
    'led_off_mode': 1,
    'led_off_color': 0xFFFF99,
    'led_wakeup_mode': 2,
    'led_wakeup_color': 0x33FFFF,    
    'is_active': True        
})
data['mic'].append({
    'type': 'ReSpeaker Core v2.0',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['volume'] = []
data['volume'].append({
    'value': 50,
    'type': 'event'    
})
data['volume'].append({
    'value': 50,
    'type': 'speak'    
})
data['volume'].append({
    'value': 50,
    'type': 'playback'    
})
data['hotword'] = []
data['hotword'].append({
    'name': 'hey siri',
    'keyword_path': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'americano',
    'keyword_path': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'blueberry',
    'keyword_path': 'blueberry_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'terminator',
    'keyword_path': 'terminator_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': False    
})
data['hotword'].append({
    'name': 'ok google',
    'keyword_path': 'ok google_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'name': 'hey google',
    'keyword_path': 'hey google_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True   
})
data['stt_engine'] = []
data['stt_engine'].append({
    'name': 'stt_gg_free',
    'token': '',
    'token_file': '',    
    'time_out': 6000,
    'is_active': False    
})
data['stt_engine'].append({
    'name': 'stt_gg_cloud',
    'token': '',
    'token_file': 'google.json',    
    'time_out': 6000,
    'is_active': True    
})
data['stt_engine'].append({
    'name': 'stt_gg_ass',
    'token': '',
    'token_file': '',    
    'time_out': 6000,
    'is_active': False    
})
data['stt_engine'].append({
    'name': 'stt_viettel',
    'token': 'SythBY7fdgdfgdfgXxzdWRNwYE8N',
    'token_file': '',    
    'time_out': 4000,
    'is_active': False    
})
data['stt_engine'].append({
    'name': 'stt_fpt',
    'token': '',
    'token_file': '',    
    'time_out': '',
    'is_active': False    
})
data['tts_engine'] = []
data['tts_engine'].append({
    'token': '',
    'token_file': '',        
    'name': 'tts_gg_free',
    'voice_name': '',    
    'speed': '',
    'pitch': '',
    'is_active': False    
})
data['tts_engine'].append({
    'token': 'AIzaSyDX3fdsdfsdfsdfxhw6_k16b3c',
    'token_file': 'google.json',    
    'name': 'tts_gg_cloud',    
    'voice_name': 'vi-VN-Wavenet-A',
    'speed': 1.0,
    'pitch': 0,
    'is_active': True    
})
data['tts_engine'].append({
    'token': 'SythBY7N8AUsfsdfsdfsdfyXxzdWRNwYE8N',
    'token_file': '',    
    'name': 'tts_viettel',    
    'voice_name': 'hcm-diemmy2',
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})
data['tts_engine'].append({
    'token': '8sJJ39osfsdfsdkmBXC2fRGU',
    'token_file': '',    
    'name': 'tts_zalo',
    'voice_name': '1',    
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})    
data['tts_engine'].append({
    'token': '7591A4mtsfsdfXNkyEqEC',
    'name': 'tts_fpt',
    'voice_name': 'linhsan',
    'speed': 1.0,
    'pitch': '',    
    'is_active': False    
})
data['hass_skill'] = []
data['hass_skill'].append({
    'name':'hass_skill',
    'url':'http://192.168.2.121:8123',
    'long_token': 'eyJ0eXAiOiJKV1QiLCJhbxOTM3ODc3NTc2fQ.Qu0soxqfRfv4h3XAIplFRU3_sYYgLQdGWe9aJtyG3DU',
    'is_active': True        
})
data['google_ass_skill'] = []
data['google_ass_skill'].append({
    'name':'google_ass_skill',                
    'credential':'',
    'device_config':'',
    'is_active': True
})
data['news_skill'] = []
data['news_skill'].append({
    'name':'news_skill',                
    'is_active': True,
})
data['news_skill_data'] = []
data['news_skill_data'].append({    
    'name': 'dân trí',
    'link': 'https://dantri.com.vn/trangchu.rss',
    'is_active': True    
})
data['news_skill_data'].append({       
    'name': 'lao động',
    'link': 'https://laodong.vn/rss/home.rss',
    'is_active': True    
})
data['news_skill_data'].append({       
    'name': 'việt nam net',
    'link': 'https://vietnamnet.vn/rss/thoi-su-chinh-tri.rss',
    'is_active': True    
})
data['news_skill_data'].append({       
    'name': 'thanh niên',
    'link': 'https://vietnamnet.vn/rss/thoi-su-chinh-tri.rss',
    'is_active': True    
})
data['lunar_calendar_skill'] = []
data['lunar_calendar_skill'].append({
    'name':'lunar_calendar_skill',                
    'is_active': True
})
data['lunar_calendar_skill_data'] = []
data['lunar_calendar_skill_data'].append({
    'day': 'hôm qua',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'hôm nay',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'ngày mai',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'ngày kia',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'ngày mốt',    
    'is_active': True
})
data['noted_day_skill'] = []
data['noted_day_skill'].append({
    'name':'noted_day_skill',                
    'is_active': True
})
data['noted_day_skill_data'] = []
data['noted_day_skill_data'].append({
    'name': 'sinh nhật châu anh',
    'day': 3,
    'month': 10,
    'type': 'calendar',    
    'is_active': True  
})
data['noted_day_skill_data'].append({
    'name': 'sinh nhật quang minh',
    'day': 11,
    'month': 12,
    'type': 'calendar',    
    'is_active': True   
})
data['noted_day_skill_data'].append({
    'name': 'sinh nhật mẹ nga',
    'day': 8,
    'month': 2,
    'type': 'calendar',  
    'is_active': True 
})  
data['noted_day_skill_data'].append({
    'name': 'tết dương lịch',
    'day': 1,
    'month': 1,
    'type': 'calendar',  
    'is_active': True  
}) 
data['noted_day_skill_data'].append({
    'name': 'quốc tế lao động',
    'day': 1,
    'month': 5,
    'type': 'calendar',  
    'is_active': True
})   
data['noted_day_skill_data'].append({
    'name': 'tết âm lịch',
    'day': '1',
    'month': '1',
    'type': 'lunar_calendar',  
    'is_active': True
})
data['lottery_skill'] = []
data['lottery_skill'].append({
    'name':'lottery_skill',                
    'is_active': True
})
data['lottery_skill_data'] = []
data['lottery_skill_data'].append({
    'location': 'miền nam',
    'link': 'https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'miền trung',
    'link': 'https://xskt.com.vn/rss-feed/mien-trung-xsmt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'miền bắc',    
    'link': 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'an giang',     
    'link': 'https://xskt.com.vn/rss-feed/an-giang-xsag.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'bình dương',     
    'link': 'https://xskt.com.vn/rss-feed/binh-duong-xsbd.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'bình định',
    'link': 'https://xskt.com.vn/rss-feed/binh-dinh-xsbdi.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'bạc liêu',     
    'link': 'https://xskt.com.vn/rss-feed/bac-lieu-xsbl.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'bình phước',     
    'link': 'https://xskt.com.vn/rss-feed/binh-phuoc-xsbp.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'bến tre',   
    'link': 'https://xskt.com.vn/rss-feed/ben-tre-xsbt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'bình thuận',    
    'link': 'https://xskt.com.vn/rss-feed/binh-thuan-xsbth.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'cà mau',  
    'link': 'https://xskt.com.vn/rss-feed/ca-mau-xscm.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'cần thơ',    
    'link': 'https://xskt.com.vn/rss-feed/can-tho-xsct.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'đắc lắc',    
    'link': 'https://xskt.com.vn/rss-feed/dac-lac-xsdlk.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'đồng nai',
    'link': 'https://xskt.com.vn/rss-feed/dong-nai-xsdn.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'đà nẵng',
    'link': 'https://xskt.com.vn/rss-feed/da-nang-xsdng.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'đắc nông',     
    'link': 'https://xskt.com.vn/rss-feed/dac-nong-xsdno.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'đồng tháp',     
    'link': 'https://xskt.com.vn/rss-feed/dong-thap-xsdt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'gia lai',     
    'link': 'https://xskt.com.vn/rss-feed/gia-lai-xsgl.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'hồ chí minh',
    'link': 'https://xskt.com.vn/rss-feed/tp-hcm-xshcm.rss',
     'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'hậu giang',
    'link': 'https://xskt.com.vn/rss-feed/hau-giang-xshg.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'kiên giang',
    'link': 'https://xskt.com.vn/rss-feed/kien-giang-xskg.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'khánh hòa',
    'link': 'https://xskt.com.vn/rss-feed/khanh-hoa-xskh.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'con tum',
    'link': 'https://xskt.com.vn/rss-feed/kon-tum-xskt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'long an',
    'link': 'https://xskt.com.vn/rss-feed/long-an-xsla.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'lâm đồng',
    'link': 'https://xskt.com.vn/rss-feed/lam-dong-xsld.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'ninh thuận',
    'link': 'https://xskt.com.vn/rss-feed/ninh-thuan-xsnt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'phú yên',
    'link': 'https://xskt.com.vn/rss-feed/phu-yen-xspy.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'quảng bình',
    'link': 'https://xskt.com.vn/rss-feed/quang-binh-xsqb.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'quảng ngãi',
    'link': 'https://xskt.com.vn/rss-feed/quang-ngai-xsqng.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'quảng nam',
    'link': 'https://xskt.com.vn/rss-feed/quang-nam-xsqnm.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'quảng trị',
    'link': 'https://xskt.com.vn/rss-feed/quang-tri-xsqt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'sóc trăng',
    'link': 'https://xskt.com.vn/rss-feed/soc-trang-xsst.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'tiền giang',
    'link': 'https://xskt.com.vn/rss-feed/tien-giang-xstg.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'tây ninh',
    'link': 'https://xskt.com.vn/rss-feed/tay-ninh-xstn.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'thừa thiên huế',
    'link': 'https://xskt.com.vn/rss-feed/thua-thien-hue-xstth.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'trà vinh',
    'link': 'https://xskt.com.vn/rss-feed/tra-vinh-xstv.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'vĩnh long',
    'link': 'https://xskt.com.vn/rss-feed/vinh-long-xsvl.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'vũng tàu',
    'link': 'https://xskt.com.vn/rss-feed/vung-tau-xsvt.rss',
    'is_active': True    
})
data['foreign_currency_skill'] = []
data['foreign_currency_skill'].append({
    'name':'foreign currency_skill',                
    'is_active': True
})
data['foreign_currency_skill_data'] = []
data['foreign_currency_skill_data'].append({
    'name': 'đô la',
    'code': 'USD',      
    'is_active': True    
})
data['foreign_currency_skill_data'].append({
    'name': 'đôla',
    'code': 'USD',      
    'is_active': True    
})
data['foreign_currency_skill_data'].append({
    'name': 'ơ rô',
    'code': 'EUR',    
    'is_active': True    
})    
data['foreign_currency_skill_data'].append({
    'name': 'ơrô',
    'code': 'EUR',    
    'is_active': True    
}) 
data['foreign_currency_skill_data'].append({
    'name': 'bảng anh',
    'code': 'GBP',        
    'is_active': True    
})
data['gold_rate_skill'] = []    
data['gold_rate_skill'].append({
    'name':'gold_rate_skill',                
    'is_active': True
})
data['gold_rate_skill_data'] = []
data['gold_rate_skill_data'].append({
    'location': 'hà nội',
    'code': 'Hà Nội',    
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'đà nẵng',
    'code': 'Đà Nẵng',       
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'hồ chí minh',
    'code': 'Hồ Chí Minh',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'nhatrang',
    'code': 'Nha Trang',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'cà mau',
    'code': 'Cà Mau',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'huế',
    'code': 'Huế',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'bình phước',
    'code': 'Bình Phước',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'miền tây',
    'code': 'Miền Tây',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'biên hòa',
    'code': 'Biên Hòa',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'quảng ngãi',
    'code': 'Quảng Ngãi',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'long xuyên',
    'code': 'Long Xuyên',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'bạc liêu',
    'code': 'Bạc Liêu',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'quy nhơn',
    'code': 'Quy Nhơn',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'phan rang',
    'code': 'Phan Rang',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'Hạ Long',
    'code': 'hạ long',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'Quảng Nam',
    'code': 'quảng nam',           
    'is_active': True    
})
data['speedtest_skill'] = []
data['speedtest_skill'].append({
    'name':'speedtest_skill',                
    'is_active': True
})
data['spotify_skill'] = []
data['spotify_skill'].append({
    'client_id': '8fcfa835ba264d599df082b62a9d0260',
    'client_secret': '5b1ae349720d4f12be696a60efe1b195',
    'redirect_url': 'http://localhost:3979',
    'device_id': '2244d6ab3ec18cf2cdb18c12f7b5cb22ac71571c',
    'is_active': False        
})
data['mqtt_skill'] = []
data['mqtt_skill'].append({
    'ip': '',
    'port': '1883',
    'username': '',
    'password': '',
    'is_active': False            
})
data['camera_skill'] = []
data['camera_skill'].append({
    'name':'camera_skill',                
    'is_active': False
})
data['compare_percent'] = []
data['compare_percent'].append({
    'type':'music_compare',                
    'value': 80
})
data['download_music_skill'] = []
data['download_music_skill'].append({
    'name':'download_music_skill',                
    'is_active': True
})
data['offline_music_skill'] = []
data['offline_music_skill'].append({
    'name':'offline_music_skill',
    'is_active': True
})
data['zingmp3_skill'] = []
data['zingmp3_skill'].append({
    'name':'zingmp3_skill',                
    'is_active': True
})
data['youtube_skill'] = []
data['youtube_skill'].append({
    'name':'youtube_skill',                
    'is_active': False
})
data['spotify_skill'] = []
data['spotify_skill'].append({
    'name':'spotify_skill',                
    'is_active': False
})
data['search_document_skill'] = []
data['search_document_skill'].append({
    'name':'search_document_skill',                
    'is_active': True
})
data['translate_skill'] = []
data['translate_skill'].append({
    'name':'translate_skill',                
    'is_active': True
})
data['translate_skill_data'] = []
data['translate_skill_data'].append({
    'name1':'việt',    
    'name2':'vietnamese',
    'code':'vi',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'anh',    
    'name2':'english',
    'code':'en',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'trung quốc',    
    'name2':'chinese',
    'code':'cn',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'nhật',    
    'name2':'japanese',
    'code':'jp',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'hàn quốc',    
    'name2':'korean',
    'code':'kr',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'pháp',    
    'name2':'francis',
    'code':'fr',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'nga',    
    'name2':'russian',
    'code':'ru',        
    'is_active': True
})
data['wishes_skill'] = []
data['wishes_skill'].append({
    'name':'wishes_skill',                
    'is_active': True
})
data['wishes_skill'] = []
data['wishes_skill'].append({
    'name':'wishes_skill',                
    'is_active': False
})
data['speaker_skill'] = []
data['speaker_skill'].append({
    'name':'speaker_skill',                
    'is_active': True
})
data['smart'] = []
data['smart'].append({
    'content': 'thông minh',
    'is_active': True
})
data['smart'].append({
    'content': 'smart',
    'is_active': True
})
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
data['turn_on'] = []
data['turn_on'].append({
    'content': 'bật',
    'is_active': True
})
data['turn_on'].append({
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
data['music_source'] = []
data['music_source'].append({
    'content': 'tìm thấy nhạc',    
    'is_active': True
})
data['music_source'].append({
    'content': 'phát hiện nhạc',    
    'is_active': True
})
data['no_music_source'] = []
data['no_music_source'].append({
    'content': 'không có nhạc',    
    'is_active': True
})
data['no_music_source'].append({
    'content': 'không phát hiện nhạc',    
    'is_active': True
})
data['no_music_source'].append({
    'content': 'không tìm thấy nhạc',    
    'is_active': True
})
data['no_music_source'].append({
    'content': 'không có nhạc',    
    'is_active': True
})
data['music_online'] = []
data['music_online'].append({
    'content': 'sử dụng nhạc trực tuyến',    
    'is_active': True
})
data['music_online'].append({
    'content': 'dùng nhạc trực tuyến',    
    'is_active': True
})
data['request_enable'] = []
data['request_enable'].append({
    'content': 'kích hoạt',
    'is_active': True
})
data['request_enable'].append({
    'content': 'thực hiện',
    'is_active': True
})
data['music_offline'] = []
data['music_offline'].append({
    'content': 'sử dụng thẻ nhớ',    
    'is_active': True
})
data['music_offline'].append({
    'content': 'dùng thẻ nhớ',    
    'is_active': True
})
data['request_enable'].append({
    'content': 'thi hành',
    'is_active': False
})
data['turn_off'] = []
data['turn_off'].append({
    'content': 'tắt',
    'is_active': True
})
data['turn_off'].append({
    'content': 'ngắt',
    'is_active': True
})
data['request_disable'] = []
data['request_disable'].append({
    'content': 'vô hiệu',
    'is_active': True
})
data['request_disable'].append({
    'content': 'hủy bỏ',
    'is_active': True
})
data['light'] = []
data['light'].append({
    'content': 'đèn',
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
data['unit'] = []
data['unit'].append({
    'code': 'clients',    
    'name': 'kết nối',
    'is_active': True    
})
data['unit'].append({
    'code': '%',    
    'name': 'phần trăm',
    'is_active': True    
})
data['unit'].append({
    'code': 'MiB',    
    'name': 'mê bai',
    'is_active': True    
})
data['unit'].append({
    'code': '°C',    
    'name': 'độ xê',
    'is_active': True    
})
data['unit'].append({
    'code': 'min',    
    'name': 'phút',
    'is_active': True    
})
data['unit'].append({
    'code': 'km/h',    
    'name': 'ki lô mét trên giờ',
    'is_active': True    
})
data['unit'].append({
    'code': 'Hz',    
    'name': 'héc',
    'is_active': True    
})
data['unit'].append({
    'code': 'V',    
    'name': 'vôn',
    'is_active': True    
})
data['unit'].append({
    'code': 'A',    
    'name': 'am pe',
    'is_active': True    
})
data['unit'].append({
    'code': 'kW',    
    'name': 'ki lô oát giờ',
    'is_active': True    
})
data['television'] = []
data['television'].append({
    '1': 'tivi',
    '2': 'tivi',    
    '3': 'vô tuyến'
})
data['request_temperature'] = []
data['request_temperature'].append({
    'content': 'nhiệt độ',
    'is_active': True    
})
data['request_sensor'] = []
data['request_sensor'].append({
    'content': 'giá trị',
    'is_active': True    
})
data['request_binary_sensor'] = []
data['request_binary_sensor'].append({
    'content': 'trạng thái',
    'is_active': True    
})
data['request_humidity'] = []
data['request_humidity'].append({
    'content': 'độ ẩm',
    'is_active': True    
})
data['request_script'] = []
data['request_script'].append({
    'content': 'kịch bản',
    'is_active': True    
})
data['request_automation'] = []
data['request_automation'].append({
    'content': 'tự động',
    'is_active': True    
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
data['request_check'] = []
data['request_check'].append({
    'content': 'kiểm tra',
    'is_active': True
})
data['request_check'].append({
    'content': 'hiển thị',
    'is_active': True
})
data['request_check'].append({
    'content': 'tắt hay mở',
    'is_active': True
})
data['request_check'].append({
    'content': 'đóng hay mở',
    'is_active': True
})
data['request_check'].append({
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
    'content': 'Chọn một trong các ngày sau',    
    'is_active': True
})
data['no_lunar_day'].append({
    'content': 'Các ngày sau chọn một ngày',    
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
data['end_of_request'] = []
data['end_of_request'].append({
    'content': 'nhé',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'ngay',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'em nhé',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'ngay nhé',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'ngay nào',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'cho anh',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'cho anh nhé',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'được không',    
    'is_active': True    
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

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
