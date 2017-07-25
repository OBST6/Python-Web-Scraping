import codecs
from lxml import etree

f = codecs.open("C:\\Users\\NZMCBQ\Desktop\~Python work\Web-Scraping\get_index.html","r")
content=f.read()
f.close()
tree=etree.HTML(content)

#print (content)

html_list = tree.xpath("//div[@id='wrap']/div[@id='wrapframe']/div[@id='content']/a/@href")
print (html_list)

full_url_list = []

for i in html_list:
    i = 'http://www.listeningexpress.com' + i
    print (i)
    full_url_list.append(i)

print (full_url_list)