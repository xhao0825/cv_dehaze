import cv2
import math
import numpy as np

def show_image():
    img = cv2.imread("image/2.jpg") #读入一张图
    img_gray = cv2.imread("image/2.jpg",cv2.IMREAD_GRAYSCALE)  #读入图后灰度表示
    cv2.imshow("picture",img)      #显示
    cv2.imshow("picture_gray",img_gray)

    print(img.shape)       #shape，彩色图出来 h ，w ，c(channel) ;
    print(img_gray.shape)    # 灰度图出来 h，w
    # h,w = img_gray.shape
    # print(h,w)
    roi = img[100:500, 600:900, :]    #从图片里截取一块感兴趣区域
    black = np.zeros_like(img)       #生成一张和img大小一样的黑板
    #black = np.copy(img)  #也可以，black = img 但改变black的时候会改变img
    #black2 = np.zeros((img.shape),dtype=np.uint8)  第二种创建和原图同大小的黑黑图；
    black[100:500, 600:900, :] = roi   #把截的图贴在黑板上； 左边不带坐标时，贴上去的时候黑板变得和截图一样大小
    cv2.imshow("black", black)

def color_space():     #色彩空间的转换
    img = cv2.imread("image/2.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    #rgb2...
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hls= cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    cv2.imshow("picture",img)
    cv2.imshow("GRAY", gray)
    cv2.imshow("HSV", hsv)
    cv2.imshow("HLS", hls)

def pix_image():         #对图像的像素操作    总结img[:,:]=(xx,xx,xx) ;img[:,:,0or1or2]=xx ,不写通道赋3，写了赋1
    img = cv2.imread("image/2.jpg") #读入一张图
    cv2.imshow("picture",img)
    a = img[:, :, 0]  # 提取出一个通道，但是是灰度图；就是暗通道法里取单通道的操作，没有颜色；
    b = img[:, :, 1]   #遍历像素，但只取其中一个通道，012对应bgr；
    d = img[:, :, 2]   #与下面的循环遍历不一样，那个是有颜色的；
    black = np.zeros_like(img)
    black2 = np.zeros_like(img)    #建立几个黑板用来写下面提取的像素；
    black3 = np.zeros_like(img)
    black4 = np.zeros_like(img)
    h,w,c = img.shape   #获取照片的形状信息，进行下面的循环遍历的时候用到；
    print(black.shape)   #黑板也是三通道的；
    print(h,w,c)
    for i in range(h):
        for j in range(w):     #遍历像素
            b,g,r = img[i, j]  # 每个像素三个颜色！！提取出每个像素,☆ 理解以下，把一个像素赋给3个值，按顺序为bgr ，像素读操作
            black[i,j] = (b,0,0)  #把单通道带色的赋给黑板  像素写操作
            black2[i, j] = (0, g, 0)  # 把单通道带色的赋给黑板
            black3[i, j] = (0, 0, r)  # 把单通道带色的赋给黑板
            black4[i, j,0] = b    #对black4一个一个通道地赋值；发现也没错,对的！！
            black4[i, j,1] = g
            black4[i, j,2] = r
            #img[i, j] = (255-b,255-g,255-r)   #对像素进行一次处理
    #cv2.imshow("verse",img)                    #每种功能先会一种方法就行，不要钻牛角尖,但是还真出来了，说明比较灵活；
    # cv2.imshow("blue", black)
    # cv2.imshow("green", black2)
    cv2.imshow("red_color", black4)
    cv2.imshow("red_gray", d)
    #cv2.imwrite("image/result.jpg",black3)  存储存储！！！


def pix_calculate():       #把两张图片的像素信息进行运算，可以改变亮度，或者作为滤镜；
    img = cv2.imread("image/2.jpg") #读入一张图
    cv2.imshow("picture",img)
    black = np.zeros_like(img)
    black[:,:,0] = 90
    black[:, :,1] = 90
    black[:, :, 2] = 90
    # 也可以把上面的3句变成1句， black[:, :] = （90,90,90）
    result = cv2.add(img,black)    #像素加上这么多，相当于变亮了；
    result2 = cv2.subtract(img,black)   #相反；
    cv2.imshow("++", result)
    cv2.imshow("--", result2)


if __name__ == "__main__":
    #show_image()
    #color_space()
    #pix_image()
    #pix_calculate()
    cv2.waitKey(0)
    cv2.destroyAllWindows()