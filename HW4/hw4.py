import random
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# #Iitial data
# num_list1=int(input("Введите количество элементов первого множества"))
# num_list2=int(input("Введите количество элементов второго множества"))
# list1=[]
# for i in range(num_list1):list1.append(random.randint(0,9))
# list2=[]
# for i in range(num_list2):list2.append(random.randint(0,9))
# print(list1)
# print(list2)

# #set without repeats
# set_no_repeat=set()
# for i in range(num_list1): set_no_repeat.add(list1[i])
# for i in range(num_list2): set_no_repeat.add(list2[i])
# print(set_no_repeat)

# #unsorted list
# rezult=[]
# for i in set_no_repeat: rezult.append(i)
# print(rezult)

# #sorting unsorted list
# temp=0
# for i in range(0,len(rezult)-1): 
#     for j in range(len(rezult)-1): 
#         if(rezult[j]>rezult[j+1]): 
#             temp = rezult[j] 
#             rezult[j] = rezult[j+1] 
#             rezult[j+1] = temp 
# print(rezult)

#**********************************************************************************************
#у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной 
# во входном файле грядки.
num_bush=int(input("Введите количество кустов"))
num_sbor=int(input("Введите количество кустов, с которых одновременно ведется сбор ягод"))
berries=[]
for i in range(num_bush):berries.append(random.randint(0,9))
print(berries)
berries.append(berries[0])
berries.insert(0,berries[num_bush-1])

max_bush=0
sborka=0
for i in range(1,num_bush):
    sborka=berries[i-1]+berries[i]+berries[i+1]
    if sborka>max_bush:
        max_bush=sborka
print(max_bush)

