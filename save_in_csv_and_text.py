# 442_100_per_serration_general.xls
def save_in_per_serration_general(A4_name, m, num, serrations, serrations_names, sheet):
    if num == 1:
        sheet.write(0, 0, 'A4_name')
        sheet.write(0, 1, 'Sub_leaf')
        for i in range(len(serrations)):
            sheet.write(0, i+2, serrations_names[i])
    
    for i in range(m, m+serrations[0]):
        sheet.write(i, 0, A4_name)
        sheet.write(i, 1, num)
    
    for i in range(2, len(serrations)+1):
        if i == 2:
            for j in range(m, m+serrations[0]):
                sheet.write(j, i, j-m+1)
            continue
        for j in range(m, m+len(serrations[i-2])):
            sheet.write(j, i, serrations[i-2][j-m])

            
# 100_2_1_boundary_curvature
def save_in_boundary_curvature(A4_name, f, serration_numbers, filename):
    # 442_100_curvatures.xls
    sheet2 = f.add_sheet(A4_name, cell_overwrite_ok=True)
    sheet2.write(0, 0, 'A4_name')
    sheet2.write(1, 0, A4_name)
    for i in range(serration_numbers):
        sheet2.write(0, i+1, 'serrations_' + str(i + 1) + '_curvature')
    sheet2.write(0, serration_numbers+1, 'boundary_curvature_all')
    for i in range(serration_numbers+1):
        sheet2.write(1, i+1, 'none')
    f.save(filename)

# 442_100_leaves_general.xls
def save_in_leaves_general(A4_name, num, serrations_general_names, serrations_general, sheet):
    # 442_100_general.xls
    if num == 1:
        sheet.write(0, 0, 'A4_name')
        sheet.write(0, 1, 'Sub_leaf')
        for i in range(len(serrations_general_names)):
            sheet.write(0, i+2, serrations_general_names[i])
    sheet.write(num, 0, A4_name)
    sheet.write(num, 1, num)
    for i in range(len(serrations_general)):
        sheet.write(num, i+2, serrations_general[i][0])

# 442_100_boundary_evenly_segment_coordinate.xls
def save_in_boundary_evenly(A4_name, num, sheet, text):
    if num == 1:
        sheet.write(0, 0, 'A4_name')
        sheet.write(0, 1, 'Sub_leaf')
        i = 0
        for j in range(text):
            sheet.write(0, i+2, 'X'+str(j+1))
            sheet.write(0, i+3, 'Y'+str(j+1))
            i+=2
    sheet.write(num, 0, A4_name)
    sheet.write(num, 1, num)
    for i in range(text*2):
        sheet.write(num, i+2, 'none')

# 442_100_vein_general.xls
def save_in_vein_general(A4_name, num, vein_general_names, sheet):
    if num == 1:
        sheet.write(0, 0, 'A4_name')
        sheet.write(0, 1, 'Sub_leaf')
        for i in range(len(vein_general_names)-1):
            sheet.write(0, i+2, vein_general_names[i])
        for i in range(8):
            sheet.write(0, 2+len(vein_general_names)+i, 'vein_cross_angle_'+str(i+1))
    sheet.write(num, 0, A4_name)
    sheet.write(num, 1, num)
    for i in range(len(vein_general_names)+7):
        sheet.write(num, i+2, 'none')
        

# 100_2_1_boundary_curvature ...
def save_in_vein_curvature(A4_name, f, sub_vein_curvature_numbers, filename):
    # 442_100_curvatures.xls
    sheet2 = f.add_sheet(A4_name, cell_overwrite_ok=True)
    sheet2.write(0, 0, 'A4_name')
    sheet2.write(0, 1, 'main_vein_curvature')
    sheet2.write(1, 0, A4_name)
    for i in range(sub_vein_curvature_numbers):
        sheet2.write(0, i+2, 'sub_vein_' + str(i + 1) + '_curvature')
    for i in range(sub_vein_curvature_numbers+1):
        sheet2.write(1, i+1, 'none')
    f.save(filename)
        

import xlrd
def xls_to_txt(file):
    wb = xlrd.open_workbook(file)

    for sheetName in wb.sheet_names():
        name = sheetName.split('.')[0]
        txtFile = open(name + '.txt', mode='w', encoding='utf-8')
        sheet = wb.sheet_by_name(sheetName)
        for rownum in range(sheet.nrows):
            for i in range(sheet.ncols):
                v = sheet.cell(rownum, i).value
                txtFile.write(str(v))
                txtFile.write(' ')
            txtFile.write('\n')
            # txtFile.write(dataStr)
        txtFile.close()
    
    

def xls_to_txt_2(file, name):
    wb = xlrd.open_workbook(file)

    for sheetName in wb.sheet_names():
        txtFile = open(name + '.txt', mode='a', encoding='utf-8')
        sheet = wb.sheet_by_name(sheetName)
        for rownum in range(sheet.nrows):
            for i in range(sheet.ncols):
                v = sheet.cell(rownum, i).value
                txtFile.write(str(v))
                txtFile.write(' ')
            txtFile.write('\n')
        txtFile.write('\n\n')
            # txtFile.write(dataStr)
    txtFile.close()


def xls_to_txt_3(file, name):
    wb = xlrd.open_workbook(file)

    num = 0
    for sheetName in wb.sheet_names():
        txtFile = open(name + '.txt', mode='a', encoding='utf-8')
        sheet = wb.sheet_by_name(sheetName)

        if num == 0:
            flag = 0
        else:
            flag = 1

        for rownum in range(flag, sheet.nrows):
            for i in range(sheet.ncols):
                v = sheet.cell(rownum, i).value
                txtFile.write(str(v))
                txtFile.write(' ')
            txtFile.write('\n')
        num = 1
            # txtFile.write(dataStr)
    txtFile.close()








