import requests
import codecs
from lxml import etree

#函数——抓取首页
def get_index(url,file_path):
    html = requests.get(url)
    target = open('%sindex.html' % (file_path), 'w')
    for i in html.text:
        target.write(i)
    target.close()

    # 抓取单个URL值，形成列表 full_url_list
    f = codecs.open('%sindex.html' % (file_path), 'r')
    content = f.read()
    f.close()
    tree = etree.HTML(content)
    # print (content)
    html_list = tree.xpath("//div[@id='wrap']/div[@id='wrapframe']/div[@id='content']/a/@href")
    #print(html_list)
    full_url_list = []
    for i in html_list:
        i = 'http://www.listeningexpress.com' + i
        full_url_list.append(i)
    return full_url_list


#函数——抓取文本
def get_txt(url_str,file_path):
#    url = 'http://www.listeningexpress.com/cnn/cnnstudentnews/CNNSN-2017-02-27-CNN-Student-News.html'
    file_name = url_str.split("/")[-1]
    file_name = file_name.split(".")[0]
    html_content = requests.get(url_str)
#    print(html_content.text)
    html_content = html_content.text
    tree = etree.HTML(html_content)
    txt_content = tree.xpath("//div[@id='wraper']/div[@id='containerLeft']/div[@id='srcWin']/div[@id='srcWinText']/text()")

    target_txt = open('%s%s.txt' % (file_path , file_name), 'w')
    for i in txt_content:
        i = i + '\n'
        target_txt.write(i)
    target_txt.close()

#函数——抓取MP3地址并下载
def get_MP3(url_str,file_path):
    file_name = url_str.split("/")[-1]
    file_name = file_name.split(".")[0]
    html_content = requests.get(url_str)
    html_content = html_content.text
    tree = etree.HTML(html_content)

    mp3_link = tree.xpath("//div[@id='wraper']/div[@id='containerLeft']/div[@id='btnsbar']/script/text()")
    print (mp3_link)
    mp3_link_txt = mp3_link[0]
    s = mp3_link_txt.split('\r\n\t')
    s_1 = "http://www.listeningexpress.com/cnn/cnnstudentnews/"
    s_2 = s[2].split('"')[1]
    s_2 = s_2.replace(' ', '%20')
    final_mp3_url = s_1 + s_2
    print(final_mp3_url)

    # download1 = requests.get('http://www.listeningexpress.com/cnn/cnnstudentnews/CNNSN%202017-02-27%20CNN%20Student%20News.mp3')
    download1 = requests.get(final_mp3_url)
    print(download1)
    fp = open("%s%s.mp3" % (file_path , file_name) , "wb")
    fp.write(download1.content)
    fp.close()


def index_txt_read(file_path):
    try:
        read_index_txt = open('%sindex.txt' % (file_path), 'r').readlines()
        old_url_list = []
        for i in read_index_txt:
            old_url_list.append(i[:-1])
        return old_url_list
    except IOError:
        initial_txt = open('%sindex.txt' % (file_path), 'w')
        initial_txt.close()
        old_url_list = []
        return old_url_list

def index_txt_write(full_url_list,file_path):
    index_txt = open('%sindex.txt' % (file_path), 'w')
    full_url_list.sort(reverse=True)
    for i in full_url_list:
        index_txt.write(i)
        index_txt.write('\n')
    index_txt.close()


def match_index(old_url_list,new_url_list):
    index_update_list = []
    for i in new_url_list:
        if i in old_url_list:
            continue
        else:
            index_update_list.append(i)
    return index_update_list




if __name__ == '__main__':
    url = 'http://www.listeningexpress.com/cnn/cnnstudentnews/'
#    file_path = "C:\\Users\Jane\Desktop\CNNSN\\"
    file_path = "C:\\Users\Administrator\Desktop\CNNSN\\"

    old_url_list = index_txt_read(file_path) #得到历史列表
    #print(old_url_list)
    full_url_list = get_index(url, file_path)   #得到网页列表
    #print(full_url_list)
    index_update_list = match_index(old_url_list,full_url_list) #得到差值列表
    index_txt_write(full_url_list,file_path) #网页列表写入历史列表，带排序


    # 列表排序，取最新10个
#    full_url_list.sort(reverse=True)
#    full_url_list_top10 = full_url_list[:3]
#    print(full_url_list_top10)


    index_update_list.sort(reverse=True)
    print(index_update_list)

    # get_txt('http://www.listeningexpress.com/cnn/cnnstudentnews/CNNSN-2017-02-27-CNN-Student-News.html')
    # get_MP3('http://www.listeningexpress.com/cnn/cnnstudentnews/CNNSN-2017-02-27-CNN-Student-News.html')

    for i in index_update_list: #只下载差值列表的内容
        get_txt(i, file_path)
        get_MP3(i, file_path)
