'''
3. ให้รับเวลาเข้าและออกของรถให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้นคํานวณค่าที่จอดรถที่ต้องจ่าย โดยหลักเกณฑ์การคํานวณมีดังนี้
    1) จอดรถไม่เกิน 15 นาทีไม่คิดค่าบริการ
    2) จอดรถเกิน 15 นาทีแต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
    3) จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
    4) จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท

ข้อมูลนําเข้า
มี1 บรรทัด แต่ละบรรทัดมีจํานวนเต็ม 4 จํานวนคั่นด้วย Space โดยบรรทัดที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และบรรทัดที่ 3-4 เป็นชั่วโมงและนาทีของเวลาออก
ข้อมูลส่งออก
มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจํานวนเต็ม
'''

hours_in,miniute_in,hours_out,miniute_out = input("").split()
payment=0

hours_total = int(hours_out)-int(hours_in)
minute_total = int(miniute_out)-int(miniute_in)
n=hours_total

if hours_total==0 and minute_total<=15:
    payment=0
    print(payment)
elif hours_total==0 and minute_total>15:
    payment=10
    print(payment)
elif hours_total<=2 and minute_total >=1 :
    payment=(n+1)*10
    print(payment)
elif hours_total<=2 and minute_total>15:
    payment=10*n
    print(payment)
elif hours_total<=3 and minute_total==0:
    payment=10*n
    print(payment)
elif hours_total ==3 and minute_total>=1:
    payment=50
    print(payment)
elif (hours_total>=4 and hours_total<=6) and minute_total==0:
    payment=30+((n-3)*20)
    print(payment)
elif(hours_total>=4 and hours_total<=5) and minute_total>=0:
    payment=30+((n-2)*20)
    print(payment)
elif hours_total>=6 and minute_total>=0:
    payment=200
    print(payment)
