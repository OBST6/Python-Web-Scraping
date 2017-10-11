import requests
import codecs
from lxml import etree


def content_from_link(link_str):
#    chapter_url = 'http://book.sfacg.com/Novel/16040/29058/226853/'
    print(link_str[:-1])
    chapter_url = link_str[:-1]
    chapter_html = requests.get(chapter_url)
#    print(type(chapter_html.text))
    html_str = chapter_html.text
    print(html_str)
    target = open('chapter.html', 'w', encoding = 'utf-8')
    for i in html_str:
        target.write(i)
    target.close()

def content_from_chapter():
    f = codecs.open('chapter.html', 'r', encoding='utf-8')
    content = f.read()
    # print(content)
    f.close()
    tree = etree.HTML(content)
    download_link_1 = tree.xpath("//div[@class='wrap']/div[@class='wrap_left']/"
                                 "div[@class='content_left2']/div[@class='list_menu_title']/text()")
    print(download_link_1[0])
    chapter_title = download_link_1[0]

    download_link_2 = tree.xpath("//div[@class='wrap']/div[@class='wrap_left']/"
                                 "div[@class='content_left2']/span/div/p/text()")
    # print(download_link_2)

    target = open('%s.txt'% chapter_title, 'w', encoding='utf-8')
    for i in download_link_2:
        print(i)
        target.write(i)
    target.close()


f = codecs.open('Index_link.txt', 'r', encoding='utf-8')
content = f.readlines()
# print(content)
f.close()
for i in content:
    j = i[:-1]
    print(j)
    content_from_link(j)
    content_from_chapter()
