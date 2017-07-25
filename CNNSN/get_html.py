import requests
import codecs
from lxml import etree


url = 'http://www.listeningexpress.com/cnn/cnnstudentnews/CNNSN-2017-02-27-CNN-Student-News.html'
html = requests.get(url)
#print (html.text)



f = codecs.open("C:\\Users\Administrator\Desktop\Python test\get_html1.html","r")
content=f.read()
f.close()
tree=etree.HTML(content)

nodes_mp3=tree.xpath("//div[@id='wraper']/div[@id='containerLeft']/div[@id='btnsbar']/script/text()")
print (nodes_mp3)
#print (len(nodes_mp3))
nodes_mp3_txt = nodes_mp3[0]

s = nodes_mp3_txt.split('\n\n\t')
for i in s:
    print (i)

nodes=tree.xpath("//div[@id='wraper']/div[@id='containerLeft']/div[@id='srcWin']/div[@id='srcWinText']/text()")

#for i in nodes:
#    print (i)

target_txt = open(r'C:\Users\Jane\Desktop\Python test\get_html1.txt', 'w')
for i in nodes:
    i = i+'\n'
    target_txt.write(i)
target_txt.close()


#target = open(r'C:\Users\Jane\Desktop\Python_test\get_html1.html', 'w')
#for i in html.text:
#    target.write(i)
#target.close()






