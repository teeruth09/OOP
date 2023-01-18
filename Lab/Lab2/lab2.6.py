'''
6. กําหนดให้ list x และ y เป็น list ของจํานวนเต็ม โดยมีขนาดเท่ากัน
ให้ return list ที่เป็นผลบวกของ list x และ y โดยใช้ list comprehension
ให้เขียนในฟังก์ชัน function ชื่อ add2list(lst1,lst2)
'''
def add2list(lst1, lst2):
  return[sum(i) for i in zip(lst1,lst2)]

lst1=[1,2,3,4]
lst2=[5,6,7,8]
print(add2list(lst1,lst2))
