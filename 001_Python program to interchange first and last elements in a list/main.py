def by_temp_variable(my_list):
    tmp = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = tmp
    print(my_list)

def by_index_referal(my_list):
    my_list[0],my_list[-1]=my_list[-1],my_list[0]
    print(my_list)

def by_operand(my_list):
    start,*middle,end = my_list
    my_list =[end,*middle,start]
    print(my_list)

def by_inbuilt_func(my_list):
    first_el = my_list.pop(0)
    last_el = my_list.pop(-1)
    my_list.insert(0,first_el)
    my_list.append(last_el)
    print(my_list)

def by_slicing(my_list):
    if len(my_list) >= 2:
        my_list = my_list[-1:] + my_list[1:-1] + my_list[:1]
    print(my_list)

def main():
    Input = input("Enter your List Components splitted by comma:")
    In_list = Input.split(",")
    #by_temp_variable(In_list)
    #by_index_referal(In_list)
    #by_operand(In_list)
    #by_inbuilt_func(In_list)
    by_slicing(In_list)
    
if __name__ =="__main__":
    main()