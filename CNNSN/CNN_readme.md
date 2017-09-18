听力特快
http://www.listeningexpress.com/cnn/cnnstudentnews/


Completed_Edition.py 函数 def index_txt_read(file_path): 优化，迭代？


CNNSN_MP3withTEXT目录中index.txt中包含所有已经扫描过的记录，下次扫描到的记录，如果已经在index.txt中，将不会再下载。
新扫描到的记录，根据参数设置只下载10个。代码：
"    index_update_list = index_update_list[:9]  # 只选取10条数据"