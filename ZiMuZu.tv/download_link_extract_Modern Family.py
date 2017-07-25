import codecs
from lxml import etree


#f = codecs.open("C:\\Users\\NZMCBQ\Desktop\~Python work\摩登家庭,Modern Family.htm","r",encoding="utf-8")
f = codecs.open("C:\\Users\Administrator\Desktop\摩登家庭,Modern Family.htm","r",encoding="utf-8")
content=f.read()
#print(content)
f.close()
tree = etree.HTML(content)


#download_link = tree.xpath("//div[@class='middle-box']/div[@class='box download-box']/div[@class='media-box']/div[@class='media-list']/ul/li[@format='HR-HDTV']/div[@class='fr']//@href")

download_link = tree.xpath("//div[@class='middle-box']/div[@class='w box']/div[@class='box download-box']/div[@class='media-box']/div[@class='media-list']/ul/li/div[@class='fr']//@href")
print(download_link)
ed2k_list= []
for i in download_link:
    try:
        i.index('ed2k')
        ed2k_list.append(i)
    except:
        continue

'''
ed2k_MP4_list= []
for i in ed2k_list:
    try:
        i.index('.mp4')
        ed2k_MP4_list.append(i)
    except:
        continue
print(ed2k_MP4_list)
'''




target = open('C:\\Users\Administrator\Desktop\download_list.txt', 'w')
for i in ed2k_list:
    target.write(i)
    target.write('\n')
target.close()

'''
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

'''