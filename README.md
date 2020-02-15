# baiduCrawler
A panorama crawler based on Baidu Maps open API.
usage: 

## baiduCrawler.py

1. Manually create a txt file "locations.txt" under the project directory, in the file put latitude and longitude coordinates you want to craw like this:  
108.957158,34.270684  
108.953492,34.261614  
108.953421,34.264836  
...  
2. Run `py -3 -m baiduCrawler.py`  
3. The program will automaticlly create a "imgs" file under the project directory  
4. Packages needed for this project：  
`py -3 -m pip install urllib `  
`py -3 -m pip install opencv-python`  
`py -3 -m pip install numpy`   

## size0imgs.py

Some coordinates may return invalid pictures for the first time, run `py -3 size0imgs.py` to re-crawl those invalid pictures(0 size).


