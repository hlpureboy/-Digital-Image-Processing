# encoding=utf-8
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
path = 'F:/pythonprogram/work2pic/data/gray/%s'
filename = ['NatureImage/%s.tiff','ScreenContent/cim%s.bmp']
if __name__ == '__main__':
    # plt.figure(1)
    # for i in range(0,4):
    #     name = path %(filename[0] % str(i+1))
    #     im=Image.open(name)
    #     plt.sca(plt.subplot(221+i))
    #     plt.gray()
    #     plt.contour(im, origin='image')
    # plt.show()
    # plt.figure(2)
    # for i in range(0, 4):
    #     name = path % (filename[0] % str(i + 1))
    #     im = Image.open(name)
    #     plt.sca(plt.subplot(221 + i))
    #     m=array(im)
    #     plt.hist(m.flatten(),128)
    #     plt.xlim([0, 260])
    #     plt.ylim([0, 15000])
    # plt.show()
    # plt.figure(1)
    # for i in range(0,20):
    #     name = path %(filename[1] % str(i+1))
    #     im=Image.open(name)
    #     plt.sca(plt.subplot(4,5,i+1))
    #     plt.gray()
    #     plt.contour(im, origin='image')
    # plt.show()
    # plt.figure(2)
    # for i in range(0, 20):
    #     name = path % (filename[1] % str(i + 1))
    #     im = Image.open(name)
    #     plt.sca(plt.subplot(4,5,i+1))
    #     m=array(im)
    #     plt.hist(m.flatten(),128)
    #     plt.xlim([0, 260])
    #     plt.ylim([0, 15000])
    # plt.show()
    # plt.figure(2)
    for i in range(0, 20):
        name = path % (filename[1] % str(i + 1))
        _name='F:/pythonprogram/work2pic/data/histogram/%s' %('ScreenContent/cim%s.png' %str(i+1))
        im = Image.open(name)
        plt.sca(plt.subplot(1,1,1))
        m=array(im)
        plt.hist(m.flatten(),128)
        plt.xlim([0, 260])
        plt.ylim([0, 15000])
        plt.savefig(_name)
        plt.close()
    # for i in range(0, 4):
    #     name = path % (filename[0] % str(i + 1))
    #     _name='F:/pythonprogram/work2pic/data/histogram/%s' %('NatureImage/%s.png' % str(i + 1))
    #     im = Image.open(name)
    #     plt.sca(plt.subplot(1, 1, 1))
    #     m=array(im)
    #     plt.hist(m.flatten(),128)
    #     plt.xlim([0, 260])
    #     plt.ylim([0, 15000])
    #     #plt.show()
    #     plt.savefig(_name)
    #     plt.close()
'''
1.填空30
2.选择10
3.程序注释
4.简述
5.计算
6.给题型
7.填空 选择 看ppt 最基本的知识
'''