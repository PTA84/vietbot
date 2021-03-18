import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'ReSpeaker 2/4-Mics Pi HAT',
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Mic Array v2.0',
    'is_active': True        
})
data['mic'].append({
    'type': 'ReSpeaker Core v2.0',
    'is_active': False        
})
data['volume'] = []
data['volume'].append({
    'value': 1.0,
    'type': 'event'    
})
data['volume'].append({
    'value': 1.0,
    'type': 'speak'    
})
data['volume'].append({
    'value': 1.0,
    'type': 'playback'    
})
data['hotword'] = []
data['hotword'].append({
    'name': 'hey siri',
    'keyword_path': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': False    
})
data['hotword'].append({
    'name': 'americano',
    'keyword_path': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': False    
})
data['hotword'].append({
    'name': 'hi_vc',
    'keyword_path': 'hi_vc.ppn',    
    'sensitive': 0.3,        
    'is_active': False    
})
data['hotword'].append({
    'name': 'hey_vc',
    'keyword_path': 'hey_vc.ppn',    
    'sensitive': 0.3,        
    'is_active': False    
})
data['hotword'].append({
    'name': 'hey_vici',
    'keyword_path': 'hey_vici.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['stt_engine'] = []
data['stt_engine'].append({
    'name': 'stt_gg_free',
    'token': '',
    'token_file': '',    
    'time_out': '',
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
    'name': 'stt_viettel',
    'token': '',
    'token_file': '',    
    'time_out': '',
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
    'token': 'AIzaSyDX37sfsdfsxhw6_k16b3c',
    'token_file': 'google.json',    
    'name': 'tts_gg_cloud',    
    'voice_name': 'vi-VN-Wavenet-A',
    'speed': 1.0,
    'pitch': 0,
    'is_active': True    
})
data['tts_engine'].append({
    'token': 'SythBY7N8AUnddbzfUsdfsdfWpxlyXxzdWRNwYE8N',
    'token_file': '',    
    'name': 'tts_viettel',    
    'voice_name': 'hcm-diemmy2',
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})
data['tts_engine'].append({
    'token': '8sJJ39o7qsfxsfsdfkmBXC2fRGU',
    'token_file': '',    
    'name': 'tts_zalo',
    'voice_name': '1',    
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})    
data['tts_engine'].append({
    'token': '7591A4mrewrwesfds8PXNkyEqEC',
    'name': 'tts_fpt',
    'voice_name': 'linhsan',
    'speed': 1.0,
    'pitch': '',    
    'is_active': False    
})
data['hass_skill'] = []
data['hass_skill'].append({
    'name':'hass_skill',
    'url':'http://192.168.1.127:8123',
    'long_token': 'eyJ0eXAiOiJKV1QiLCJhbssdfdsfOWIzZjY5NWZiNTkzMSIsImlsdfdsfNzA3fQ.QSNK0ptkagGwVCL-Nd092E7FQYLNXjeVJstqnl5Ub14',
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
    'client_id': '8fcfa835ba264d5sfsdf9d0260',
    'client_secret': '5b1ae349sfsdfa60efe1b195',
    'redirect_url': 'http://localhost:3979',
    'device_id': '2244d6ab3ec1sdfsdff7b5cb22ac71571c',
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

data[''] = []
data['download_music_skill'] = []
data['download_music_skill'].append({
    'name':'download_music_skill',                
    'compare_percent': 20,
    'is_active': False
})
data['music_offline_skill'] = []
data['music_offline_skill'].append({
    'name':'music_offline_skill',
    'compare_percent': 20,    
    'is_active': False
})
data['youtube_skill'] = []
data['youtube_skill'].append({
    'name':'youtube_skill',                
    'compare_percent': 20,
    'is_active': False
})
data['wishes_skill'] = []
data['wishes_skill'].append({
    'name':'wishes_skill',                
    'is_active': False
})

    

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
