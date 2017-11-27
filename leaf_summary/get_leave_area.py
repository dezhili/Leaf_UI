import cv2
import get_pic_rotated_and_broaden


def get_leave_areas(image, dpi=(300, 300)):
    img = cv2.imread(image)
    # 扩大背景, 以防止叶片贴边
    img = get_pic_rotated_and_broaden.get_pic_rotated_and_broaden(img, 10, (255, 255, 255))
    img = get_pic_rotated_and_broaden.get_pic_rotated_and_broaden(img, -10, (255, 255, 255))

    # 提取叶片
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, threshed_img = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)

    # 去噪
    img, contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    small_areas = [i for i in contours if cv2.contourArea(i) < 500]
    cv2.fillPoly(threshed_img, small_areas, 255)
    img, contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea)
    contours.pop()
    # cv2.imshow('threshed_img', threshed_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 统计像素上的大小
    area_pixel = 0
    for i in contours:
        area_pixel += cv2.contourArea(i)

    # 像素 -> 厘米
    area_cm = area_pixel / (dpi[0] * dpi[1]) * (2.54 * 2.54)
    # print('area_cm:', area_cm)

    return area_cm
