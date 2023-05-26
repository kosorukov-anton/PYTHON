# # Ритм винипуха
# #количество слогов
# def calc_glas(krik: list[str]) -> list[int]:
#     glas="АЕЁИОУЫЭЮЯ"
#     slog=[0 for _ in range(len(krik))]
#     k=0
#     for word in krik:
#         for letter in word:
#             for bukva in glas: 
#                 if letter==bukva:slog[k]+=1
#         k+=1
#     return slog
# #проверка равенства слогов
# def slog_equal(slog: list):
#     slog=list(map(lambda x: x-slog[0],slog))
#     rez=0
#     for i in slog: rez+=i
#     if rez: print("нет рифмы")
#     else: print("есть рифма")

# krik=input("введи кричалку").upper().split(" ")
# slog=calc_glas(krik)
# slog_equal(slog)

#*******************************************************************
#Задача от человека, который не очень владеет письменной речью...
#Сделал так, как понял этот текст

# def print_operation_table(operation,num_rows,num_columns):   
#     for i in range(1,num_rows+1):
#         print()
#         for j in range(1,num_columns+1):
#             print(operation(i,j), end=" ")

# print_operation_table(lambda x, y: x * y,3,3)