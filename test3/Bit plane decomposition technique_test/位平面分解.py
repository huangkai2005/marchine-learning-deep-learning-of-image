import cv2
import cv2 as cv
import numpy as  np
import matplotlib.pyplot as plt
import matplotlib
#位平面分解技术
#二进制位平面分解技术(BBD)
"""

0-255 8个二进制位 char类型组成的字符串构成的图像二维乃至三维数组最终组成整幅图像
高位显然对整个数的贡献更大，贪心，所有高位的像素点更加饱满接近原图像
图像压缩 图像数据隐藏 (和project4相关捏

图像压缩:因为低位对高位影响小，我们可以适当舍弃部分低位平面来实现图像压缩功能(高斯金字塔也可以用于压缩
图像数据隐藏:同样的原理，我们可以选择将低位平面数据修改隐藏我们想要参杂的数据进入其中，但是表面却看不出来
"""
def cv_show(img,x):
    cv.imshow('name',img)
    cv.waitKey(0)
    cv.imwrite(f'D:\project.test\Bit plane decomposition technique_test/Bits_test{x}.png',img)
    cv.destroyAllWindows()
img=cv.imread('D:\project.test\Bit plane decomposition technique_test/Bits_test001.png',0)
h,w=img.shape
print(h,w)
cv_show(img,0)
res=np.zeros((h,w,8),dtype=np.uint8)
for i in range(8):
    res[:,:,i]=2**i

result=np.zeros((h,w,8),dtype=np.uint8)
for i in range(8):
    result[:,:,i]=cv.bitwise_and(img,res[:,:,i])
    mask=result[:,:,i]>0
    result[mask]=255
    cv_show(result[:,:,i],i+1)


#格雷码位平面分解技术(GCBD)
"""
格雷码又叫循环二进制码或反射二进制码

格雷码相邻只有一个位发生变化便于观察
数据的改变综上所述，尽管格雷码有一些优点,
但其适用性取决于具体的应用场景和需求。
在某些情况下，格雷码可能更适合用于数字信号处理和通信，而在其他情况下，普通的二进制编码可能更合适。
但是，对于一般的图像，GCBD的每一个位平面的内容与BBD种相对于的位平面的内容几乎是完全不同的。
这种分解方法通常可以大大减小灰度变化所带来的影响。
"""
result=np.zeros((h,w,8),dtype=np.uint8)
op=result.copy()
for i in range(8):
    result[:,:,i]=cv.bitwise_and(img,res[:,:,i])
    op[:, :, i] = cv.bitwise_and(img, res[:, :, i])
    if(i) :
     for j in range(1,h):
        for k in range(1,w):
             op[j][k][i]^=result[j][k][i-1]
    mask=op[:,:,i]>0
    op[mask]=255
    cv_show(op[:,:,i],9+i)

#P-Fibonacci位平面分解(TFPBs)
