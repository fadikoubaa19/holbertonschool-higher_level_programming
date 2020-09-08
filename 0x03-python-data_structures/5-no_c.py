def no_c(my_string):
    check = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
        check += i
    return (check)

