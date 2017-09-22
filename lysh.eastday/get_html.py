import requests

url = 'http://lysh.eastday.com/#xxcx'
html = requests.get(url)
html.encoding = 'gb2312'
# print (html.text)
print(type(html.text))
html_str = html.text
print(html_str)


target = open('get.html', 'w', encoding='gb2312')
target.write(html_str)
target.close()





url = 'http://lyjs.eastday.com/lyj/WebApiService/api/GetSpots?t=%s' % 20170922165700
html = requests.get(url)
# html.encoding = 'gb2312'
# print (html.text)
print(type(html.text))
html_str = html.text
print(html_str)


target = open('get2.html', 'w', encoding = 'utf-8')
target.write(html_str)
target.close()

