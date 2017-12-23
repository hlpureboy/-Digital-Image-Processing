# encoding=utf-8
from PIL import Image
from pylab import *
'''
对图像进行灰度化处理
'''
path = 'F:/pythonprogram/work2pic/data/rgb/%s'
filename = ['NatureImage/%s.tiff','ScreenContent/cim%s.bmp']
def rgb2gray(filename,path):
    pathname=path %filename
    img=Image.open(pathname).convert('L')
    img.save('F:/pythonprogram/work2pic/data/gray/'+filename)
if __name__ == '__main__':
    for i in range(1,21):
        name=filename[1] %str(i)
        rgb2gray(name,path)
    for i in range(1,5):
        name=filename[0] %str(i)
        rgb2gray(name,path)
