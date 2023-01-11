'''
5. ตัวเลข palindrome คือตัวเลขที่อ่านได้ทั้ง 2 ทาง แล้วมีค่าเท่ากัน เช่น 9009 โดย 9009 คือ palindrome
ที่เกิดจากการคูณของตัวเลข 2 หลักที่มากที่สุด คือ 91x99 จงหา palindrome ที่มากที่สุดของตัวเลข 3
หลัก
'''
product = 0
for first_number in range(999,100,-1):
    for second_number in range(999,100,-1):
        result_number = first_number*second_number
        if str(result_number)==str(result_number)[::-1]:
            if result_number > product:
                product = result_number 
print(product)
