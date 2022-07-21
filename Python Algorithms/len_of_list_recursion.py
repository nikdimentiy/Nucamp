def get_list_lenght(my_list):
    if my_list == []: # base case
        return 0
    return 1 + get_list_lenght(my_list[1:]) # recursion call


my_user_list = [3, 5, 9, 7, 8, 5, 7] # example of my list
print(get_list_lenght(my_user_list)) 
