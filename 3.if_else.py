# Условгые операторы

var = 'a'
# if имеет условие 
# if var != 0: #tab - пробел, shift+tab - отступ назад
#     print("Hello")
# if var < 0:
#     print("меньше нуля")
# else: 
#     print("не меньше нуля")
# if var == 'a':
#     res = "lit A"
# elif var == 'B':
#     res = " lit B"
# elif var == 'C':
#     res = 'lit C'
# elif var == 'a':
#     res = 'lit a'
# else:
#     res = 'ни один из вариантов'

# print(res)

# ПРИМЕР "ТЕРМОСТАТ"

current_temp = 25
# диапазон температур
min_temp = 21
max_temp = 26

# логика термостата
if current_temp < min_temp:
    print('включен нагрев')
elif current_temp > max_temp:
    print('нагрев выключен')
else:
    print('температура оптимальна')