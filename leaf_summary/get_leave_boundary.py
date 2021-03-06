# import matplotlib.pyplot as plt
from skimage import measure,data,color
import cv2
import numpy as np

def get_leave_boundary(image):
    img = cv2.imread(image)
    #生成二值测试图像
    img=color.rgb2gray(img)

    #检测所有图形的轮廓
    contours = measure.find_contours(img, 0.70)
    contours = [contours[i] for i in range(len(contours)) if len(contours[i]) > 100]


    if len(contours) == 1:
        contours = contours
        contours = np.concatenate(contours)
    elif len(contours) == 2:
        contours = np.concatenate(contours)
    elif len(contours) == 3:
        if abs(contours[0][-1][0] - contours[1][0][0])+abs(contours[0][-1][1] - contours[1][0][1])<50:
            contours = np.concatenate((contours[0], contours[1], contours[2]))
        else:
            contours = np.concatenate((contours[0], contours[2], contours[1]))
    elif len(contours) == 4:
        if abs(contours[0][-1][0] - contours[2][0][0])+abs(contours[0][-1][1] - contours[2][0][1])<50:
            contours = np.concatenate((contours[0], contours[2], contours[3], contours[1]))
        else:
            contours = np.concatenate((contours[0], contours[3], contours[2], contours[1]))
    else:
        contours = np.concatenate((contours[0], contours[2], contours[4],contours[3], contours[1]))
    # contours = np.concatenate((contours[0], contours[2], contours[3], contours[1]))

    for i in range(len(contours)):
        contours[i, 0], contours[i, 1] = contours[i, 1], contours[i, 0]
    #绘制轮廓
    # fig, axes = plt.subplots(1,2,figsize=(8,8))
    # ax0, ax1= axes.ravel()
    # ax0.imshow(img,plt.cm.gray)
    # ax0.set_title('original image')
    #
    # rows,cols=img.shape
    # ax1.axis([0,rows,cols,0])
    # # for n, contour in enumerate(contours):
    #
    # ax1.plot(contours[:, 0], contours[:, 1], linewidth=2)
    # ax1.axis('image')
    # ax1.set_title('contours')
    # plt.show()
    return contours
