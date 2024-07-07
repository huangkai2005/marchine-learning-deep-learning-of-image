import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
"""

图像分割通过简化或改变图像的表示形式，使得图像更易于分析。最简单的图像分割方法是二值化（Binarization）
图像二值化（Image Binarization）就是将图像上的像素点的灰度值设置为0或255，也就是将整个图像呈现出明显的黑白效果的过程。
二值图像每个像素只有两种取值：要么纯黑，要么纯白
由于二值图像数据足够简单，许多视觉算法都依赖二值图像。通过二值图像，能更好地分析物体的形状和轮廓。二值图像也常常用作原始图像的掩模（又称遮罩、蒙版，Mask）：它就像一张部分镂空的纸，把我们不感兴趣的区域遮掉。进行二值化有多种方式，其中最常用的就是采用阈值法（Thresholding）进行二值化。
其将大于某个临界灰度值的像素灰度设为灰度极大值，小于这个值的为灰度极小值，从而实现二值化。
阈值法又分为全局阈值（Global Method）和局部阈值（Local Method），又称自适应阈值（Adaptive Thresholding）
平均值法   双峰法    OTSU法
"""
test="D:\project.test/binary_test/"
def cv_show (img,x) :
    cv2.imshow("names",img)
    cv2.waitKey(0)
    cv.imwrite(test+f'test{x}.png',img)
    cv2.destroyAllWindows()

img=cv.imread("D:\project.test/binary_test/nini.png")
img=cv.resize(img,(0,0),fx=0.4,fy=0.4)
#平均值法
def my_binarization(img):
  img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  threshold=np.mean(img1)
  img1[img1>threshold]=255
  img1[img1<=threshold]=0
  cv_show(img1,1)

my_binarization(img)

#双峰法

def hist_binarization(img) :
    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#OTSU法
