import math

import cv2
import cv2 as cv
import  numpy as np
import matplotlib.pyplot as plt
import matplotlib
#圆周率
pi=math.pi
#图像地址
test="D:\project.test\image model_test/"
"""

RGB CMYK YUV   HSL  HSB(HSV) YCbCr HIS CMY

"""
def cv_show(img,x):
    cv.imshow('name', img)
    #cv.imwrite(test+f"test00{x}.png",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
def cmyk(r,g,b):
    k = min((1 - r, 1 - g, 1 - b))
    k = 1 - k
    k = np.float32(k)
    return k

def hsi(r,g,b):
    #r=r/255.0
    #g=g/255.0
    #b=g/255.0
    num=(r-g+r-b)
    den = 2 * math.sqrt((r - g) ** 2 + (r - b) * (g - b))
    return math.acos(num / den) if den != 0 else 0  # 避免除零错误
    #return math.acos(((r-g)+(r-b))/(2*math.sqrt((r-g)*(r-g)+(r-b)*(g-b))))

img=cv.imread('D:\project.test\image model_test/test.png')
img=cv.resize(img,(0,0),fx=0.4,fy=0.4)
H,W,L=img.shape

"通过公式我们可以发现已经实现了归一化操作了"
#HSI(Hue, Saturation, Intensity )  色调，色饱和度，亮度
"""
色调范围 0-255
色饱和度 0-100%
亮度   

"""

(b,g,r)=cv.split(img)
b=np.float32(b)
g=np.float32(g)
r=np.float32(r)
b/=255.0;g/=255.0;r/=255.0
#h
num = 0.5 * ((r- g) + (r - b))
denominator = np.sqrt((r - g) ** 2 + (r - b) * (g - b))
theta = np.arccos(num / (denominator + 1e-6))  # 加小值防止除以0

h = np.where(b <= g, theta, 2 * np.pi - theta)  # 色调范围 [0, 2π]
h = h / (2 * np.pi)  # 转换到 [0, 1]
#s
min_rgb = np.minimum(np.minimum(r, g), b)
s = 1 - (3 * min_rgb / (r + g + b + 1e-6))  # 归一化范围 [0, 1]

#i

I=(r+g+b)/3.0

img2=cv.merge((h,s,I))
cv_show(img2,2)
hh=h.copy() #注意要copy不然会影响原图
ss=s.copy()
II=I.copy()
#色调 饱和度 亮度
#switch h
img22=cv.merge((h,s,I))
cv_show(img22,22)
print(1)
hh[:,:]=2*pi
for i in range(0,11):
    hh[:,:]-=1
    img22 = cv.merge((hh, s, I))
    cv_show(img22, 22)

#swith s
img22=cv.merge((h,s,I))
cv_show(img22,22)
print(1)
ss[:,:]=0
for i in range(0,11):
    ss[:,:]+=0.1
    img22 = cv.merge((h, ss, I))
    cv_show(img22, 22)


#switch i
img22=cv.merge((h,s,I))
cv_show(img22,22)
print(1)
II[:,:]=1
for i in range(0,11):
    II[:,:]-=0.1
    img22 = cv.merge((h, s, II))
    cv_show(img22, 22)






#HSV模型 H代表色调，S代表饱和度，V代表亮度值

img=cv.imread('D:\project.test\image model_test/test.png')
img=cv.resize(img,(0,0),fx=0.4,fy=0.4)
(b,g,r)=cv.split(img)
b=np.float32(b)
g=np.float32(g)
r=np.float32(r)
v=r.copy()
s=r.copy()
num = 0.5 * ((r- g) + (r - b))
denominator = np.sqrt((r - g) ** 2 + (r - b) * (g - b))
theta = np.arccos(num / (denominator + 1e-6))  # 加小值防止除以0
h = np.where(b <= g, theta, 2 * np.pi - theta)  # 色调范围 [0, 2π]
h = h / (2 * np.pi)  # 转换到 [0, 1]
for i in range(0,H):
    for j in range(0,W):
      s[i][j]=(max((r[i][j],g[i][j],b[i][j]))-min((r[i][j],g[i][j],b[i][j])))/(max((r[i][j],g[i][j],b[i][j])))
      v[i][j]=max((r[i][j],g[i][j],b[i][j]))/255.0
img4=cv.merge((h,s,v))
cv_show(img4,4)

hh=h.copy()
ss=s.copy()
vv=v.copy()

#switch h
cv_show(img4,4)
hh[:,:]=2*pi
print(1)
for i in range(0,7):
 hh[:,:]-=1

 img22=cv.merge((hh,s,v))
 cv_show(img22,22)


#switch s
cv_show(img4,10)
ss[:,:]=0
print(1)
for i in range(0,10) :
 ss[:,:]+=0.1
 img22=cv.merge((h,ss,v))
 cv_show(img22,22)

#switch v
cv_show(img4,4)
vv[:,:]=1
print(1)
for i in range(0,11):
 vv[:,:]-=0.1
 mask=vv[:,:]<0
 vv[mask]=0
 img22=cv.merge((h,s,vv))
 cv_show(img22,22)

#BGR转HSV   内置函数
"""
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
(h,s,v)=cv.split(img_HSV)
img2=cv.merge((h,s,v))
cv_show(img2,2)
hh=h.copy()
ss=s.copy()
vv=v.copy()

img22=cv.merge((hh,ss,v))
cv_show(img22,22)

img22=cv.merge((h,ss,vv))
cv_show(img22,22)

img22=cv.merge((hh,s,vv))
"""
#cv_show(img22,22)
