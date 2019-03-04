# -*- coding: utf-8 -*-
import os
import shutil
path='D:\\Data\\1\\img'##更改为自己图片的目录，最好是绝对路径
files=os.listdir(path)
for num,file in enumerate(files):
    if os.path.splitext(file)[-1]=='.jpg':
        last_name=os.path.join(path,file)
        now_name=os.path.join(path,str(num)+'.jpg')
        if now_name==last_name:
            continue
        #shutil.copy(last_name,now_name)
        os.rename(last_name,now_name)
