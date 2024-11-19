from operator import index

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Index_list = 0
while 1 > 0:
    number = index(my_list[Index_list])
    Len = len(my_list)
    if number < 0 or Index_list >= Len - 1:
        break
    else:
        print(number)
        Index_list = Index_list + 1

