import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')  # 或者 'TkAgg'

test="D:\project.test\histogram_test/"
img=cv.imread('D:\project.test\histogram_test/CafeStella_screenshot_test01.png',0)
#将图像转换为rgb格式便于后续的plt输出
#img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
def cv_show(img) :
    cv.imshow('names',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
"""
cv2.calcHist(img,channels,mask,ranges)
img:原图像格式为uint8或者float32.当传入是应用中括号表示[img]
mask:掩模图像。统整幅图像的直方图就把它为None。但是如果像统图像某一分的直方图的你就制作一个掩模图像并使用它
range:像素值范围通常为[0,256]
histSize:BIN的数目。也应用中括号来 256个数值
"""
#灰度图
#None代表全区域覆盖
hist=cv.calcHist([img],[0],None,[256],[0,256]) #0代表单颜色通道
print(hist.shape)#(256, 1)
plt.title('Grayscale histogram')
plt.xlabel('Pixel value')
plt.ylabel('count')
plt.hist(img.ravel(),256)
plt.show()

#灰度图底片
res=img.copy()
print(res.shape)
h,w=res.shape
for i in range(0,h):
    for j in range(0,w):
       res[i][j]=255-res[i][j]
cv_show(res)
cv.imwrite(test+'Grayscale map_test.png',res)
plt.title('Grayscale map histogram')
plt.xlabel('Pixel value')
plt.ylabel('count')
plt.hist(img.ravel(),256)
plt.show()

#三颜色通道

img=cv.imread('D:\project.test\histogram_test/CafeStella_screenshot_test01.png')
img0=img.copy()
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
color=('b','g','r')

for i,col in enumerate(color) :
    histr=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0, 256])
plt.title('Color histogram')
plt.xlabel('Pixel value')
plt.ylabel('count')
plt.show()

#mask操作

#创建mask
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img0=cv.cvtColor(img0,cv.COLOR_BGR2GRAY)
mask=np.zeros(img.shape[:2],np.uint8)
mask[500:1000,500:1000]=255 #设置为255，框定区域全变白色
cv_show(mask)
cv_show(img0)
make_img=cv.bitwise_and(img0,img0,mask=mask)#与操作 对于所框定区域满足条件的区域就是所框定的
cv_show(make_img)
hist_full=cv.calcHist([img],[0],None,[256],[0,256])
hist_mask=cv.calcHist([img],[0],mask,[256],[0,256])
img0=cv.cvtColor(img0,cv2.COLOR_BGR2RGB)
make_img=cv.cvtColor(make_img,cv2.COLOR_BGR2RGB)
mask=cv.cvtColor(mask,cv2.COLOR_BGR2RGB)
#subplot产生连续图表
plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(make_img,'gray')
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
#直方图的均衡化
#全区域均衡化
img=cv.imread('D:\project.test\histogram_test/CafeStella_screenshot_test01.png',0)
img0=cv.equalizeHist(img)
img0=cv.equalizeHist(img0)

img0=cv.equalizeHist(img0)
plt.hist(img.ravel(),256)
plt.hist(img0.ravel(),256)
plt.show()
res=np.vstack((img,img0))#平均后但是丢失了细节信息
cv.imwrite("D:\project.test\histogram_test/Region-wide equalization001.png",res)
cv_show(res)

#部分均衡化----自适应均衡化
clahe=cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
img2=clahe.apply(img)
res2=np.hstack((img,img0,img2))
cv_show(res2)
cv.imwrite("D:\project.test\histogram_test/Region-wide equalization002.png",res2)

#多颜色通道均衡化及其合并

img=cv.imread('D:\project.test\histogram_test/CafeStella_screenshot_test01.png',1)
#分解三颜色通道
(b,g,r)=cv.split(img)
bh=cv.equalizeHist(b)
gh=cv.equalizeHist(g)
rh=cv.equalizeHist(r)
#合并均衡化后的三颜色通道
result=cv.merge((bh,gh,rh))
res=np.vstack((img,result))
cv.imwrite('D:\project.test\histogram_test/equalizeHist_color.png',res)
cv_show(res)#相对来说没那么亮和集中了
img0=cv.cvtColor(img,cv.COLOR_BGR2RGB)
resulte0=cv.cvtColor(result,cv.COLOR_BGR2RGB)
plt.hist(img0.ravel(),256)
plt.hist(resulte0.ravel(),256)
plt.show()
