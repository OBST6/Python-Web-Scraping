import requests
import codecs
from lxml import etree


Index_url = 'http://book.sfacg.com/Novel/16040/MainIndex/'
Index_html = requests.get(Index_url)
print(type(Index_html.text))
html_str = Index_html.text
print(html_str)


target = open('Index.html', 'w', encoding = 'utf-8')
for i in html_str:
    target.write(i)
target.close()


f = codecs.open('Index.html', 'r', encoding='utf-8')
content = f.read()
# print(content)
f.close()
tree = etree.HTML(content)
download_link = tree.xpath("//div[@class='container']/div[@class='wrap s-list']/"
                           "div[@class='story-catalog']/div[@class='catalog-list']/"
                           "ul/li/a/@href")
print(download_link)

