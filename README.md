# 杂货铺

## Mask_R-CNN_demo.py
用于Mask R-CNN Benchmark的测试。

## labelme2COCO.py
将labelme标注文件转换为coco数据集格式

## rename.py
批量更改文件夹中图片名字（e.g. 1.jpg,2.jpg,..)

## jsonmod.py
用于批量更改json文件中的信息

## cocoappend.py
用于融合COCO数据集与自建数据集。 

**Windows: **
```python cocoappend.py --original_COCO_file D:\annotations\instances_val2014.json --your_COCO_file D:\mintdata\container\coco\annotations\instances_train2014.json --COCO_image_folder D:\val2014\ --labels {person,car,truck} --numbers 50 --appended_COCO_file D:\mintdata\container\coco\appended.json --custom_image_folder D:\mintdata\container\coco\custom\```

**Linux: **
```python cocoappend.py --original_COCO_file /media/edible/Document/annotations/instances_val2014.json --your_COCO_file /media/edible/Document/googleimage/images_v2/new.json --COCO_image_folder /media/edible/Document/val2014/ --labels person,car,truck --numbers 200 --appended_COCO_file /media/edible/Document/googleimage/images_v2/appended.json --custom_image_folder /media/edible/Document/googleimage/images_v2/```
