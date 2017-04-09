import os
import xlwt

pathdir = os.listdir(r'C:\Users\free\Documents\University\Learning\Economics\Financial Econometric'
                     r'\class4\2014200222')

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('sheet1')

i = 0
j = 0
for item in pathdir:
    pathdir_1 = os.listdir(r'C:\Users\free\Documents\University\Learning\Economics\Financial Econometric\class4'
                           r'\2014200222\%s' % pathdir[i])
    for file in pathdir_1:
        worksheet.write(j, 0, label=item)
        worksheet.write(j, 1, label=file.split('.')[0])
        worksheet.write(j, 2, label=file.split('_')[0].replace('-', '/'))
        j += 1
    i += 1

workbook.save('2014200222.xls')