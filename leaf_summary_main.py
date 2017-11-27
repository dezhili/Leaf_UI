import get_leave_boundary
import get_leave_serration
import leave_splite
import get_leave_top_bottom
import get_leave_area
import get_leave_perimeter
import save_in_csv_and_text
import cv2
import math
import os
import xlwt

import matplotlib.pyplot as plt



# split images
leave_splite.split_save_images('./split_before/', './split_after/')
images = os.listdir('./split_before/')


# get the list of splited images￼
img_list = leave_splite.get_imlist('./split_after/')

f1 = xlwt.Workbook()
f2 = xlwt.Workbook()
f3 = xlwt.Workbook()
A4_name = images[0].split('.')[0]  # 442_100

# show the image
fig1, axes1 = plt.subplots(2, 5)
fig2, axes2 = plt.subplots(2, 5)
plt.subplots_adjust(left= 0.125, right=0.9, top=0.9, bottom=0.1)
i = 0
j = 0
count = 0
num = 1 # sub_leaf
for img in img_list:

    # get leaf contours
    contours = get_leave_boundary.get_leave_boundary(img)
    print('叶片边界坐标: ', contours)

    print('getting serration width depth numbers and curvatures ...')
    # get serration width depth numbers and curvatures ...
    ser4_idx, ser4_deepest_idx, serration_numbers, serration_depths, serration_widthes, \
        curvatures_mean, curvatures_median, curvatures_std, \
        boundary_curvature_mean, boundary_curvature_median, \
        boundary_curvature_std, boundary_curvature, serrations_curvatures = \
        get_leave_serration.get_leave_serration(contours)


    # serration_area = get_leave_area_circum.get_leave_area(contours)
    serrations_names = ['serration_idx', 'serration_depths', 'serration_widthes',
                        'curvatures_mean', 'curvatures_median','curvatures_std',
                        'boundary_curvature_mean', 'boundary_curvature_median',
                        'boundary_curvature_std']
    serrations = [serration_numbers, serration_depths, serration_widthes,
                  curvatures_mean, curvatures_median,curvatures_std,
                  boundary_curvature_mean, boundary_curvature_median,
                  boundary_curvature_std]




    (filepath, tempfilename) = os.path.split(img)
    (shotname, extension) = os.path.splitext(tempfilename)  # shotname : 442_100_1

    name1 = str(shotname) + '.xls'
    name2 = str(shotname) + '_serration_details.xls'
    name3 = str(shotname) + '_general.xls'

    # 442_100_serration&curvature.xls
    # save to results of csv format
    save_in_csv_and_text.save_in_serration_and_curvature(A4_name, num, f1,
                                                serrations=serrations,
                                              serrations_names=serrations_names,
                                              filename=name1)

    # 442_100_serration_details.xls
    save_in_csv_and_text.save_in_serration_details(A4_name, f2,
                                                serrations_curvatures=serrations_curvatures,
                                                boundary_curvature=boundary_curvature,
                                                filename=name2)

    image = cv2.imread(img, 0)
    rows, cols = image.shape
    axes1[i, j].axis([0, rows+100, cols+100, 0])
    axes2[i, j].axis([0, rows+100, cols+100, 0])

    get_leave_serration.show_leave_serration(axes1[i, j], contours, ser4_idx, ser4_deepest_idx)



    print('getting leaf width height ...')
    # get leaf width height and rotating angle
    p1_t, p2_b, k1, k2 = get_leave_top_bottom.get_leave_top_bottom(img, contours)
    p3_c, p4_r, p5_l = get_leave_top_bottom.search_points(p1_t, p2_b, k2, contours, search_heng=True)
    p6_c, p7_r, p8_l = get_leave_top_bottom.search_points(p1_t, p3_c, k2, contours, search_heng=True)
    p9_c, p10_r, p11_l = get_leave_top_bottom.search_points(p2_b, p3_c, k2, contours, search_heng=True)
    p12_c, p13_t, p14_b = get_leave_top_bottom.search_points(p5_l, p3_c, k1, contours, search_heng=False)
    p15_c, p16_t, p17_b = get_leave_top_bottom.search_points(p4_r, p3_c, k1, contours, search_heng=False)
    # 计算长度 宽度
    height_middle = math.sqrt((p1_t[0] - p2_b[0]) ** 2 + (p1_t[1] - p2_b[1]) ** 2) / 118.11
    height_left = math.sqrt((p13_t[0] - p14_b[0]) ** 2 + (p13_t[1] - p14_b[1]) ** 2) / 118.11
    height_right = math.sqrt((p16_t[0] - p17_b[0]) ** 2 + (p16_t[1] - p17_b[1]) ** 2) / 118.11
    width_middle = math.sqrt((p5_l[0] - p4_r[0]) ** 2 + (p5_l[1] - p4_r[1]) ** 2) / 118.11
    width_top = math.sqrt((p8_l[0] - p7_r[0]) ** 2 + (p8_l[1] - p7_r[1]) ** 2) / 118.11
    width_bottom = math.sqrt((p11_l[0] - p10_r[0]) ** 2 + (p11_l[1] - p10_r[1]) ** 2) / 118.11
    print('中间的长度为:\t', height_middle)
    print('左边的长度为:\t', height_left)
    print('右边的长度为:\t', height_right)
    print('中间的宽度为:\t', width_middle)
    print('上边的宽度为:\t', width_top)
    print('下边的宽度为:\t', width_bottom)

    get_leave_top_bottom.show_leave_top_bottom(axes2[i, j], contours,
                                               p1_t, p2_b, p4_r, p5_l, p7_r, p8_l,
                                             p10_r, p11_l, p13_t, p14_b, p16_t, p17_b)


    # get leave area and perimeter
    leaf_area = get_leave_area.get_leave_areas(img)
    leaf_perimeter = get_leave_perimeter.get_leave_perimeter(img)


    serrations_general_names = ['boundary_curvature_mean', 'boundary_curvature_median',
                          'boundary_curvature_std', 'leaf_area, leaf_perimeter',
                          'height_left', 'height_middle', 'height_right',
                          'width_top', 'width_middle', 'width_bottom']
    serrations_general = [boundary_curvature_mean, boundary_curvature_median,
                          boundary_curvature_std, [leaf_area], [leaf_perimeter],
                          [height_left], [height_middle], [height_right],
                          [width_top], [width_middle], [width_bottom]]
    save_in_csv_and_text.save_in_serrations_general(A4_name, num, f3,
                               serrations_general_names, serrations_general, name3)

    num += 1
    print("num", num)

    count += 1
    if count == 5:
        i += 1
        j = 0
    else:
        j += 1




plt.show()

# f1.save(images[0].split('.')[0]+'.csv')
# f2.save(images[0].split('.')[0]+'_curvatures.csv')

f1.save(A4_name+'_serration&curvature.xls')
f2.save(A4_name+'_serration_details.xls')
f3.save(A4_name+'_general.xls')

# # xls to txt
# save_in_csv_and_text.xls_to_txt(A4_name+'_serration_details.xls')
# save_in_csv_and_text.xls_to_txt_2(A4_name+'_serration&curvature.xls',
#                                   A4_name + '_serration&curvature')
#
# save_in_csv_and_text.xls_to_txt_3(A4_name+'_general.xls', A4_name+'_general')





