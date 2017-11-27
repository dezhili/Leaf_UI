import cv2
import get_pic_rotated_and_broaden


def get_leave_perimeter(image, dpi=(300, 300)):

    img = cv2.imread(image)
    img = get_pic_rotated_and_broaden.get_pic_rotated_and_broaden(img, 10, 255)
    img = get_pic_rotated_and_broaden.get_pic_rotated_and_broaden(img, -10, 255)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, threshed_img = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    small_areas = [i for i in contours if cv2.contourArea(i) < 500]
    cv2.fillPoly(threshed_img, small_areas, 255)
    img, contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea)
    contours.pop()
    perimeter_pixel = 0
    for i in contours:
        perimeter_pixel += cv2.arcLength(i, True)

    perimeter_cm = perimeter_pixel / dpi[0] * 2.54
    # print('perimeter_cm:', perimeter_cm)

    return perimeter_cm
