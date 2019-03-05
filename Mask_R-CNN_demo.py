#!/usr/bin/env python
# coding: utf-8

# In[11]:


from maskrcnn_benchmark.config import cfg
from predictor import COCODemo


# # Mask R-CNN demo
# 
# This notebook illustrates one possible way of using `maskrcnn_benchmark` for computing predictions on images from an arbitrary URL.
# 
# Let's start with a few standard imports

# In[ ]:


import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

from os import listdir
from io import BytesIO
from PIL import Image
import numpy as np


# In[ ]:


# this makes our figures bigger
pylab.rcParams['figure.figsize'] = 20, 12


# Those are the relevant imports for the detection model

# We provide a helper class `COCODemo`, which loads a model from the config file, and performs pre-processing, model prediction and post-processing for us.
# 
# We can configure several model options by overriding the config options.
# In here, we make the model run on the CPU

# In[ ]:

# 使用的配置文件
config_file = "../configs/e2e_mask_rcnn_R_101_FPN_1x.yaml"

# update the config options with the config file
cfg.merge_from_file(config_file)
# 使用的模型权重
cfg.MODEL.WEIGHT = '../output/model_final.pth'
# manual override some options
cfg.merge_from_list(["MODEL.DEVICE", "cpu"])


# Now we create the `COCODemo` object. It contains a few extra options for conveniency, such as the confidence threshold for detections to be shown.

# In[12]:


coco_demo = COCODemo(
    cfg,
    min_image_size=800,
    confidence_threshold=0.7,
)


# Let's define a few helper functions for loading images from a URL

# In[ ]:


def imshow(img):
    plt.imshow(img[:, :, [2, 1, 0]])
    plt.axis("off")


# Let's now load an image from the COCO dataset. It's reference is in the comment

# In[ ]:

# 测试图片目录
val_path='../datasets/coco/test/' #this is the validation image data
imglistval = listdir(val_path) 
for name in imglistval:
    imgfile = val_path + name
    pil_image = Image.open(imgfile).convert("RGB")
    image = np.array(pil_image)[:, :, [2, 1, 0]]
    print(name)
 
    predictions = coco_demo.run_on_opencv_image(image) # forward predict
    plt.subplot(1, 2, 1)
    plt.imshow(image[:,:,::-1])
    plt.axis('off')
 
    plt.subplot(1, 2, 2)
    plt.imshow(predictions[:,:,::-1])
    plt.axis('off')
    plt.show()


# ### Computing the predictions
# 
# We provide a `run_on_opencv_image` function, which takes an image as it was loaded by OpenCV (in `BGR` format), and computes the predictions on them, returning an image with the predictions overlayed on the image.

# In[ ]:


# compute predictions
predictions = coco_demo.run_on_opencv_image(image)
imshow(predictions)


# ## Keypoints Demo

# In[ ]:


# set up demo for keypoints
# config_file = "../configs/caffe2/e2e_keypoint_rcnn_R_50_FPN_1x_caffe2.yaml"
# cfg.merge_from_file(config_file)
# cfg.merge_from_list(["MODEL.DEVICE", "cpu"])
# cfg.merge_from_list(["MODEL.MASK_ON", False])

# coco_demo = COCODemo(
#     cfg,
#     min_image_size=800,
#     confidence_threshold=0.7,
# )


# In[ ]:


# run demo
# image = load("http://farm9.staticflickr.com/8419/8710147224_ff637cc4fc_z.jpg")
# predictions = coco_demo.run_on_opencv_image(image)
# imshow(predictions)

