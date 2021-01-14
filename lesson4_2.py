"""Определяем список с элементами n+1 больше чем n, с использованием генератора"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
n_el =- 2
#for n_el in my_list:
#    print(my_list)
#    if my_list[n_el-1] < my_list[n_el]:
#        print(my_list[n_el])
new_my_list=[el for n_el, el in enumerate(my_list) if my_list[n_el] > my_list[n_el-1]]
#new_my_list =[n_el for n_el, el in enumerate(my_lin_)]
print(new_my_list)


