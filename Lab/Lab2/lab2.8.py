'''
8. จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff
 รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น

date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน
date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน
 ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ปี
 ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย
 ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ
'''
day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    return year%4==0 and year%100 !=0 or year%400 ==0    
def day_in_year(year):
    return 365+ is_leap(year)
def day_of_year(day,month,year):
    return int(month > 2 and is_leap(year)) + sum(day_in_month[:month - 1]) * int(month > 1) + day
def date_diff(date1,date2):
    result = 0
    day1,month1,year1 = [int(num) for num in date1.split("-")]
    day2,month2,year2 = [int(num) for num in date2.split("-")]
    remaining_day_date1 = day_in_year(year1) - day_of_year(day1,month1,year1) + 1 # +1 cuz we include that day
    day_of_year_date2 = day_of_year(day2,month2,year2)
    day_between_skipped_year = (year2 - year1 - 1) * 365 + sum([int(is_leap(year)) for year in range(year1 + 1,year2)])
    ans = remaining_day_date1 + day_of_year_date2 + day_between_skipped_year
    return result
date1=input()
date2=input()
print(date_diff(date1,date2))
