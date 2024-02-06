def by_temp_variable(my_list=None):
    n = len(my_list)
    tmp = my_list[0]
    my_list[0] = my_list[n-1]
    my_list[n-1] = tmp
    print(my_list)

def by_index_referal(inlist = None):
    n = len(inlist)
    inlist[0],inlist[n-1]=inlist[n-1],inlist[0]
    print(inlist)

def main():
    Input = input("Enter your List Components splitted by comma:")
    In_list = Input.split(",")
    by_temp_variable(In_list)
    by_index_referal(In_list)
    
if __name__ =="__main__":
    main()