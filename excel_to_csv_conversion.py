# Converting excel to csv
filename="book500000.xlsx"
from xlsx2csv import Xlsx2csv as x1
x1(filename,outputencoding="utf-8").convert("500000_Recordsmffile.csv")
