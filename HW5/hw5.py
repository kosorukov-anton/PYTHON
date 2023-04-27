#Напишите программу, которая на вход принимает два числа A и B, 
#и возводит число А в целую степень B с помощью рекурсии.

# #initial data
# num=int(input("введите число"))
# err=1
# while err==1:
#     stepen=int(input("введите степень >= 0"))
#     if stepen>=0: err=0

# #func
# def power(num: int, stepen: int) -> int:
#     if stepen==0: return 1
#     if stepen>0: return (num*power(num, stepen-1))

# #calculate
# print(f"Число {num} в степени {stepen} равно {power(num, stepen)}")

#**************************************************************************
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
#initial data
# err=1
# while err==1:
#     num_a=int(input("введите первое число >=0"))
#     num_b=int(input("введите второе число >=0"))
#     if num_a>=0&num_b>=0: err=0

# #func
# def summa_cherez_recurs(num_a: int, num_b: int):
#     if num_b == 0:
#         return num_a
#     else:
#         return summa_cherez_recurs(num_a+1, num_b-1)


# print(f"Сумма {num_a} и {num_b} равна {summa_cherez_recurs(num_a, num_b)}")