from __future__ import division
import sys
import xlsxwriter
import xlrd
import datetime
from app.models import *
output_file = u"test.xlsx"
wb = xlsxwriter.Workbook(output_file)
ws = wb.add_worksheet(u"活動標籤")
d = Group_record.objects.filter()
ws.write(2, 0, "123")
wb.close()