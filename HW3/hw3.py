import random
import math
import re

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# #initial data
# num = int(input('Введите количество элементов массива'))
# array=[]
# for i in range(num):array.append(random.randint(0,9))
# print(array)
# x = int(input('Введите число x'))
# #calculation
# count=0
# for i in range(num):
#     if array[i]==x:count+=1
# #output
# print(f"количество повторений числа {x} равно {count}")

#**************************************************************************
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#initial data
# num = int(input('Введите количество элементов массива'))
# array=[]
# for i in range(num):array.append(random.randint(0,9))
# print(array)
# x = int(input('Введите число x'))
# #calculation
# min_delta=math.inf
# for i in range(num):
#     array[i]-=x
#     if abs(array[i])<abs(min_delta):min_delta=array[i]
# #output
# print(f"ближайшее число {min_delta+x}")
#**************************************************************************
#Initial data
ENG={1:'AEIOULNSTR',2:'DG',3:'BCMP',4:'FHVWY',5:'K',8:'JX',10:'QZ'}
RUS={1:'АВЕИНОРСТ',2:'ДКЛМПУ',3:'БГЁЬЯ',4:'ЙЫ',5:'ЖЗХЦЧ',8:'ШЭЮ',10:'ФЩЪ'}
#Input data
world = input('Введите слово').upper()
#Choose language
if re.search('[A-Z]', world): dic=ENG
else: dic=RUS
print(dic)
#Return key=point if letter = value
points=0
for i in world:
    for key,value in dic.items(): 
        if i in value:
            points+=key

print(points)