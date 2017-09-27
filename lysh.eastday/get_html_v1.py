import requests
import datetime



now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M')
list_time = now.split(' ')
print(list_time)





#url = 'http://lyjs.eastday.com/lyj/WebApiService/api/GetSpots?t=%s' % 20170922165700
url = 'http://lyjs.eastday.com/lyj/WebApiService/api/GetSpots'
html = requests.get(url)
# html.encoding = 'gb2312'
# print (html.text)
print(type(html.text))
html_str = html.text
list1 = html_str.split('],"', 1)
list2 = list1[0].split(':[')
list3 = list2[1][1:-1].split(',')
list4 = list3[2].split(':')
cur_num = list4[1][1:-1] + '\n'
print(list1[0])
print(list2[1])
print(list3[2])
print(list4)
print(type(cur_num))
print(cur_num)


target = open('cur_num.csv', 'a')
for i in list_time:
    target.write(i + ',')
target.write(cur_num)
target.close()



