# project 4 :

$$
kai \ huang\\
May \ 24,2024
$$

## 大纲

**1.边缘检测**

**2.图像去噪**

**3.图像增强**

**4.形态学操作**

**5.特征提取**

**6.python code**

## 边缘检测

### 简单经典的canny边缘检测算法

### 1.高斯滤波除噪音

利用高斯分布，靠近卷积核中心的数值最大，使得像素值分布变得均匀来模糊图像去除显眼的噪音点

例如：以下是5*5的一个卷积核

$$
G=\frac{1}{275} *
\left[
\matrix{
  1 & 4 & 7 & 4 & 1\\
   4 &16&26&16&4\\
   7&26&41&26&7\\
   4&16&26&16&4\\
   1&4&7&4&1
}
    
  \right  ]
$$
以下是效果展示：

![001](D:\project.test\filtering\001.jpg)

![GaussianBlur](D:\project.test\filtering\GaussianBlur.jpg)

### 2.计算梯度大小，选取最大梯度边界，得到最初边缘

#### **sobel算子**

利用soble算子得到最初始的边缘信息
$$
\theta=arctan(Gy/Gx) \ \ slope
$$

$$
G=\sqrt{Gx^2+Gy^2}
$$

$$
Sx=\left[              
\matrix{
  -1 & 0 &1\\
  -2 & 0& 2\\     
  -1 & 0& 1 
}
\right]

\  \ \ Sy=\left[              
\matrix{
  1 & 2 &1\\
  0 & 0& 0\\     
  -1& -2& -1 
}
\right]
$$

### 3.非极大值抑制(NMS算法)

在进行sobel算子后边缘任然不是很确定，我们要对他们进行再一轮检测，对边缘内外梯度不是极大值的点进行消除

![屏幕截图 2024-05-26 210601](C:\Users\黄凯\Pictures\Screenshots\屏幕截图 2024-05-26 210601.png)

#### 线性插值法

**线性插值法:设g1的梯度幅度M(g1),g2的梯度幅度M(g2),则dtmp1可以得到:M(dtmp1)=w * M(g2)+(1- w) * M(g1) **
**其中w=dist(dtmp1,g2)/dist(g1,g2)  dist指的是两者的距离**
**对于每个像素点，进行非极大值抑制，对于非边缘像素我们要将其过滤掉，将模糊的边界变得清晰**

对于在边缘领域内是极大值的我们保留，否则消去抑制

### 4.双阈值法检测真实和潜在的边界

如果图像中像素点大于阈值上界则被认为是应该保留的(称为强边界),小于阈值下界的必然不是边界,两者之间被认为是候选项(称为弱边界),需要进一步处理

![屏幕截图 2024-05-26 211508](C:\Users\黄凯\Pictures\Screenshots\屏幕截图 2024-05-26 211508.png)

![屏幕截图 2024-05-26 211519](C:\Users\黄凯\Pictures\Screenshots\屏幕截图 2024-05-26 211519.png)

#### 比较不同阈值的边缘

上面是低阈值图像

下面是高阈值图像

阈值太低会带有虚假的边界信息，阈值太高会失去一些真实的边界信息，需要适当选择阈值

![Canny_test001](C:\Users\黄凯\Desktop\科研\my_project\test4\Edge detetion\Canny_test001.jpg)

### 5.削弱边界

利用滞后技术来跟踪边界。若某一像素位置和强边界相连的弱边界认为是边界，其他的弱边界则被删除(canny算子)

## 图像去噪

### 1.滤波器

以下为原图：

![001](C:\Users\黄凯\Desktop\科研\my_project\test4\Image denoising\filtering\001.jpg)

#### 1.均值滤波器

简单平均卷积操作，就是使用对区域进行平均卷积操作来模糊图像，达到去除噪音点的效果，有归一化操作

![boxFilter](C:\Users\黄凯\Desktop\科研\my_project\test4\Image denoising\filtering\boxFilter.jpg)

#### 2.方框滤波器

基本和均值滤波一样，但是可以选择归一化也可以不选择，不选择归一化但是可能会出现溢出

![boxFilter](C:\Users\黄凯\Desktop\科研\my_project\test4\Image denoising\filtering\boxFilter.jpg)

溢出后：

![boxFilter001](C:\Users\黄凯\Desktop\科研\my_project\test4\Image denoising\filtering\boxFilter001.jpg)



#### 3.高斯滤波器

符合高斯(正态)分布的滤波器，使用高斯卷积核来进行高斯模糊

![GaussianBlur](C:\Users\黄凯\Desktop\科研\my_project\test4\Image denoising\filtering\GaussianBlur.jpg)

#### 4.中值滤波器

在某个范围内选择中间数值作为该区域的数值

![medianBlur](C:\Users\黄凯\Desktop\科研\my_project\test4\Image denoising\filtering\medianBlur.jpg)

### 2.数学算子

#### **边缘检测算子分类:**

**1.一阶导数的边缘检测算子，通过模板作为核与图像的每个像素点做卷积和运算，然后选取合适的阈值来提取图像的边缘，例如soble算子**
**2.依据于二阶导数过零点，常见的有Laplacian 算子，此类算子对噪声敏感。**

#### 1.Sobel算子

分为水平Sobel算子和垂直Sobel算子

最后分别进行卷积运算，取绝对值，
$$
G=\sqrt{Gx^2+Gy^2}
$$

$$
Sx=\left[              
\matrix{
  -1 & 0 &1\\
  -2 & 0& 2\\     
  -1 & 0& 1 
}
\right]

\  \ \ Sy=\left[              
\matrix{
  1 & 2 &1\\
  0 & 0& 0\\     
  -1& -2& -1 
}
\right]
$$

#### 2.scharr算子

和soble算子不一样的比例
$$
Sx=\left[              
\matrix{
  -3 & 0 &3\\
  -10 & 0& 10\\     
  -3 & 0& 3 
}
\right]

\  \ \ Sy=\left[              
\matrix{
  3 & 10 &3\\
  0 & 0& 0\\     
  -3& -10& -3 
}
\right]
$$

#### 3.Laplacian 算子

利用二阶微分进行锐化效果
$$
G=\left[              
\matrix{
  0 & 1 &0\\
  1 & -4& 1\\     
  0 & 1& 0 
}
\right]
$$
从做到右边是sobel，scharr，Laplacian算子实验图

![Arithmetic001](C:\Users\黄凯\Desktop\科研\my_project\test4\Image denoising\Arithmetic_test\Arithmetic001.png)

## 图像增强

以下是原图

![test0](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\equal_hist enhance\test0.png)

#### 1.直方图均衡化

利用直方图均衡化，使得高像素值的像素点降低，低像素值的点增大

利用累计函数(前缀和)实现
$$
F=\frac{n}{N} \\其中n为该领域内某个像素的像素点数量\\N是该领域内所有像素点数量
$$
![test1](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\equal_hist enhance\test1.png)

#### 2.拉普拉斯

在图像中，微分是锐化效果，积分是模糊效果

利用二阶导数的拉普拉斯算子实现图像锐化

![test2](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Laplace enhance\test2.png)

#### 3.Log和指数函数增强

Log函数可以实现低像素值像素点增强，高像素值像素点减弱

指数函数相反，高像素值像素点增强，低像素值像素点减弱

log2图像:

![test2](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Log enhance\test2.png)

log10图像:

![test10](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Log enhance\test10.png)

#### 4.幂律增强

利用幂函数的特性，以x的一次方为界限分为，低像素值像素点增强和高像素值像素点增强

![屏幕截图 2024-05-27 120504](C:\Users\黄凯\Pictures\Screenshots\屏幕截图 2024-05-27 120504.png)

0.3:

![test0.3](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Power function domain transformations enhance\test0.3.png)

0.5:

![test0.5](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Power function domain transformations enhance\test0.5.png)

0.8:

![test0.8](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Power function domain transformations enhance\test0.8.png)

2:

![test2](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Power function domain transformations enhance\test2.png)

3:

![test3](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Power function domain transformations enhance\test3.png)

4:

![test4](C:\Users\黄凯\Desktop\科研\my_project\test4\Image enhancement\Power function domain transformations enhance\test4.png)

## 形态学操作

#### 腐蚀和膨胀

膨胀:填充连接作用

![origial_2](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\dilate_test\origial_2.jpg)

![dilate_2](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\dilate_test\dilate_2.jpg)

腐蚀：去除毛刺

![Image corrosion](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\Image corrosion_test\Image corrosion.jpg)

![Image corrosion001_test3](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\Image corrosion_test\Image corrosion001_test3.jpg)

#### 开运算与闭运算

$$
开运算：先腐蚀后膨胀，将噪音点去除后再对图像加强\\

闭运算：先膨胀后腐蚀，先实现加强保留部分噪音点，再去除加强后的噪音点
$$

![result001](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\opening and closing_test\result001.jpg)

![result002](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\opening and closing_test\result002.jpg)

#### 顶帽算法与黑帽算法

$$
顶帽=原始输入-开运算结果  \  (白顶帽变换) \\

黑帽=闭运算-原始输入  \     (黑底帽变换)
$$

##### origial

![origial](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\tophat and blackhat_test\origial.jpg)

##### tophat:保留毛刺

![tophat](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\tophat and blackhat_test\tophat.jpg)

##### blackhat:图像轮廓

![black](C:\Users\黄凯\Desktop\科研\my_project\test4\morphology\tophat and blackhat_test\black.jpg)

## 特征提取

**特征提取过程分为：特征提取，特征描述和特征匹配**

#### 特征提取

##### 1.harris角点检测

角点：向x与y方向移动变化很大的图像块
边界：沿着某一个方向变化小，另一方向移动变化大
$$
角点响应R值：
R=x1*x2-k(x1+x2)^2 \\
R>0 角点  \\
R约等于0 平坦区域 \\
R<0   边界
$$
![test000](C:\Users\黄凯\Desktop\科研\my_project\test4\Feature extraction\Harris corner detection\test000.jpg)

![test3](C:\Users\黄凯\Desktop\科研\my_project\test4\Feature extraction\Harris corner detection\test3.jpg)

##### 2.SIFT尺度不变空间特征变换算法

**尺度空间的获取通常使用高斯模糊来实现**
**尺度不变特征变换匹配算法**
**L(x,y,z)=G(x,y,z)*I(x,y)**
**G是高斯函数**
**SIFT特征对于旋转和尺度均具有不变性，并且对于噪声、视角变化和光照变化具有良好的鲁棒性**
**SIFT所查找到的关键点是一些十分突出，不会因光照、仿射变换和噪音等因素而变化的点，如角点、边缘点、暗区的亮点及亮区的暗点等。**

不同的是角点检测会受到角度旋转的影响，而SIFT算法不会受到影响

**图像的尺度空间是指图像的模糊程度，而非图像的大小。**
近距离看一个物体和远距离看一个物体，模糊程度是不一样的；从近到远，图像越来越模糊的过程，也是图像的尺度越来越大的过程。

###### 1.检测空间极值

检测空间极值分为几个步骤：1.建立高斯金字塔 2.建立DOG高斯差分金字塔 3.DOG局部极值检测

###### 2.关键点的精确定位

以上方法检测到的极值点是离散空间的极值点，
以下通过拟合三维二次函数来精确确定关键点的位置和尺度，
同时去除低对比度的关键点和不稳定的边缘响应点(因为DOG算子会产生较强的边缘响应)，以增强匹配稳定性、提高抗噪声能力。

分为：1.关键点的精确定位 (使用子像素插值法) 2.去除边缘效应 

###### 3.关键点的主方向分配

###### 4.关键点特征描述



###### ![luna001](C:\Users\黄凯\Desktop\科研\my_project\test4\Feature extraction\SIFT_test\luna001.png)   

![test003](C:\Users\黄凯\Desktop\科研\my_project\test4\Feature extraction\SIFT_test\test003.png)

#### 特征描述

特征描述就类似于 我从这张图像上得到了一些数据，例如像素，我该怎么表示它的强度呢？我们就必须说 像素高或低形容，但是我们要可视化我们的口头描述，因此必须通过一些图像之类的方式进行统计，让我们一目了然我们想要表示的意思

**特征描述常见的就是使用直方图来统计特征数据**

#### 特征匹配

##### 1.暴力匹配

直接用图像与我们的模板一对一匹配

缺点：显而易见的慢

![test_Brute-Force1](C:\Users\黄凯\Desktop\科研\my_project\test4\Feature extraction\Feature matching_test\test_Brute-Force1.png)

##### 2.RANSAC算法(随机抽样一致算法)

就是利用最小二乘法进行多次操作，来确保准确性和算法时间复杂度

K对最佳匹配

从匹配器分出分支我们可以选择暴力多次匹配，但是我们可以选择拥有基于树壮的数据结构的Flannd模型，但是Flannd模型需要构造单应性矩阵

![test_RANSAC1](C:\Users\黄凯\Desktop\科研\my_project\test4\Feature extraction\Feature matching_test\test_RANSAC1.png)