#2. ให้ตรวจสอบว่า String ที่รับเข้ามาผ่านคีย์บอร์ด เป็นตัวอักษรพิมพ์เล็ก หรือตัวอักษรพิมพ์ใหญ่ อย่างละกี่ตัว ให้ตอบ 2 บรรทัด จํานวนตัวพิมพ์เล็ก 1 บรรทัด จํานวนตัวพิมพ์ใหญ่ 1 บรรทัด
inputs = input("inputs = ")
upper_character = 0
lower_character = 0
for i in range (len(inputs)):
    if inputs[i].isupper():
        upper_character += 1
    elif inputs[i].islower():
        lower_character +=1
    else:
        pass
print(upper_character)
print(lower_character)
    