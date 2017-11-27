# save to results of csv format
def save_in_serration_and_curvature(A4_name, num, f, serrations, serrations_names, filename):

    sheet1 = f.add_sheet(filename, cell_overwrite_ok=True)
    sheet1.write(0, 0, 'A4_name')
    sheet1.write(0, 1, 'Sub_leaf')
    sheet1.write(1, 0, A4_name)
    sheet1.write(1, 1, num)
    for i in range(len(serrations)):
        sheet1.write(0, i+2, serrations_names[i])
    for i in range(2, len(serrations)+1):
        if i == 2:
            for j in range(1, serrations[0]+1):
                sheet1.write(j, i, j)
            continue
        for j in range(1, len(serrations[i-1])+1):
            sheet1.write(j, i, serrations[i-1][j-1])

# 修改后
def save_in_serration_details(A4_name, f, serrations_curvatures, boundary_curvature, filename):
    # 442_100_curvatures.xls
    sheet2 = f.add_sheet(filename, cell_overwrite_ok=True)
    sheet2.write(0, 0, 'A4_name')
    sheet2.write(1, 0, A4_name)
    for i in range(len(serrations_curvatures)):
        sheet2.write(0, i+1, 'serrations_' + str(i + 1) + '_curvature')
    sheet2.write(0, len(serrations_curvatures)+1, 'boundary_curvature')
    for i in range(len(serrations_curvatures)):
        for j in range(1, len(serrations_curvatures[i]) + 1):
            sheet2.write(j, i+1, serrations_curvatures[i][j - 1])
    for i in range(1, len(boundary_curvature) + 1):
        sheet2.write(i, len(serrations_curvatures)+1, boundary_curvature[i - 1])


def save_in_serrations_general(A4_name, num, f, serrations_general_names, serrations_general, filename):
    # 442_100_general.xls
    sheet = f.add_sheet(filename, cell_overwrite_ok=True)
    sheet.write(0, 0, 'A4_name')
    sheet.write(1, 0, A4_name)
    sheet.write(0, 1, 'Sub_leaf')
    sheet.write(1, 1, num)
    for i in range(len(serrations_general_names)):
        sheet.write(0, i+2, serrations_general_names[i])
    for i in range(len(serrations_general)):
        sheet.write(1, i+2, serrations_general[i][0])



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








