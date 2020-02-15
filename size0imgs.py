
import os
from urllib.request import urlopen
import cv2
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
import numpy as np


size0imgs = []
def gci(filepath):
#遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fsize = os.path.getsize(filepath+fi)
        if fsize ==0:
            size0imgs.append(fi)

gci('imgs\\')

def download(url, img_name):
    conn = urlopen(url)
    outimg = conn.read()
    data_img = cv2.imdecode(np.asarray(bytearray(outimg), dtype=np.uint8), 1)
    conn.close()#这里一定要关闭，不然爬几次之后会报连接错误
    cv2.imwrite(img_name, data_img)
    #plt.imshow(data_img)
    print(img_name+' Pic Saved!')
    return data_img


for img in size0imgs:
    img = img[:-4]
    longitude = img.split('_')[0]
    latitude = img.split('_')[1]
    img_name = "imgs\\"+longitude+'_'+latitude+".jpg"
    url = "http://api.map.baidu.com/panorama/v2?ak=your key here&width=1024&height=512&location="+longitude+","+latitude+"&coordtype=wgs84ll&fov=360"
    outimg = download(url, img_name)
