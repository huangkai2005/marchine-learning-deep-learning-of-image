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


img=cv.imread('D:\project.test\image model_test/test.png')
img=cv.resize(img,(0,0),fx=0.4,fy=0.4)
H,W,L=img.shape

#CMY(K)   (C,M,Y)=(1-R,1-G,1-B)     青(C) 品(M) 黄(Y) 黑(K)

(b, g, r) = cv.split(img)
B = b.copy()
G = g.copy()
R = r.copy()
op=0

w,h,l=img.shape

res = cv.merge((B, G, R))
cv_show(res, 1)



b = 1 - (b / 255.0)
g = 1 - (g / 255.0)
r = 1 - (r / 255.0)

img1 = cv.merge((b, g, r))
cv_show(img1, 1)

# 创建CMY通道的副本
y = b.copy()
m = g.copy()
c = r.copy()

# 确保CMY通道的值在0到1之间
y = np.clip(y, 0, 1)
m = np.clip(m, 0, 1)
c = np.clip(c, 0, 1)

# 检查结果
img_cmy = cv.merge((y, m, c))
cv_show(img_cmy, 1)

#chage y
print(1)
for i in range(0,10):
    c[:,:]+=0.1
    m[:,:]+=0.1
    img1=cv.merge((y,m,c))
    cv_show(img1,1)

m=g.copy()
c=r.copy()
#change m
print(1)
for i in range(0,10):
    m[:,:]-=0.1
    mask = m[:, :] < 0
    m[mask] = 0
    img1=cv.merge((b,m,r))
    cv_show(img1,1)
#change c
print(1)
for i in range(0,10):
    c[:,:]-=0.1
    mask = c[:, :] < 0
    c[mask] = 0
    img1=cv.merge((b,g,c))
    cv_show(img1,1)

img1=cv.merge((B,G,R))
cv_show(img1,1)
"CMYK"
(b,g,r)=cv.split(img)
b=np.float32(b)
g=np.float32(g)
r=np.float32(r)
b/=255.0
g/=255.0
r/=255.0

for i in range(0,H):
    for j in range (0,W):
        b[i][j]= np.float32(1 - b[i][j]/ cmyk(r[i][j],g[i][j],b[i][j]))
        g[i][j]= np.float32(1 - g[i][j] / cmyk(r[i][j],g[i][j],b[i][j]))
        r[i][j]= np.float32(1 - r[i][j] / cmyk(r[i][j],g[i][j],b[i][j]))
img3=cv.merge((b,g,r))
cv_show(img3,3)

y=b.copy()
m=g.copy()
c=r.copy()
#chage y
print(1)
for i in range(0,10):
    y[:,:]-=0.1
    mask=y[:,:]<0
    y[mask]=0
    img1=cv.merge((y,g,r))
    cv_show(img1,1)

#change m
print(1)
for i in range(0,10):
    m[:,:]-=0.1
    mask = m[:, :] < 0
    m[mask] = 0
    img1=cv.merge((b,m,r))
    cv_show(img1,1)
#change c
print(1)
for i in range(0,10):
    c[:,:]-=0.1
    mask = c[:, :] < 0
    c[mask] = 0
    img1=cv.merge((b,g,c))
    cv_show(img1,1)

