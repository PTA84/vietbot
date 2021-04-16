#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2012 Matt Martz
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import urllib.request
import speedtest
import requests, json 

def main():

    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    url = 'http://ip-api.com/json/'+external_ip
    response = requests.get(url) 
    isp_name = response.json()['org']
    st = speedtest.Speedtest()
    download = round(st.download()/1024000,2)
    upload= round(st.upload()/1024000,2)
    servernames = []
    st.get_servers(servernames)
    ping_result =st.results.ping
    result = 'Địa chỉ IP của mạng là ' +str(external_ip)+' thuộc về nhà mạng '+str(isp_name)+ ' với tốc độ download là '+str(download) +' Mbps, tốc độ upload là '+str(upload) +' Mbps, thời gian ping là '+str(ping_result)+' giây'
    print(result)
    return result
if __name__ == '__main__':
    main()