##learn cv_python ,part 2  ;by xhao 2022/9.4  at Anhui University
import numpy as np

import cv2
import cv2 as cv
import matplotlib
import matplotlib.pyplot as plt

def videodemo():   #读取显示video的函数
    #cap = cv.VideoCapture(0)   #本地摄像头是“0”；
    cap = cv.VideoCapture("wuwu.mp4")  #本地视频
    w=cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv.VideoWriter("image/out1.mp4",cv.CAP_ANY,np.int(cap.get(cv.CAP_PROP_FOCUS)),fps,(np.int(w),np.int(h)),True)
    print(fps)
    while True:
        ret,frame = cap.read()
        frame=cv.flip(frame,1)
        if ret is True:
            cv.imshow("frame",frame)
            c= cv.waitKey(10)
            if c ==27:
                break
    cv.destroyAllWindows()

def image_zhifangtu():          ##给出一幅图，求出对应的直方图
    img = cv.imread("image/tiananmen.png")
    cv.imshow("yuantu",img)
    colors = ("blue","green","red")
    for i ,color in enumerate(colors):
        zhifangtu = cv.calcHist([img],[i],None,[256],[0,256]) #后两个数据，1.等分数，2.图上横坐标；
        plt.plot(zhifangtu,color=color)
        plt.xlim([0,255])
    plt.show()
    cv.waitKey()
    cv.destroyAllWindows()

def eqhist():  ##直方图均衡化函数
    img = cv.imread("image/tiananmen.png",cv.IMREAD_GRAYSCALE)
    cv.imshow("tuantu",img)
    eqhist = cv.equalizeHist(img)
    cv.imshow("eqhist",eqhist)
    cv.waitKey()
    cv.destroyAllWindows()

def conv_demo():     #使用卷积核，对图像进行模糊处理，这个是最简单的滤波；
    img = cv.imread("image/tiananmen.png")
    cv.imshow("yuantu",img)
    result = cv.blur(img,(5,5))
    cv.imshow("mohu",result)
    cv.waitKey()
    cv.destroyAllWindows()

def gaosi_conv_demo():  #高斯滤波，比上面的稍微复杂一点；
    img = cv.imread("image/tiananmen.png")
    cv.imshow("yuantu",img)
    result = cv.GaussianBlur(img,(5,5),15)
    cv.imshow("gaosimohu",result)
    cv.waitKey()
    cv.destroyAllWindows()

def erode_demo():     #腐蚀，在暗通道里使用过；
    img = cv.imread("image/tiananmen.png")
    cv.imshow("yuantu",img)
    core = cv.getStructuringElement(cv.MORPH_RECT,(4,4))  #自己创建一个卷积核，用它去腐蚀原图
    result = cv.erode(img,core)
    cv.imshow("fushi",result)
    cv.waitKey()
    cv.destroyAllWindows()

def gaosi_bifiler_demo():    #高斯双边滤波器函数
    img = cv.imread("image/tiananmen.png")
    cv.imshow("yuantu",img)
    result = cv.bilateralFilter(img,0,100,10)
    cv.imshow("gaosishuangbianlvbo",result)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__=="__main__":
     videodemo()
    # image_zhifangtu()
    # eqhist()
    # conv_demo()
    # gaosi_conv_demo()
    # erode_demo()
    # gaosi_bifiler_demo()

