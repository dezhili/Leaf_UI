# -*- coding: utf-8 -*-
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
import numpy as np 

def leaves_general():
    # split images
    leave_splite.split_save_images('./split_before/', './split_after/')
    images = os.listdir('./split_before/')

    # get the list of splited images
    img_list = leave_splite.get_imlist('./split_after/')
    
    f1 = xlwt.Workbook()
    A4_name = images[0].split('.')[0]  # 442_100
    sheet = f1.add_sheet(A4_name)
    
    num = 1 # sub_leaf
    for img in img_list:
        print('getting leave contours ... ')
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
        round_or_not = ["none"]
        serration_depth_mean = [np.mean(serration_depths)]
        serration_depth_median = [np.median(serration_depths)]
        serration_depth_std = [np.std(serration_depths)]
        serration_width_mean = [np.mean(serration_widthes)]
        serration_width_median = [np.median(serration_widthes)]
        serration_width_std = [np.std(serration_widthes)]
        serration_area_mean = ["none"]
        serration_area_median = ["none"]
        serration_area_std = ["none"]
        print(round_or_not[0], serration_depth_mean)
        
        
        
    
#==============================================================================
#         (filepath, tempfilename) = os.path.split(img)
#         (shotname, extension) = os.path.splitext(tempfilename)  # shotname : 442_100_1
#     
#         name = str(shotname) + '_general.xls'
#==============================================================================
    
    
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
    
        
        print("getting leaf area and perimeter")
        # get leave area and perimeter
        leaf_area = get_leave_area.get_leave_areas(img)
        leaf_perimeter = get_leave_perimeter.get_leave_perimeter(img)
        print("leaf_area:\t", leaf_area)
        print("leaf_perimeter:\t", leaf_perimeter)
        leaf_entire_area = [leaf_area]
        leaf_area_without_holes = ["none"]
        leaf_perimeter = [leaf_perimeter]
        length_left = [height_left]
        length_middle = [height_middle]
        length_right = [height_right]
        width_top = [width_top]
        width_middle = [width_middle]
        width_bottom = [width_bottom]
        L_W = [length_middle[0] / width_middle[0]]
        
        
#==============================================================================
#         serrations_general_names = ['boundary_curvature_mean', 'boundary_curvature_median',
#                               'boundary_curvature_std', 'leaf_area, leaf_perimeter',
#                               'height_left', 'height_middle', 'height_right',
#                               'width_top', 'width_middle', 'width_bottom']
#==============================================================================
        serrations_general_names_new = ['round or not', 'serration_depth_mean', 
                                'serration_depth_median', 'serration_depth_std', 'serration_width_mean', 
                                'serration_width_median', 'serration_width_std', 'serration_area_mean', 
                                'serration_area_median', 'serration_area_std', 'boundary_curvature_mean', 
                                'boundary_curvature_median', 'boundary_curvature_std', 'leaf_entire_area', 
                                'leaf_area_without_holes', 'leaf_perimeter', 'length_left', 'length_middle', 
                                'length_right', 'width_top', 'width_middle', 'width_bottom', 
                                'L:W(ratio=length_middle/width_middle)']
        
#==============================================================================
#         serrations_general = [boundary_curvature_mean, boundary_curvature_median,
#                               boundary_curvature_std, [leaf_area], [leaf_perimeter],
#                               [height_left], [height_middle], [height_right],
#                               [width_top], [width_middle], [width_bottom]]
#==============================================================================

        serration_numbers = [serration_numbers]
        serrations_general_new = [round_or_not, serration_numbers, serration_depth_mean, serration_depth_median, 
                                   serration_depth_std, serration_width_mean, serration_width_median, 
                                   serration_width_std, serration_area_mean, 
                                serration_area_median, serration_area_std, boundary_curvature_mean, 
                                 boundary_curvature_median, boundary_curvature_std, leaf_entire_area, 
                                 leaf_area_without_holes, leaf_perimeter, length_left, length_middle, 
                                 length_right, width_top, width_middle, width_bottom, 
                                 L_W]

        
        save_in_csv_and_text.save_in_leaves_general(A4_name, num,
                                   serrations_general_names_new, serrations_general_new, sheet)
        num += 1
        #del serration_numbers[0]
    f1.save(A4_name+'_leaves_general.xls')

    

def boundary_evenly_segment_coordinate(text):
    # split images
    leave_splite.split_save_images('./split_before/', './split_after/')
    images = os.listdir('./split_before/')

    # get the list of splited images
    img_list = leave_splite.get_imlist('./split_after/')
    
    f1 = xlwt.Workbook()
    A4_name = images[0].split('.')[0]  # 442_100
    sheet = f1.add_sheet(A4_name)
    
    num = 1 # sub_leaf
    for img in img_list:
        
        save_in_csv_and_text.save_in_boundary_evenly(A4_name, num,sheet, text)
        num += 1
        #del serration_numbers[0]
    f1.save(A4_name+'_boundary_evenly_segment_coordinate.xls')
    

    
    
def per_serration_general():
    # split images
    leave_splite.split_save_images('./split_before/', './split_after/')
    images = os.listdir('./split_before/')
    
    # get the list of splited images￼
    img_list = leave_splite.get_imlist('./split_after/')
    
    f2 = xlwt.Workbook()
    A4_name = images[0].split('.')[0]  # 442_100
    sheet = f2.add_sheet(A4_name, cell_overwrite_ok=True)
    
    num = 1 # sub_leaf
    m = 1
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
#==============================================================================
#         serrations_names = ['serration_idx', 'serration_depths', 'serration_widthes',
#                             'curvatures_mean', 'curvatures_median','curvatures_std',
#                             'boundary_curvature_mean', 'boundary_curvature_median',
#                             'boundary_curvature_std']
#==============================================================================
        serrations_names_new = ['serration No.', 'serration_depth(mm)', 'serration_width(mm)', 
                                'serration_area(mm2)', 'serration_curvature_mean', 
                                'serration_curvature_median', 'serration_curvature _std']
        serration_area = ['none'] * serration_numbers                    
        serrations_new = [serration_numbers, serration_depths, serration_widthes, 
                                serration_area, curvatures_mean, curvatures_median,curvatures_std]                    
#==============================================================================
#         serrations = [serration_numbers, serration_depths, serration_widthes,
#                       curvatures_mean, curvatures_median,curvatures_std,
#                       boundary_curvature_mean, boundary_curvature_median,
#                       boundary_curvature_std]
#==============================================================================
        
#==============================================================================
#         (filepath, tempfilename) = os.path.split(img)
#         (shotname, extension) = os.path.splitext(tempfilename)  # shotname : 442_100_1
#     
#         name = str(shotname) + '.xls'
#==============================================================================
    
        # 442_100_serration&curvature.xls
        # save to results of csv format
        save_in_csv_and_text.save_in_per_serration_general(A4_name, m, num,
                                                    serrations=serrations_new,
                                                  serrations_names=serrations_names_new,
                                                  sheet=sheet)
        num+=1
        m+=serrations_new[0]
    f2.save(A4_name+'_per_serration_general.xls')
    
 
    
def boundary_curvature():
    # split images
    leave_splite.split_save_images('./split_before/', './split_after/')
    images = os.listdir('./split_before/')
    
    # get the list of splited images￼
    img_list = leave_splite.get_imlist('./split_after/')
    
    
    A4_name = images[0].split('.')[0]  # 442_100
    
    for img in img_list:
        f3 = xlwt.Workbook()
        # get leaf contours
        contours = get_leave_boundary.get_leave_boundary(img)
        print('叶片边界坐标: ', contours)
    
        # get serration width depth numbers and curvatures ...
        ser4_idx, ser4_deepest_idx, serration_numbers, serration_depths, serration_widthes, \
            curvatures_mean, curvatures_median, curvatures_std, \
            boundary_curvature_mean, boundary_curvature_median, \
            boundary_curvature_std, boundary_curvature, serrations_curvatures = \
            get_leave_serration.get_leave_serration(contours)
    
    
        serrations_names_new = ["serrations_curvature", "boundary_curvature"]
        
        (filepath, tempfilename) = os.path.split(img)
        (shotname, extension) = os.path.splitext(tempfilename)  # shotname : 442_100_1
    
        name = str(shotname) + '_boundary_curvature.xls'
    
        # 442_100_serration_details.xls
        save_in_csv_and_text.save_in_boundary_curvature(A4_name, f3, 
                                                serration_numbers, 
                                                filename=name)
    #f3.save(A4_name+'_serration_details.xls')


def vein_general():
    # split images
    leave_splite.split_save_images('./split_before/', './split_after/')
    images = os.listdir('./split_before/')

    # get the list of splited images
    img_list = leave_splite.get_imlist('./split_after/')
    
    f1 = xlwt.Workbook()
    A4_name = images[0].split('.')[0]  # 442_100
    sheet = f1.add_sheet(A4_name)
    
    num = 1 # sub_leaf
    for img in img_list:
        vein_general_names = ["vein_angle_mean", "vein_angle_median", "vein_angle_std", "top_left_angle",
                "top_right_angle", "bottom_left_angle", "bottom_right_angle",
                "main_vein_curvature_mean", "main_vein_curvature_median",
                "main_vein_curvature_std", "sub_vein_curvature_mean",
                "sub_vein_curvature_median", "sub_vein_curvature_std", "sub_vein_number",
                "vein_cross_angle_number", "vein_cross_angle(multi)"]

        
        save_in_csv_and_text.save_in_vein_general(A4_name, num, vein_general_names, sheet)
        num += 1
        #del serration_numbers[0]
    f1.save(A4_name+'_vein_general.xls')

    
def vein_curvature():
    
    # split images
    leave_splite.split_save_images('./split_before/', './split_after/')
    images = os.listdir('./split_before/')
    
    # get the list of splited images￼
    img_list = leave_splite.get_imlist('./split_after/')
    
    
    A4_name = images[0].split('.')[0]  # 442_100
    
    sub_vein_curvature_numbers = 8
    for img in img_list:
        f3 = xlwt.Workbook()
        
        (filepath, tempfilename) = os.path.split(img)
        (shotname, extension) = os.path.splitext(tempfilename)  # shotname : 442_100_1
    
        name = str(shotname) + '_vein_curvature.xls'
        
        vein_curvature_names = ["main_vein_curvature", "sub_vein_curvature"]
    
        save_in_csv_and_text.save_in_vein_curvature(A4_name, f3,
                                                sub_vein_curvature_numbers, 
                                                filename=name)
    
    
    