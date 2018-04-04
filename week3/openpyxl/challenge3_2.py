#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from openpyxl import load_workbook 
from openpyxl import Workbook 
import datetime 
courses = load_workbook("courses.xlsx")
def combine():
    
    combine_sheet = courses.create_sheet("combine")
    students_sheet = courses["students"]
    time_sheet = courses["time"]
    for student in students_sheet.values:
        for time in time_sheet.values:
            if student[1] == time[1]:
                combine_sheet.append(list(student)+[time[2]])
    courses.save("courses.xlsx")
    

def split():
    combine_sheet = courses["combine"]
    years = []
    for item in combine_sheet.values:
        if item[0] != "创建时间":
            years.append(item[0].strftime('%Y'))
    years = set(years)
    for year in years:
        wb = Workbook()
        year_sheet = wb.active
        year_sheet.title = year
        for item in combine_sheet.values:
            if item[0] != "创建时间":
                if item[0].strftime('%Y') == year:
                    year_sheet.append(item)
        wb.save('{}.xlsx'.format(year))
        



if __name__ == '__main__':
    combine()
    split()
