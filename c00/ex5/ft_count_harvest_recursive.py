def ft_helper(count: int , cmp : int):
    if(cmp not in range(count+1)):
        return
    else:
        print(f"Day {cmp}")
        return ft_helper(count , cmp+1)

def ft_count_harvest_recursive():

    count = int(input("Days until harvest : "))
    i = 1
    ft_helper(count , i)
    print("harvest time!")

