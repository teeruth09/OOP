'''
4.
ให้เขียนโปรแกรมเพื่อรับข้อมูล 1 บรรทัด ที่ประกอบด้วยจํานวนเต็มหลายจํานวน (คั่นด้วยช่องว่าง)
ให้ส่งคืนว่ามีจํานวนที่เป็นลบกี่จํานวน โดยใช้ List comprehension
ให้เขียนในฟังก์ชัน count_minus(str) แล้ว return เป็นคําตอบ
'''
def count_minus(x):
    y=[number for number in x if number<0]
    return len(y)
x=[int(number) for number in input().split()]
print(count_minus(x))
