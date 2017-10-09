import requests
import codecs
from lxml import etree

'''
chapter_url = 'http://book.sfacg.com/Novel/16040/29058/226853/'
chapter_html = requests.get(chapter_url)
print(type(chapter_html.text))
html_str = chapter_html.text
print(html_str)


target = open('chapter.html', 'w', encoding = 'utf-8')
for i in html_str:
    target.write(i)
target.close()

'''

f = codecs.open('chapter.html', 'r', encoding='utf-8')
content = f.read()
# print(content)
f.close()
tree = etree.HTML(content)
download_link_1 = tree.xpath("//div[@class='wrap']/div[@class='wrap_left']/"
                             "div[@class='content_left2']/div[@class='list_menu_title']/text()")
print(download_link_1)

download_link_2 = tree.xpath("//div[@class='wrap']/div[@class='wrap_left']/"
                             "div[@class='content_left2']/span/div/p/text()")
# print(download_link_2)
for i in download_link_2:
    print(i)
