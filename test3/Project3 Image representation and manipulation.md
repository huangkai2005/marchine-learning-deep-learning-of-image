# *Digital Image Processing:Image Representation and Operations*

$$
project \ \ 3 \\
Kai \ Huang
$$



$$
May \ 2,2024
$$

## outline

**1.image  showing  and  histogram**
**2.bit  plane  decomposition  and  binary  image**
**3.image model**

**4.python code**

## image  showing  and  histogram

### image showing

Our common images, such as jpg, png, etc., are all composed of RGB three primary color models, in the computer three colors are divided into three channels, for example: 
$$
img=cv2.imread('names.png') \\ img[:,:,0],img[:,:,1],img[:,:,2]
$$


#### color image

$$
  value>=0 \\ value<=255
$$

it represents the three channels of BGR. In the CV library function, the image is divided into BGR, and the whole image is divided into pixels. The pixel values of different channels are used to compose the whole image. 

#### gray image

In addition to the common RGB images, in order to more simply reflect the rightness   characteristics of the image, the concept of grayscale map is proposed, and the other channels are turned off, leaving a brightness channel

#### image map

$$
g(x,y)=M-f(x,y)
$$

Inverse the pixel values in the channel,eg: img[:,:]=255-img[:,:]

Negatives can be better used in medical imaging and other fields

![Grayscale map_test](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Grayscale map_test.png)

![origial_gal](C:\Users\黄凯\Desktop\科研\my_project\test3\image_show_test\origial_gal.jpg)

![Grayscale graph_gal](C:\Users\黄凯\Desktop\科研\my_project\test3\image_show_test\Grayscale graph_gal.jpg)

![gal002__blue](C:\Users\黄凯\Desktop\科研\my_project\test3\image_show_test\gal002__blue.jpg)

![gal003__red](C:\Users\黄凯\Desktop\科研\my_project\test3\image_show_test\gal003__red.jpg)

![gal004__green](C:\Users\黄凯\Desktop\科研\my_project\test3\image_show_test\gal004__green.jpg)

### histogram

#### backgrond

In order to better and more intuitively display the properties of images, image researcher introduces the concept of "histogram", through the knowledge of traditional mathematics, statistics on some properties of pixel counting, to mathematically and intuitively observe some properties of images

#### show

![屏幕截图 2024-05-09 134733](C:\Users\黄凯\Pictures\Screenshots\屏幕截图 2024-05-09 134733.png)

![Figure_1_gray](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Figure_1_gray.png)

![CafeStella_screenshot_test01](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\CafeStella_screenshot_test01.png)

![Figure_2_1](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Figure_2_1.png)

![Grayscale map_test](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Grayscale map_test.png)

![Figure_Grayscale map_test](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Figure_Grayscale map_test.png)

#### image equalize

![Figure_Grayscale map_test](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Figure_Grayscale map_test.png)

This is a histogram, it can be observed that the values of this graph are too concentrated in the area of greater than or equal to 150 pixel values, which will make the image look unbalanced in color, so the theory of "equalization" is generated, simply put, it makes the histogram appear "fat" instead of prominent, we will inevitably lose a part of the pixel value to balance the whole image, which will make the image lose some details

![equalize_color](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\equalize_color.png)

![Region-wide equalization001](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Region-wide equalization001.png)



![Figure_Region-wide equalization](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Figure_Region-wide equalization.png)

##### Partial equalization ---- adaptive equalization

Because of equalization, the image may lose some of the key information we want, and then we can take partial equalization measures and only equalize the part, so that the image is neither so polarized nor loses too much key information

![Region-wide equalization002](C:\Users\黄凯\Desktop\科研\my_project\test3\histogram_test\img\Region-wide equalization002.png)

（None->equal->partly equal）

## bit  plane  decomposition  and  binary  image

### bit  plane  decomposition

#### backgrond

The binary pixel values on the same bit in the grayscale map are combined to obtain a binary value image, which is called a bit plane of the grayscale map. This process is bit plane decomposition

Pixel values from 0-255 and 8 binary bits.The image is composed of a string of type char, and the two-dimensional or even three-dimensional array finally forms the whole image

So,the high bit obviously contributes more to the overall number, which is a greedy algorithmic process, and the pixels in the high bit are fuller and closer to the original image

#### fuction

**Image compression: Because the low bit has little influence on the high bit, we can appropriately discard part of the low plane to achieve the image compression function (Gaussian pyramid can also be used to compress Image** 

**data hiding: the same principle, we can choose to modify and hide the low plane data into the data we want to mix, but the surface is not visible**

#### Classification

##### Binary Bit Decomposition (BBD)

The binary of 8 bits is divided into 8 images

![Bits_test1](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test1.png)

![Bits_test2](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test2.png)

![Bits_test3](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test3.png)



![Bits_test5](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test5.png)

![Bits_test6](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test6.png)



![Bits_test7](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test7.png)

![Bits_test8](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test8.png)



##### Gray code bit Decomposition (GCBD)

**Gray code is also known as circular binary code or reflection binary code**
$$
g(i)=\begin{cases}
b(i), & i=n-1\\
bi \ xor \  b(i-1) ,& i>=0 \ and \ i<=n-2
\end{cases}
$$
There is only one bit of the Gray code adjacent to each other that changes for easy observation

In some cases, Gray code may be more suitable for digital signal processing and communication, while in others, plain binary encoding may be more appropriate. However, for a general image, the content of each bit plane of the GCBD is almost completely different from the content of the bit plane to which the BBD is concerned. This decomposition method can often greatly reduce the effects of grayscale changes.

![Bits_test9](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test9.png)

![Bits_test10](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test10.png)

![Bits_test11](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test11.png)

![Bits_test12](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test12.png)

![Bits_test13](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test13.png)



![Bits_test14](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test14.png)

![Bits_test15](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test15.png)

![Bits_test16](C:\Users\黄凯\Desktop\科研\my_project\test3\Bit plane decomposition technique_test\img\Bits_test16.png)



##### P-Fibonacci Bit Decomposition (TFP Bs)

![屏幕截图 2024-05-09 170522](C:\Users\黄凯\Pictures\Screenshots\屏幕截图 2024-05-09 170522.png)

### Image binarization

Image segmentation makes images easier to analyze by simplifying or changing the representation of images. The simplest method of image segmentation is binarization

Image binarization is the process of setting the grayscale value of pixels on an image to 0 or 255, that is, to make the entire image appear obvious black and white. Binary images have only two values per pixel: either pure black or pure white

Because binary image data is simple enough, many vision algorithms rely on binary images. Binary images allow for better analysis of the shape and contours of objects. Binary images are also often used as a mask (also known as a mask) for the original image: it is like a partially hollowed-out piece of paper that obscures areas that are not of interest to us. There are several ways to binarize, the most common of which is to use the thresholding method for binarization. It sets the gray scale of pixels greater than a certain critical gray value to the gray maximum, and the gray scale minimum value less than this value, so as to achieve binarization.

The threshold method is further divided into global method and local method, also known as adaptive thresholding

##### Averaged method

$$
g(x)=\begin{cases}
255&,x>T \\
0&,x<=T
\end{cases}
$$

![nini](D:\project.test\binary_test\nini.png)

![test1](D:\project.test\binary_test\test1.png)

### image model

#### RGB

**RGB (Red, Green, Blue) is the most basic and common image color model, consisting of three primary colors and three color channels**
$$
value>=0 \ \  and \ value<=255
$$
![origial_gal](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\RGB\image_show_test\origial_gal.jpg)

##### change b

As the value of the B channel increases, the proportion of blue gradually increases, and the image becomes blue

![gal002__blue](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\RGB\image_show_test\gal002__blue.jpg)

##### change g

As the value of the g channel increases, the proportion of green gradually increases, and the image turns green

![gal004__green](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\RGB\image_show_test\gal004__green.jpg)

##### chang r

As the value of the r channel increases, the proportion of red gradually increases, and the image turns red

![gal003__red](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\RGB\image_show_test\gal003__red.jpg)

#### CMY

**cyan (C)  Magenta (M) Yellow (Y) **
$$
y=1-(b/255)\\
m=1-(g/255)\\
c=1-(r/255)
$$
<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY_test01.png" alt="CMY_test01" style="zoom:25%;" />

##### chang c

As the value of the C channel increases, the proportion of cyan gradually increases, and the image becomes  cyan

![屏幕截图 2024-05-08 193952](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\C\屏幕截图 2024-05-08 193952.png)



![屏幕截图 2024-05-08 193959](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\C\屏幕截图 2024-05-08 193959.png)

##### chang m

With the increase of the value of the m-channel, the proportion of the magenta color gradually increases, and the picture becomes magenta

![屏幕截图 2024-05-08 192725](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\M\屏幕截图 2024-05-08 192725.png)

![屏幕截图 2024-05-08 192730](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\M\屏幕截图 2024-05-08 192730.png)

![屏幕截图 2024-05-08 192738](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\M\屏幕截图 2024-05-08 192738.png)

![屏幕截图 2024-05-08 192748](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\M\屏幕截图 2024-05-08 192748.png)

![屏幕截图 2024-05-08 192753](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\M\屏幕截图 2024-05-08 192753.png)

##### chang y

As the value of the y channel increases, the proportion of yellow gradually increases, and the image turns yellow

![屏幕截图 2024-05-08 192603](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\Y\屏幕截图 2024-05-08 192603.png)

![屏幕截图 2024-05-08 192610](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\Y\屏幕截图 2024-05-08 192610.png)

![屏幕截图 2024-05-08 192640](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\Y\屏幕截图 2024-05-08 192640.png)

![屏幕截图 2024-05-08 192648](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\Y\屏幕截图 2024-05-08 192648.png)

![屏幕截图 2024-05-08 192656](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\Y\屏幕截图 2024-05-08 192656.png)

![屏幕截图 2024-05-08 192702](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMY\Y\屏幕截图 2024-05-08 192702.png)

#### CMYK

**Blue (C) Magenta(M)  Yellow (Y) Black (B)**
$$
k=1-min(c,m,y)\\
c=1-r/k\\
m=1-g/k\\
y=1-b/k
$$
<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK_test01.png" alt="CMYK_test01" style="zoom:12%;" />

##### change c

![屏幕截图 2024-05-08 194303](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\C\屏幕截图 2024-05-08 194303.png)

![屏幕截图 2024-05-08 194308](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\C\屏幕截图 2024-05-08 194308.png)

![屏幕截图 2024-05-08 194315](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\C\屏幕截图 2024-05-08 194315.png)

##### change m

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\M\屏幕截图 2024-05-08 194237.png" alt="屏幕截图 2024-05-08 194237" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\M\屏幕截图 2024-05-08 194252.png" alt="屏幕截图 2024-05-08 194252" style="zoom:20%;" />

##### change y

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\Y\屏幕截图 2024-05-08 194213.png" alt="屏幕截图 2024-05-08 194213" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\Y\屏幕截图 2024-05-08 194218.png" alt="屏幕截图 2024-05-08 194218" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\CMY(K)\CMYK\Y\屏幕截图 2024-05-08 194223.png" alt="屏幕截图 2024-05-08 194223" style="zoom:20%;" />

#### HSI

**HSI(Hue, Saturation, Intensity )**
$$
H=\begin{cases}
\ arccos( 
\frac{(R-G)+(R-B)}{2\sqrt{(R-G)^2+(R-B)(G-B)}})&B<=G \\
2pi-arccos( 
\frac{(R-G)+(R-B)}{2\sqrt{(R-G)^2+(R-B)(G-B)}})&B>G
\end{cases} \\
S=1-\frac{3}{(R+G+B)}min(R,G,B)\\
I=\frac{R+G+B}{3}
$$


<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI.png" alt="HSI" style="zoom:20%;" />

##### change h

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\h\屏幕截图 2024-05-08 215201.png" alt="屏幕截图 2024-05-08 215201" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\h\屏幕截图 2024-05-08 215154.png" alt="屏幕截图 2024-05-08 215154" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\h\屏幕截图 2024-05-08 215149.png" alt="屏幕截图 2024-05-08 215149" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\h\屏幕截图 2024-05-08 215139.png" alt="屏幕截图 2024-05-08 215139" style="zoom:20%;" />

##### change s

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\s\屏幕截图 2024-05-08 215208.png" alt="屏幕截图 2024-05-08 215208" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\s\屏幕截图 2024-05-08 215429.png" alt="屏幕截图 2024-05-08 215429" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\s\屏幕截图 2024-05-08 215433.png" alt="屏幕截图 2024-05-08 215433" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\s\屏幕截图 2024-05-08 215443.png" alt="屏幕截图 2024-05-08 215443" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\s\屏幕截图 2024-05-08 215453.png" alt="屏幕截图 2024-05-08 215453" style="zoom:20%;" />

##### change i

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\i\08.png" alt="08" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\i\04.png" alt="04" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSI_switch\i\00.png" alt="00" style="zoom:20%;" />

#### HSV

**HSV(Hue, Saturation, Value)**
$$
H=\begin{cases}
\ arccos( 
\frac{(R-G)+(R-B)}{2\sqrt{(R-G)^2+(R-B)(G-B)}})&B<=G \\
2pi-arccos( 
\frac{(R-G)+(R-B)}{2\sqrt{(R-G)^2+(R-B)(G-B)}})&B>G
\end{cases} \\ 
S=\frac{max(R,G,B)-min(R,G,B)}{max(R,G,B)}\\
V=\frac{max(R,G,B)}{255}
$$
<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\my_HSV.png" alt="my_HSV" style="zoom:25%;" />

##### change h

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSV_switch\h\屏幕截图 2024-05-08 215746.png" alt="屏幕截图 2024-05-08 215746" style="zoom:20%;" />



​                                  <img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSV_switch\h\屏幕截图 2024-05-08 215629.png" alt="屏幕截图 2024-05-08 215629" style="zoom:20%;" />

##### change s

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSV_switch\s\屏幕截图 2024-05-08 220011.png" alt="屏幕截图 2024-05-08 220011" style="zoom:20%;" />



<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSV_switch\s\屏幕截图 2024-05-08 215957.png" alt="屏幕截图 2024-05-08 215957" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSV_switch\s\屏幕截图 2024-05-08 215803.png" alt="屏幕截图 2024-05-08 215803" style="zoom:20%;" />

##### change v

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSV_switch\v\08.png" alt="08" style="zoom:20%;" />

<img src="C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\HSL(V)\HSV_switch\v\屏幕截图 2024-05-08 220045.png" alt="屏幕截图 2024-05-08 220045" style="zoom:20%;" />

#### YUV

**YUV(Luminance,Chrominance,Chrominance)**

![屏幕截图 2024-05-09 182844](C:\Users\黄凯\Pictures\Screenshots\屏幕截图 2024-05-09 182844.png)

![屏幕截图 2024-05-08 221129](C:\Users\黄凯\Desktop\科研\my_project\test3\image model_test\YUV\屏幕截图 2024-05-08 221129.png)

### code

python code
