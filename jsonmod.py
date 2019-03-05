# -*- coding:utf-8 -*-
import os
import json
def process_json(input_json_file, output_json_file):
    file_in = open(input_json_file, "r")
    print(input_json_file)
    file_out = open(output_json_file, "w")
    print(output_json_file)
    # load数据到变量json_data
    json_data = json.load(file_in, strict=False)
    # 修改json中的数据
    # 此处为将imagePath项中的文件名由x.jpg修改为x (2).jpg，实际使用中请自行修改为需要的内容
    str1 = json_data["imagePath"]
    print(str1.split('.',1)[0])
    json_data["imagePath"] = str1.split('.',1)[0]+' (2).jpg'
    
    # 将修改后的数据写回文件
    file_out.write(json.dumps(json_data))
    file_in.close()
    file_out.close()
 
filedir = os.getcwd()+'/test'
filenames=os.listdir(filedir)
print(filenames)
#遍历文件名
for filename in filenames:
    print(filename)
    filepath = filedir+'/'+filename
    print(filepath)
    process_json(filepath,filename)
