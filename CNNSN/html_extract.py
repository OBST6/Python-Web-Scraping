import codecs
import requests
from lxml import etree


f = codecs.open("C:\\Users\\NZMCBQ\Desktop\~Python work\Web-Scraping\CNNSN-2017-02-27-CNN-Student-News.html","r")
content=f.read()
f.close()
tree=etree.HTML(content)

mp3_link = tree.xpath("//div[@id='wraper']/div[@id='containerLeft']/div[@id='btnsbar']/script/text()")
#print (mp3_link)
mp3_link_txt = mp3_link[0]

s = mp3_link_txt.split('\n\n\t')
#print (s[0])
#print (s[2])
s_1 = "http://www.listeningexpress.com/cnn/cnnstudentnews/"
s_2 = s[2].split('"')[1]
#print (s_2)
s_2 = s_2.replace(' ','%20')
final_mp3_url = s_1 + s_2
print (final_mp3_url)


#download1 = requests.get('http://www.listeningexpress.com/cnn/cnnstudentnews/CNNSN%202017-02-27%20CNN%20Student%20News.mp3')
download1 = requests.get(final_mp3_url)
print (download1)
fp = open("C:\\Users\\NZMCBQ\Desktop\~Python work\Web-Scraping\CNNSN 2017-02-27 CNN Student News.mp3", "wb")
fp.write(download1.content)
fp.close()

