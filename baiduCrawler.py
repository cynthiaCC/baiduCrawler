# _*_ coding: utf-8 _*_

from urllib.request import urlopen
import cv2
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
import numpy as np

def mkdir(path):
    import os
    path = path.strip()
    path = path.rstrip("\\")
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


# 定义要创建的目录
mkpath = "imgs\\"

mkdir(mkpath)
def download(url, img_name):
    conn = urlopen(url)
    outimg = conn.read()
    data_img = cv2.imdecode(np.asarray(bytearray(outimg), dtype=np.uint8), 1)
    conn.close()#这里一定要关闭，不然爬几次之后会报连接错误
    cv2.imwrite(img_name, data_img)
    #plt.imshow(data_img)
    print(img_name+' Pic Saved!')
    return data_img

f = open("locations.txt", "r")
lines = f.read()
for line in lines.split('\n'):
    longitude = line.split(',')[0]
    latitude = line.split(',')[1]
    img_name = "imgs\\"+longitude+'_'+latitude+".jpg"
    url = "http://api.map.baidu.com/panorama/v2?ak=your key here&width=1024&height=512&location="+longitude+","+latitude+"&coordtype=wgs84ll&fov=360"
    outimg = download(url, img_name)

f.close()

