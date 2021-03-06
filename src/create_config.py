import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'None Respeaker Mic',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': True            
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
    'is_active': False        
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
data['hotword_engine'] = []
data['hotword_engine'].append({
    'name': 'snowboy',
    'is_active': True
})
data['hotword_engine'].append({
    'name': 'porcupine',
    'is_active': False
})
data['hotword'] = []
data['hotword'].append({
    'type': 'snowboy',
    'file_name': 'snowboy.umdl',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'snowboy',
    'file_name': 'subex.umdl',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'blueberry_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'terminator_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': False    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'ok google_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey google_raspberry-pi.ppn',    
    'sensitive': 0.3,        
    'is_active': True   
})
data['continuous_asking'] = []
data['continuous_asking'].append({
    'content': 'h???i li??n t???c',
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
    'token': 'SythBY7N8Afdsdfk1XxzdWRNwYE8N',
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
    'name': 'tts_gg_free',
    'voice_name': '',    
    'speed': '',
    'pitch': '',
    'is_active': False    
})
data['tts_engine'].append({
    'token': 'AIzaSw6_k16b3c',
    'token_file': 'google.json',    
    'name': 'tts_gg_cloud',    
    'voice_name': 'vi-VN-Wavenet-A',
    'profile': 'small-bluetooth-speaker-class-device',    # https://cloud.google.com/text-to-speech/docs/audio-profiles
    'speed': 1.0,
    'pitch': 0,
    'is_active': True    
})
data['tts_engine'].append({
    'token': 'SythBY7N8AUXxzdWRNwYE8N',
    'token_file': '',    
    'name': 'tts_viettel',    
    'voice_name': 'hcm-diemmy2',
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})
data['tts_engine'].append({
    'token': '8sJJ39XC2fRGU',
    'token_file': '',    
    'name': 'tts_zalo',
    'voice_name': '1',    
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})    
data['tts_engine'].append({
    'token': '7591A4mt9NkyEqEC',
    'name': 'tts_fpt',
    'voice_name': 'linhsan',
    'speed': 1.0,
    'pitch': '',    
    'is_active': False    
})
data['hass_skill'] = []
data['hass_skill'].append({
    'name':'hass_skill',
    'url':'https://192.168.1.10',
    'long_token': 'eyJ0eXAiZAnDzScXVnxlya4',
    'is_active': True        
})
data['google_ass_skill'] = []
data['google_ass_skill'].append({
    'name':'google_ass_skill',                
    'credential':'',
    'device_config':'',
    'is_active': True
})
data['google_ass_skill_2'] = []
data['google_ass_skill_2'].append({
    'name':'google_ass_skill_2',                
    'credential':'',
    'device_config':'',
    'is_active': False
})
data['news_skill'] = []
data['news_skill'].append({
    'name':'news_skill',                
    'is_active': True,
})
data['news_skill_data'] = []
data['news_skill_data'].append({    
    'name': 'd??n tr??',
    'link': 'https://dantri.com.vn/trangchu.rss',
    'is_active': True    
})
data['news_skill_data'].append({       
    'name': 'lao ?????ng',
    'link': 'https://laodong.vn/rss/home.rss',
    'is_active': True    
})
data['news_skill_data'].append({       
    'name': 'vi???t nam net',
    'link': 'https://vietnamnet.vn/rss/thoi-su-chinh-tri.rss',
    'is_active': True    
})
data['news_skill_data'].append({       
    'name': 'thanh ni??n',
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
    'day': 'h??m qua',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'h??m nay',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'ng??y mai',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'ng??y kia',    
    'is_active': True
})
data['lunar_calendar_skill_data'].append({
    'day': 'ng??y m???t',    
    'is_active': True
})
data['noted_day_skill'] = []
data['noted_day_skill'].append({
    'name':'noted_day_skill',                
    'is_active': True
})
data['noted_day_skill_data'] = []
data['noted_day_skill_data'].append({
    'name': 'sinh nh???t ch??u anh',
    'day': 3,
    'month': 10,
    'type': 'calendar',    
    'is_active': True  
})
data['noted_day_skill_data'].append({
    'name': 'sinh nh???t quang minh',
    'day': 11,
    'month': 12,
    'type': 'calendar',    
    'is_active': True   
})
data['noted_day_skill_data'].append({
    'name': 'sinh nh???t m??? nga',
    'day': 8,
    'month': 2,
    'type': 'calendar',  
    'is_active': True 
})  
data['noted_day_skill_data'].append({
    'name': 't???t d????ng l???ch',
    'day': 1,
    'month': 1,
    'type': 'calendar',  
    'is_active': True  
}) 
data['noted_day_skill_data'].append({
    'name': 'qu???c t??? lao ?????ng',
    'day': 1,
    'month': 5,
    'type': 'calendar',  
    'is_active': True
})   
data['noted_day_skill_data'].append({
    'name': 't???t ??m l???ch',
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
    'location': 'mi???n nam',
    'link': 'https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'mi???n trung',
    'link': 'https://xskt.com.vn/rss-feed/mien-trung-xsmt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'mi???n b???c',    
    'link': 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'an giang',     
    'link': 'https://xskt.com.vn/rss-feed/an-giang-xsag.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'b??nh d????ng',     
    'link': 'https://xskt.com.vn/rss-feed/binh-duong-xsbd.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'b??nh ?????nh',
    'link': 'https://xskt.com.vn/rss-feed/binh-dinh-xsbdi.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'b???c li??u',     
    'link': 'https://xskt.com.vn/rss-feed/bac-lieu-xsbl.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'b??nh ph?????c',     
    'link': 'https://xskt.com.vn/rss-feed/binh-phuoc-xsbp.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'b???n tre',   
    'link': 'https://xskt.com.vn/rss-feed/ben-tre-xsbt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'b??nh thu???n',    
    'link': 'https://xskt.com.vn/rss-feed/binh-thuan-xsbth.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'c?? mau',  
    'link': 'https://xskt.com.vn/rss-feed/ca-mau-xscm.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'c???n th??',    
    'link': 'https://xskt.com.vn/rss-feed/can-tho-xsct.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': '?????c l???c',    
    'link': 'https://xskt.com.vn/rss-feed/dac-lac-xsdlk.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': '?????ng nai',
    'link': 'https://xskt.com.vn/rss-feed/dong-nai-xsdn.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': '???? n???ng',
    'link': 'https://xskt.com.vn/rss-feed/da-nang-xsdng.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': '?????c n??ng',     
    'link': 'https://xskt.com.vn/rss-feed/dac-nong-xsdno.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': '?????ng th??p',     
    'link': 'https://xskt.com.vn/rss-feed/dong-thap-xsdt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'gia lai',     
    'link': 'https://xskt.com.vn/rss-feed/gia-lai-xsgl.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'h??? ch?? minh',
    'link': 'https://xskt.com.vn/rss-feed/tp-hcm-xshcm.rss',
     'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'h???u giang',
    'link': 'https://xskt.com.vn/rss-feed/hau-giang-xshg.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'ki??n giang',
    'link': 'https://xskt.com.vn/rss-feed/kien-giang-xskg.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'kh??nh h??a',
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
    'location': 'l??m ?????ng',
    'link': 'https://xskt.com.vn/rss-feed/lam-dong-xsld.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'ninh thu???n',
    'link': 'https://xskt.com.vn/rss-feed/ninh-thuan-xsnt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'ph?? y??n',
    'link': 'https://xskt.com.vn/rss-feed/phu-yen-xspy.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'qu???ng b??nh',
    'link': 'https://xskt.com.vn/rss-feed/quang-binh-xsqb.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'qu???ng ng??i',
    'link': 'https://xskt.com.vn/rss-feed/quang-ngai-xsqng.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'qu???ng nam',
    'link': 'https://xskt.com.vn/rss-feed/quang-nam-xsqnm.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'qu???ng tr???',
    'link': 'https://xskt.com.vn/rss-feed/quang-tri-xsqt.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 's??c tr??ng',
    'link': 'https://xskt.com.vn/rss-feed/soc-trang-xsst.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'ti???n giang',
    'link': 'https://xskt.com.vn/rss-feed/tien-giang-xstg.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 't??y ninh',
    'link': 'https://xskt.com.vn/rss-feed/tay-ninh-xstn.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'th???a thi??n hu???',
    'link': 'https://xskt.com.vn/rss-feed/thua-thien-hue-xstth.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'tr?? vinh',
    'link': 'https://xskt.com.vn/rss-feed/tra-vinh-xstv.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'v??nh long',
    'link': 'https://xskt.com.vn/rss-feed/vinh-long-xsvl.rss',
    'is_active': True    
})
data['lottery_skill_data'].append({
    'location': 'v??ng t??u',
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
    'name': '???? la',
    'code': 'USD',      
    'is_active': True    
})
data['foreign_currency_skill_data'].append({
    'name': '????la',
    'code': 'USD',      
    'is_active': True    
})
data['foreign_currency_skill_data'].append({
    'name': '?? r??',
    'code': 'EUR',    
    'is_active': True    
})    
data['foreign_currency_skill_data'].append({
    'name': '??r??',
    'code': 'EUR',    
    'is_active': True    
}) 
data['foreign_currency_skill_data'].append({
    'name': 'b???ng anh',
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
    'location': 'h?? n???i',
    'code': 'H?? N???i',    
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': '???? n???ng',
    'code': '???? N???ng',       
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'h??? ch?? minh',
    'code': 'H??? Ch?? Minh',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'nhatrang',
    'code': 'Nha Trang',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'c?? mau',
    'code': 'C?? Mau',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'hu???',
    'code': 'Hu???',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'b??nh ph?????c',
    'code': 'B??nh Ph?????c',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'mi???n t??y',
    'code': 'Mi???n T??y',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'bi??n h??a',
    'code': 'Bi??n H??a',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'qu???ng ng??i',
    'code': 'Qu???ng Ng??i',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'long xuy??n',
    'code': 'Long Xuy??n',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'b???c li??u',
    'code': 'B???c Li??u',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'quy nh??n',
    'code': 'Quy Nh??n',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'phan rang',
    'code': 'Phan Rang',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'H??? Long',
    'code': 'h??? long',           
    'is_active': True    
})
data['gold_rate_skill_data'].append({
    'location': 'Qu???ng Nam',
    'code': 'qu???ng nam',           
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
    'name1':'vi???t',    
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
    'name1':'trung qu???c',    
    'name2':'chinese',
    'code':'cn',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'nh???t',    
    'name2':'japanese',
    'code':'jp',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'h??n qu???c',    
    'name2':'korean',
    'code':'kr',        
    'is_active': True
})
data['translate_skill_data'].append({
    'name1':'ph??p',    
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
data['all'] = []
data['all'].append({
    'content': 't???t c???',
    'is_active': True
})
data['all'].append({
    'content': 'h???t c???',
    'is_active': True
})
data['all'].append({
    'content': 'to??n b???',
    'is_active': True
})
data['all'].append({
    'content': 'to??n b???',
    'is_active': True
})
data['all'].append({
    'content': '?????y ?????',
    'is_active': True
})
data['single'] = []
data['single'].append({
    'content': 'duy nh???t',
    'is_active': True
})
data['single'].append({
    'content': 'ch??? m???t',
    'is_active': True
})
data['single'].append({
    'content': 'ri??ng m???i',
    'is_active': True
})
data['single'].append({
    'content': 'duy m???i',
    'is_active': True
})
data['single'].append({
    'content': 'm???i m???t',
    'is_active': True
})
data['single'].append({
    'content': 'duy nh???t',
    'is_active': True
})
data['smart'] = []
data['smart'].append({
    'content': 'th??ng minh',
    'is_active': True
})
data['smart'].append({
    'content': 'smart',
    'is_active': True
})
data['turn_on'] = []
data['turn_on'].append({
    'content': 'b???t',
    'is_active': True
})
data['turn_on'].append({
    'content': 'm???',
    'is_active': True
})
data['download_music'] = []
data['download_music'].append({
    'content': 'download b??i',
    'is_active': True
})
data['download_music'].append({
    'content': 'download nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 'download b??i h??t',
    'is_active': True
})
data['download_music'].append({
    'content': 'download b??i nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 'download b???n nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i b??i',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i b??i h??t',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i b??i nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i b???n nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i xu???ng b??i',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i xu???ng nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i xu???ng b??i h??t',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i xu???ng b??i nh???c',
    'is_active': True
})
data['download_music'].append({
    'content': 't???i xu???ng b???n nh???c',
    'is_active': True
})

data['search_document'] = []
data['search_document'].append({
    'content': 'tra c???u v??n b???n',
    'is_active': True
})
data['search_document'] = []
data['search_document'].append({
    'content': 't??m ki???m v??n b???n',
    'is_active': True
})

data['play_music'] = []
data['play_music'].append({
    'content': 'ph??t b??i',
    'is_active': True
})
data['play_music'].append({
    'content': 'ph??t b??i h??t',
    'is_active': True
})
data['play_music'].append({
    'content': 'ph??t nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'ph??t b??i nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'ph??t b???n nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'play b??i',
    'is_active': True
})
data['play_music'].append({
    'content': 'play b??i h??t',
    'is_active': True
})
data['play_music'].append({
    'content': 'play nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'play b??i nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'play b???n nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'ch??i b??i',
    'is_active': True
})
data['play_music'].append({
    'content': 'ch??i b??i h??t',
    'is_active': True
})
data['play_music'].append({
    'content': 'ch??i nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'ch??i b??i nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'ch??i b???n nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'b???t b??i',
    'is_active': True
})
data['play_music'].append({
    'content': 'b???t b??i h??t',
    'is_active': True
})
data['play_music'].append({
    'content': 'b???t nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'b???t b??i nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'b???t b???n nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'h??t b??i',
    'is_active': True
})
data['play_music'].append({
    'content': 'h??t b??i h??t',
    'is_active': True
})
data['play_music'].append({
    'content': 'h??t nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'h??t b??i nh???c',
    'is_active': True
})
data['play_music'].append({
    'content': 'h??t b???n nh???c',
    'is_active': True
})

data['request_enable'] = []
data['request_enable'].append({
    'content': 'k??ch ho???t',
    'is_active': True
})
data['request_enable'].append({
    'content': 'th???c hi???n',
    'is_active': True
})
data['request_enable'].append({
    'content': 'thi h??nh',
    'is_active': False
})
data['turn_off'] = []
data['turn_off'].append({
    'content': 't???t',
    'is_active': True
})
data['turn_off'].append({
    'content': 'ng???t',
    'is_active': True
})
data['request_disable'] = []
data['request_disable'].append({
    'content': 'v?? hi???u',
    'is_active': True
})
data['request_disable'].append({
    'content': 'h???y b???',
    'is_active': True
})
data['light'] = []
data['light'].append({
    'content': '????n',
    'is_active': True
})
data['light'].append({
    'content': 'b??ng ??i???n',
    'is_active': True
})
data['light'].append({
    'content': '????n ??i???n',
    'is_active': True
})
data['switch'] = []
data['switch'].append({
    'content': 'c??ng t???c',
    'is_active': True
})
data['socket'] = []
data['socket'].append({
    'content': '??? c???m',
    'is_active': True
})
data['socket'].append({
    'content': '??? ??i???n',
    'is_active': True
})
data['fan'] = []
data['fan'].append({
    'content': 'qu???t',
    'is_active': True
})
data['door'] = []
data['door'].append({
    'content': 'c???a',
    'is_active': True
})    
data['door'].append({
    'content': 'c???ng',
    'is_active': True
})
data['occupancy'] = []
data['occupancy'].append({
    'content': 'pir',
    'is_active': True
})
data['occupancy'].append({
    'content': 'chuy???n ?????ng',
    'is_active': True
})
data['curtain'] = []
data['curtain'].append({
    'content': 'r??m',
    'is_active': True
})
data['curtain'].append({
    'content': 'm??nh',
    'is_active': True
})
data['curtain'].append({
    'content': 'm??n',
    'is_active': True
})
data['cover'] = []
data['cover'].append({
    'content': 'c???a cu???n',
    'is_active': True    
})
data['gate'] = []
data['gate'].append({
    'content': 'c???ng',
    'is_active': True    
})

data['unit'] = []
data['unit'].append({
    'code': 'clients',    
    'name': 'k???t n???i',
    'is_active': True    
})
data['unit'].append({
    'code': '%',    
    'name': 'ph???n tr??m',
    'is_active': True    
})
data['unit'].append({
    'code': 'MiB',    
    'name': 'm?? bai',
    'is_active': True    
})
data['unit'].append({
    'code': '??C',    
    'name': '????? x??',
    'is_active': True    
})
data['unit'].append({
    'code': 'min',    
    'name': 'ph??t',
    'is_active': True    
})
data['unit'].append({
    'code': 'km/h',    
    'name': 'ki l?? m??t tr??n gi???',
    'is_active': True    
})
data['unit'].append({
    'code': 'Hz',    
    'name': 'h??c',
    'is_active': True    
})
data['unit'].append({
    'code': 'V',    
    'name': 'v??n',
    'is_active': True    
})
data['unit'].append({
    'code': 'A',    
    'name': 'am pe',
    'is_active': True    
})
data['unit'].append({
    'code': 'kW',    
    'name': 'ki l?? o??t gi???',
    'is_active': True    
})
data['television'] = []
data['television'].append({
    '1': 'tivi',
    '2': 'tivi',    
    '3': 'v?? tuy???n'
})
data['request_temperature'] = []
data['request_temperature'].append({
    'content': 'nhi???t ?????',
    'is_active': True    
})
data['request_humidity'] = []
data['request_humidity'].append({
    'content': '????? ???m',
    'is_active': True    
})
data['request_script'] = []
data['request_script'].append({
    'content': 'k???ch b???n',
    'is_active': True    
})
data['request_sensor'] = []
data['request_sensor'].append({
    'content': 'gi?? tr???',
    'is_active': True    
})
data['request_binary_sensor'] = []
data['request_binary_sensor'].append({
    'content': 'tr???ng th??i',
    'is_active': True    
})
data['request_automation'] = []
data['request_automation'].append({
    'content': 't??? ?????ng',
    'is_active': True    
})
data['scene'] = []
data['scene'].append({
    '1': 'ho???t c???nh',
    '2': 'ng??? c???nh'    
})
data['adjust_incrase'] = []
data['adjust_incrase'].append({
    '1': 't??ng l??n',
    '2': 't??ng th??m',
    '3': 't??ng ??i'    
})
data['light_incrase'] = []
data['light_incrase'].append({
    '1': 's??ng l??n',
    '2': 's??ng th??m',
    '3': 's??ng ??i'    
})
data['incrase_volume'] = []
data['incrase_volume'].append({
    'content': 'to l??n',
    'is_active': True
})
data['incrase_volume'].append({
    'content': 'to th??m',
    'is_active': True
})
data['incrase_volume'].append({
    'content': 't??ng ??m l?????ng',
    'is_active': True
})
data['decrase_volume'] = []
data['decrase_volume'].append({
    'content': 'b?? xu???ng',
    'is_active': True
})
data['decrase_volume'].append({
    'content': 'b?? ??i',
    'is_active': True
})
data['decrase_volume'].append({
    'content': 'gi???m ??m l?????ng',
    'is_active': True
})
data['temperature_incrase'] = []
data['temperature_incrase'].append({
    '1': '???m l??n',
    '2': '???m th??m',
    '3': 'n??ng th??m'    
})
data['humidity_incrase'] = []
data['humidity_incrase'].append({
    '1': '???m l??n',
    '2': '???m th??m',
})
data['adjust_decrase'] = []
data['adjust_decrase'].append({
    '1': 'gi???m xu???ng',
    '2': 'gi???m th??m',
    '3': 'gi???m ??i'    
})
data['light_decrase'] = []
data['light_decrase'].append({
    '1': 't???i xu???ng',
    '2': 't???i ??i'
})

data['temperature_decrase'] = []
data['temperature_decrase'].append({
    '1': 'l???nh xu???ng',
    '2': 'l???nh th??m',
    '3': 'l???nh ??i'    
})
data['humidity_decrase'] = []
data['humidity_decrase'].append({
    '1': '???m xu???ng',
    '2': 'kh?? ??i'
})
data['request_check'] = []
data['request_check'].append({
    'content': 'ki???m tra',
    'is_active': True
})
data['request_check'].append({
    'content': 'hi???n th???',
    'is_active': True
})
data['request_check'].append({
    'content': 't???t hay m???',
    'is_active': True
})
data['request_check'].append({
    'content': '????ng hay m???',
    'is_active': True
})
data['request_check'].append({
    'content': 'b???t hay t???t',
    'is_active': True
})
data['setup'] = []
data['setup'].append({
    '1': 'thi???t l???p',
    '2': 'c??i ?????t',
    '3': 'thi???t ?????t'    
})

data['speedtest'] = []
data['speedtest'].append({
    'content': '???????ng truy???n internet',
    'is_active': True
})    
data['speedtest'].append({
    'content': 'k???t n???i internet',
    'is_active': True
})
data['speedtest'].append({
    'content': '???????ng internet',
    'is_active': True
})  
data['schedule'] = []
data['schedule'].append({
    '1': '?????t gi???',
    '2': '?????t l???ch',
    '3': 'h???n gi???'    
})
data['at_now'] = []
data['at_now'].append({
    '1': 'now',
    '2': 'b??y gi???',    
    '3': 'l???p t???c'        
})
data['before'] = []
data['before'].append({
    '1': '?????n tr?????c',
    '2': 't???i tr?????c',    
})
data['after'] = []
data['after'].append({
    '1': 't??? sau',
    '2': 't???i sau',    
})
data['at_time'] = []
data['at_time'].append({
    '1': 't???i l??c',
    '2': 'v??o l??c'    
})
data['hour_schedule'] = []
data['hour_schedule'].append({
    '1': 'm???t gi???',
    '2': 'hai gi???',    
    '3': 'ba gi???',
    '4': 'b???n gi???',
    '5': 'n??m gi???',
    '6': 's??u gi???',
    '7': 'b???y gi???',
    '8': 't??m gi???',
    '9': 'ch??n gi???',
    '10': 'm?????i m???t gi???',    
    '11': 'm?????i m???t gi???',
    '12': 'm?????i hai gi???'  
})
data['minute_schedule'] = []
data['minute_schedule'].append({
    '1': 'n??m ph??t',
    '2': 'm?????i ph??t',
    '3': 'm?????i n??m ph??t',
    '4': 'hai m????i n??m ph??t',
    '5': 'ba m????i ph??t',
    '6': 'ba m????i n??m ph??t',
    '7': 'b???n m????i ph??t',
    '8': 'b???n m????i n??m ph??t',
    '9': 'n??m m????i ph??t',
    '10': 'n??m m????i n??m ph??t'
})
data['foreign_currency'] = []
data['foreign_currency'].append({
    'content': 't??? gi??',
    'is_active': True
})   
data['gold_rate'] = []
data['gold_rate'].append({
    'content': 'gi?? v??ng',
    'is_active': True
})
data['gold_rate'] = []
data['gold_rate'].append({
    'content': 'v??ng mi???ng',
    'is_active': True
})
data['day'] = []
data['day'].append({
    '1': 'h??m qua',
    '2': 'h??m nay',    
    '3': 'ng??y mai',        
    '3': 'ng??y kia',            
    '4': 'ng??y m???t'
})
data['news'] = []
data['news'].append({
    'content': '?????c b??o',    
    'is_active': True
})
data['news'].append({
    'content': '?????c tin',    
    'is_active': True
})
data['news'].append({
    'content': 'tin t???c',    
    'is_active': True
})
data['lunar_calendar'] = []
data['lunar_calendar'].append({
    'content': 'ng??y ??m',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': 'l???ch ??m',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': 'm??ng m???y',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': '??m l???ch',    
    'is_active': True
})
data['lunar_calendar'].append({
    'content': 'm???ng m???y',    
    'is_active': True
})
data['camera'] = []
data['camera'].append({
    '1': 'cam',
    '2': 'camera'
})
data['movement'] = []
data['movement'].append({
    '1': 'l??n',
    '2': 'xu???ng',
    '3': 'ph???i',    
    '4': 'tr??i',
})
data['noted_name_what'] = []
data['noted_name_what'].append({
    'content': 'ng??y n??o',    
    'is_active': True
})
data['noted_name_what'].append({
    'content': 'ng??y m???y',    
    'is_active': True
})
data['noted_name_what'].append({
    'content': 'h??m n??o',    
    'is_active': True
})
data['noted_name_what'].append({
    'content': 'ng??y h??m n??o',    
    'is_active': True
})
data['noted_name_distance'] = []
data['noted_name_distance'].append({
    'content': 'bao ng??y',    
    'is_active': True
})
data['noted_name_distance'].append({
    'content': 'nhi??u ng??y',    
    'is_active': True
})
data['noted_name_distance'].append({
    'content': 'bao l??u',    
    'is_active': True
})
data['noted_name_distance'].append({
    'content': 'nhi??u l??u',    
    'is_active': True
})
data['funny_story'] = []
data['funny_story'].append({
    '1': 'truy???n c?????i',
    '2': 'truy???n vui'
})
data['lottery'] = []
data['lottery'].append({
    'content': 'x??? s???',
    'is_active': True    
})    
data['lottery'].append({
    'content': 'v?? s???',
    'is_active': True    
})  
data['music'] = []
data['music'].append({
    'content': 'b??i h??t',
    'is_active': True    
})
data['music'].append({
    'content': 'nh???c',
    'is_active': True    
})
data['download'] = []
data['download'].append({
    'content': 'load xu???ng',
    'is_active': True    
})  
data['download'].append({
    'content': 'download',
    'is_active': True    
})  
data['download'].append({
    'content': 't???i xu???ng',
    'is_active': True    
})      
data['online'] = []
data['online'].append({
    'content': 'tr???c tuy???n',
    'is_active': True    
})
data['online'].append({
    'content': 'tr??n m???ng',
    'is_active': True    
})
data['online'].append({
    'content': 'online',
    'is_active': True    
})
data['online'].append({
    'content': 'qua m???ng',
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
    'content': 'c???c b???',
    'is_active': True    
})    
data['offline'].append({
    'content': 't???i ch???',
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
    '1': 'nh???p v??o',
    '2': '??i???n v??o',
    '3': '?????u v??o'    
})
data['select'] = []
data['select'].append({
    '1': 'l???a ch???n',
    '2': 'ch???n m???c',
    '3': 'l???a m???c'    
})
data['pause'] = []
data['pause'].append({
    'content': 't???m d???ng',
    'is_active': True
})
data['continue'] = []
data['continue'].append({
    'content': 'ti???p t???c',
    'is_active': True
})
data['reply'] = []
data['reply'].append({
    'content': 'ph??t l???i',
    'is_active': True
})
data['reply'].append({
    'content': 'b???t l???i',
    'is_active': True
})
data['next'] = []
data['reply'].append({
    'content': 'k??? ti???p',
    'is_active': True
})
data['reply'].append({
    'content': 'ti???p theo',
    'is_active': True
})
data['exit'] = []
data['exit'].append({
    'content': 'exit',
    'is_active': True
})
data['exit'].append({
    'content': 'tho??t',
    'is_active': True
})
data['exit'].append({
    'content': 'stop',
    'is_active': True
})
data['when'] = []
data['when'].append({
    '1': 'khi n??o',
    '2': 'l??c n??o',
    '3': 'th???i ??i???m n??o',    
})
data['who'] = []
data['who'].append({
    '1': 'ai l??',
    '2': 'ng?????i n??o',
    '3': 'l?? ai',    
    '4': 'l?? ng?????i',        
})
data['translate'] = []
data['translate'].append({
    'content': 'd???ch t??? ?????ng',
    'is_active': True
})
data['what'] = []
data['what'].append({
    '1': 'c??i g??',
    '2': 'g?? n??o',
    '3': 'l?? g??'    
})
data['where'] = []
data['where'].append({
    '1': '??? ????u',
    '2': 'n??i n??o',
    '3': 'ch??? n??o',    
    '4': 'khu v???c n??o',        
    '5': 't???i ????u',            
})
data['why'] = []
data['why'].append({
    '1': 'v?? sao',
    '2': 't???i sao',
    '3': 'v?? g??'
})
data['how'] = []
data['how'].append({
    '1': 'nh?? n??o',
    '2': 'ra sao',
    '3': 'th??? n??o',    
})
data['wishes'] = []
data['wishes'].append({
    'wishes': 'l???i ch??c',
    'is_active': True    
})
data['wishes'].append({
    'wishes': 'ch??c m???ng',
    'is_active': True    
})
data['wishes'].append({
    '1': 'ch??c t???t',
    '2': 'ch??c n??m m???i',
    '3': 'ch??c m???ng n??m m???i'
})
data['person_type'] = []
data['person_type'].append({
    '1': 'c???',
    '2': '??ng',
    '3': 'b??',
    '4': 'b??c',
    '5': 'c??',
    '6': 'ch??',
    '7': 'd??',
    '8': 'd?????ng',
    '9': 'anh',
    '10': 'ch???',
    '11': 'b???n',
    '12': 'em',
    '13': 'ch??u',
    '14': 'ch??u nh???'
})
data['speaker'] = []
data['speaker'].append({
    'content': 'loa th??ng b??o',
    'is_active': True    
})
data['speaker'] = []
data['speaker'].append({
    'content': 'smart speaker',
    'is_active': True    
})
data['ask_wakeup'] = []
data['ask_wakeup'].append({
    '1': 'ch??? kh???u l???nh',    
    '2': '?????c kh???u l???nh ??i'
})
data['time_out'] = []
data['time_out'].append({
    '1': 'kh??ng th???y l???nh, quay l???i ch??? l???nh'   
})
data['wait'] = []
data['wait'].append({
    'content': 'Xin vui l??ng ch??? trong gi??y l??t',    
    'is_active': True
})
data['wait'].append({
    'content': 'Ch??? trong gi??y l??t nh??',    
    'is_active': True
})
data['wait'].append({
    'content': 'Xin ch??? gi??y l??t',    
    'is_active': True
})
data['response'] = []
data['response'].append({
    '1': 'ok nh??',    
    '2': 's???n s??ng',
    '3': 'c?? ngay',
    '4': 'ch??? ch??t',
    '5': 'ch??? x??u',
    '6': 'ch??? nh??'    
})
data['no_answer'] = []
data['no_answer'].append({
    '1': 'kh??ng tr??? l???i ???????c',    
    '2': 'kh??ng c?? c??u tr??? l???i',
    '3': 'kh??ng tr??? l???i nh??'
})
data['music_source'] = []
data['music_source'].append({
    'content': 't??m th???y nh???c',    
    'is_active': True
})
data['music_source'].append({
    'content': 'ph??t hi???n nh???c',    
    'is_active': True
})
data['no_music_source'] = []
data['no_music_source'].append({
    'content': 'kh??ng c?? nh???c',    
    'is_active': True
})
data['no_music_source'].append({
    'content': 'kh??ng ph??t hi???n nh???c',    
    'is_active': True
})

data['no_music_source'].append({
    'content': 'kh??ng t??m th???y nh???c',    
    'is_active': True
})
data['no_music_source'].append({
    'content': 'kh??ng c?? nh???c',    
    'is_active': True
})
data['music_online'] = []
data['music_online'].append({
    'content': 's??? d???ng nh???c tr???c tuy???n',    
    'is_active': True
})
data['music_online'].append({
    'content': 'd??ng nh???c tr???c tuy???n',    
    'is_active': True
})
data['music_offline'] = []
data['music_offline'].append({
    'content': 's??? d???ng th??? nh???',    
    'is_active': True
})
data['music_offline'].append({
    'content': 'd??ng th??? nh???',    
    'is_active': True
})
data['no_lottery_location'] = []
data['no_lottery_location'].append({
    'content': 'ch???n m???t trong c??c khu v???c',    
    'is_active': True
})   
data['no_lottery_location'].append({
    'content': 'c???n ch???n c??c khu v???c',    
    'is_active': True
})   
data['no_news_source'] = []
data['no_news_source'].append({
    'content': 'xin m???i ch???n t??n b??o',    
    'is_active': True
})
data['no_news_source'].append({
    'content': 'ch???n m???t trong c??c b??o sau',    
    'is_active': True
})
data['no_lunar_day'] = []
data['no_lunar_day'].append({
    'content': 'Ch???n m???t trong c??c ng??y sau',    
    'is_active': True
})
data['no_lunar_day'].append({
    'content': 'C??c ng??y sau ch???n m???t ng??y',    
    'is_active': True
})
data['no_noted_name'] = []
data['no_noted_name'].append({
    'content': 'xin m???i ch???n ng??y',    
    'is_active': True
})  
data['no_noted_name'].append({
    'content': 'ch???n m???t ng??y sau',    
    'is_active': True
})      
data['no_foreign_currency'] = []
data['no_foreign_currency'].append({
    'content': 'xin m???i ch???n ngo???i t???',    
    'is_active': True
})  
data['no_foreign_currency'].append({
    'content': 'ch???n m???t ngo???i t??? sau',    
    'is_active': True
})      
data['no_gold_rate_location'] = []
data['no_gold_rate_location'].append({
    'content': 'xin m???i ch???n khu v???c',    
    'is_active': True
})  
data['no_gold_rate_location'].append({
    'content': 'ch???n m???t kh?? v???c sau',    
    'is_active': True
})
data['no_song_name'] = []
data['no_song_name'].append({
    'content': '?????c t??n b??i h??t ho???c t??n b???n nh???c',    
    'is_active': True
})
data['no_song_name'].append({
    'content': 'c???n ?????c t??n b??i h??t ho???c b???n nh???c',    
    'is_active': True
})
data['no_input_day'] = []
data['no_input_day'].append({
    'content': '?????c ng??y v?? th??ng',    
    'is_active': True    
})
data['end_of_request'] = []
data['end_of_request'].append({
    'content': 'nh??',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'ngay',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'em nh??',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'ngay nh??',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'ngay n??o',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'cho anh',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': 'cho anh nh??',    
    'is_active': True    
})
data['end_of_request'].append({
    'content': '???????c kh??ng',    
    'is_active': True    
})
data['choose_lose'] = []
data['choose_lose'].append({
    'content': 'ch???n kh??ng ????ng',    
    'is_active': True
})
data['choose_lose'].append({
    'content': 'ch???n sai r???i',    
    'is_active': True
})
data['choose_lose'].append({
    'content': '???? ch???n sai',    
    'is_active': True
})
data['say_nothing'] = []
data['say_nothing'].append({
    'content': 'kh??ng nh???n ???????c l???nh quay l???i',
    'is_active': True
})
data['say_nothing'].append({
    'content': 'quay l???i v?? kh??ng nh???n ???????c l???nh',
    'is_active': True
})    
data['say_nothing'].append({
    'content': 'quay l???i ch??? l???nh m???i',
    'is_active': False
})    
data['no_choose'] = []
data['no_choose'].append({
    '1': 'sao kh??ng ch???n',    
    '2': 'kh??ng ch???n th?? th??i'
})
data['seach_result'] = []
data['seach_result'].append({
    '1': 't??m th???y c??c k???t qu???',    
    '2': 'th???y ???????c c??c k???t qu???',
    '3': 'c?? c??c k???t qu???'
})
data['day_within_week'] = []
data['day_within_week'].append({
    'content': 'ch??a tu???n n???a l?? ?????n',
    'is_active': True
})
data['day_within_week'].append({
    'content': 'm???y ng??y n???a l?? ?????n',
    'is_active': True
})  
data['day_within_month'] = []
data['day_within_month'].append({
    'content': 'ch??a th??ng n???a l?? ?????n',
    'is_active': True
})  
data['day_within_month'].append({
    'content': 'trong th??ng l?? ?????n',
    'is_active': True
}) 
data['day_over:'] = []
data['day_over:'].append({
    'content': 'c??n l??u l???m m???i ?????n',
    'is_active': True
}) 
data['day_over:'].append({
    'content': 'xa l???m m???i ?????n',
    'is_active': True
}) 
data['day_over:'].append({
    'content': 'ch??? c??n l??u m???i ?????n',
    'is_active': True
}) 
data['no_wishes'] = []
data['no_wishes'].append({
    '1': 'c???n ch??c ng?????i n??o',
    '2': 'ch??c ng?????i n??o nh???'
})    
data['best_wishes'] = []
data['best_wishes'].append({
    'new_year': ({
    '1': 'n??m m???i',
    '2': 'n??m t??n s???u',
    '3': 'trong n??m m???i',
    '4': 'trong n??m t??n s???u',
    '5': 'v??o n??m m???i',
    '6': 'v??o n??m t??n s???u'
    }),    
    'elder': ({
    '1': 's???ng l??u tr??m tu???i',
    '2': 'kh???e m???nh', 
    '3': 'minh m???n m???nh kh???e'
    }),
    'midle': ({
    '1': 'may m???n',
    '2': 'th??nh c??ng', 
    '3': 'l??m ??n ph??t ?????t',
    '4': 's??? ngi???p th??ng ti???n',
    }),    
    'youth': ({
        '1': 'h???nh ph??c',    
        '2': 'may m???n',
        '3': 'vui v???'
    }),
    'teen': ({
        '1': 'h???c gi???i',    
        '2': 'xinh ?????p',    
        '3': 'ngoan ngo??n',
        '4': 'd??? th????ng'
    }),
    'small': ({
        '1': 'h???c gi???i',    
        '2': 'nghe l???i',
        '3': 'xinh x???n',    
        '4': 'ngoan ngo??n',
        '5': 'd??? th????ng'
    }),
    'baby': ({
        '1': 'hay ??n ch??ng l???n',    
        '2': 'ngoan',
        '3': 'nhanh l???n'    
    })
})    

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
