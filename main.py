import requests
import time
import csv

URL = 'https://fgis.gost.ru/fundmetrology/eapi/mit'
params = {
    'search': '*',
    'rows': 100,
    'start': 0
}
inc = 0
count = 0
l_list = requests.get(URL, params=params)
j_list = l_list.json()
s = j_list['result']['count']
si_types = []
str_temp = {}
time.sleep(1)
while count < 500:
    params = {
        'search': '*',
        'rows': 100,
        'start': count * 100
    }
    l_list = requests.get(URL, params=params)
    j_list = l_list.json()
    inc = 0
    while inc < 100:
        str_temp = j_list['result']['items'][inc]
        si_types.append(str_temp)
        if j_list['result']['items'][inc]['manufactorer'] == \
                'ООО "Комдиагностика", г.Москва':
            print(j_list['result']['items'][inc]['mit_id'] +
                  ' ' + j_list['result']['items'][inc]['title'] +
                  ' ' + j_list['result']['items'][inc]['notation'])
        inc += 1
    count += 1
    print(count)
    time.sleep(2)
with open('file_w.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, str_temp.keys())
    for line in si_types:
        writer.writerow(line)
print(s)
