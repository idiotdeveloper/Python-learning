f_name = input("enter your first name : ")
l_name = input("enter your last name : ")

def format_name(f_n, l_n):
    f_n = f_n.title()
    l_n = l_n.title()
    #print(f_n + " " + l_n)
    return(f_n, l_n)


final_str = format_name(f_name, l_name)
print(final_str)
print(type(final_str))



