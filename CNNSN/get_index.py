import requests



url = 'http://www.listeningexpress.com/cnn/cnnstudentnews/'
html = requests.get(url)
#print (html.text)

target = open('C:\\Users\\NZMCBQ\Desktop\~Python work\Web-Scraping\get_index.html', 'w')
for i in html.text:
    target.write(i)
target.close()



