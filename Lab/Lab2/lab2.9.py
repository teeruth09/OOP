'''
9. จากโปรแกรมในข้อ 8 ให้เขียนฟังก์ชัน date_diff เพิ่มเติม โดยให้มีการตรวจสอบ
 วันที่ต้องเป็นวันที่ถูกต้องของเดือนนั้นๆ
 เดือนต้องอยู่ระหว่าง 1-12
 เดือนกุมภาพันธ์ของปีที่มี Leap Year เท่านั้นที่จะมี 29 วันได้
 หากข้อมูล Input ผิดพลาด ให้ Return -1
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
     
    if (month1<1 or month1>12 or month2<1 or month2>12):
        return -1
    elif (day1 < 0 or (day1>day_in_month[month1-1]) or day2<0 or (day2>day_in_month[month2-1])):
        return -1
    elif (month1 == 2 and not is_leap(year1) and day1 == 29)or(month2 == 2 and not is_leap(year2) and day2 == 29):
        return -1
     
    remaining_day_date1 = day_in_year(year1) - day_of_year(day1,month1,year1) + 1 
    day_of_year_date2 = day_of_year(day2,month2,year2)
    day_between_skipped_year = (year2 - year1 - 1) * 365 + sum([int(is_leap(year)) for year in range(year1 + 1,year2)])
    result = remaining_day_date1 + day_of_year_date2 + day_between_skipped_year
    return result
date1=input()
date2=input()
print(date_diff(date1,date2))
