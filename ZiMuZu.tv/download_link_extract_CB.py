import codecs
from lxml import etree

f = codecs.open("code_blue.htm","r",encoding="utf-8")
content=f.read()
#print(content)
f.close()
tree=etree.HTML(content)


#download_link = tree.xpath("//div[@class='middle-box']/div[@class='box download-box']/div[@class='media-box']/div[@class='media-list']/ul/li[@format='HR-HDTV']/div[@class='fr']//@href")

download_link = tree.xpath("//div[@class='middle-box']/div[@class='w box']/div[@class='box download-box']/div[@class='media-box']/div[@class='media-list']/ul/li/div[@class='fr']//@href")
print(download_link)
ed2k_list= []
for i in download_link:
    try:
        i.index('ed2k') #筛选条件1
#        i.index('1024')  #筛选条件2
        ed2k_list.append(i)
    except:
        continue


target = open('code_blue.htm.txt', 'w')
for i in ed2k_list:
    target.write(i)
    target.write('\n')
target.close()
