import requests

# data ='năng lượng mặt trời'

def main(data):
    list_result=''
    #HTTP Request
    url = 'https://vanbanphapluat.co/api/search?kwd='+data
    response = requests.post(url, verify=False)
    for i in range(len(response.json()['Items'])):
        ''.join([list_result,'Kết quả thứ '+i+': Văn bản số: '+ response.json()['Items'][i]['SoHieu']+', nội dung '+response.json()['Items'][i]['TrichYeu'].replace('<em>','').replace('</em>','')])
    
    # for i in range(len(list_result)):
        # print(list_result[i])


    return list_result

        
if __name__ == '__main__':
    main(data)   


    