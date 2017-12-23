# encoding=utf-8
import cv2
import numpy as np
from PIL import Image
from pylab import *
'''
利用Sobel进行图像边缘检测
Sobel算子主要作用于边缘检测，在技术上，它是以离散性差分算子，用来运算图像亮度函数的灰度值相似值
在图像的任何一点使用此算子，将会产生对应的灰度矢量或是其法矢量
'''
path = 'F:/pythonprogram/work2pic/data/gray/%s'
path2="F:/pythonprogram/work2pic/data/Filtering/"
filename = ['NatureImage/%s.tiff','ScreenContent/cim%s.bmp']
# p=path+'ScreenContent/cim1.bmp'
# img=cv2.imread(p,0)
# cv2.imshow("p",img)
# cv2.waitKey()
# SobelX=cv2.Sobel(img,-1,1,0,ksize=3)
# # x方向上的梯度
# SobelY=cv2.Sobel(img,-1,0,1,ksize=3)
# # y方向上的梯度
# sobelX=np.uint8(np.absolute(SobelX))
# # x 方向的梯度的绝对值
# sobelY=np.uint8(np.absolute(SobelY))
# # y 方向上的梯度的绝对值
# cv2.imshow("X",sobelX)
# cv2.waitKey()
# cv2.imshow("y",sobelY)
# cv2.waitKey()
# sobelXY=cv2.bitwise_or(sobelX,sobelY)
# cv2.imshow("XY",sobelXY)
# cv2.waitKey()
if __name__ == '__main__':
    # for i in range(1,5):
    #     name = path % (filename[0] % str(i))
    #     img = cv2.imread(name)
    #     SobelX = cv2.Sobel(img, -1, 1, 0, ksize=3)
    #     # x方向上的梯度
    #     SobelY = cv2.Sobel(img, -1, 0, 1, ksize=3)
    #     # y方向上的梯度
    #     sobelX = np.uint8(np.absolute(SobelX))
    #     # x 方向的梯度的绝对值
    #     sobelY = np.uint8(np.absolute(SobelY))
    #     # y 方向上的梯度的绝对值
    #     #cv2.imshow("X", sobelX)
    #     cv2.imwrite(path2+'NatureImage/'+'/X/'+str(i)+'.tiff',sobelX)
    #     #cv2.imshow("y", sobelY)
    #     #cv2.waitKey()
    #     cv2.imwrite(path2 + 'NatureImage/' + 'Y/' + str(i) + '.tiff', sobelY)
    #     sobelXY = cv2.bitwise_or(sobelX, sobelY)
    #     #cv2.imshow("XY", sobelXY)
    #     #cv2.waitKey()
    #     print path2 + 'NatureImage/' + 'XY/' + str(i) + '.tiff'
    #     cv2.imwrite(path2 + 'NatureImage/' + 'XY/' + str(i) + '.tiff', sobelXY)
    for i in range(1,21):
        name = path % (filename[1] % str(i))
        img = cv2.imread(name)
        SobelX = cv2.Sobel(img, -1, 1, 0, ksize=3)
        # x方向上的梯度
        SobelY = cv2.Sobel(img, -1, 0, 1, ksize=3)
        # y方向上的梯度
        sobelX = np.uint8(np.absolute(SobelX))
        # x 方向的梯度的绝对值
        sobelY = np.uint8(np.absolute(SobelY))
        # y 方向上的梯度的绝对值
        #cv2.imshow("X", sobelX)
        cv2.imwrite(path2+'ScreenContent/'+'/X/cim'+str(i)+'.bmp',sobelX)
        #cv2.imshow("y", sobelY)
        #cv2.waitKey()
        cv2.imwrite(path2 + 'ScreenContent/' + 'Y/cim' + str(i) + '.bmp', sobelY)
        sobelXY = cv2.bitwise_or(sobelX, sobelY)
        #cv2.imshow("XY", sobelXY)
        #cv2.waitKey()
        print path2 + 'ScreenContent/' + 'XY/cim' + str(i) + '.bmp'
        cv2.imwrite(path2 + 'ScreenContent/' + 'XY/cim' + str(i) + '.bmp', sobelXY)