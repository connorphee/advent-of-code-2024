def columns_to_lists(file_name):
    list_one = []
    list_two = []

    with open(file_name) as file:
        for line in file:
            split = line.strip().split("   ")
            if(len(split) == 2): 
                list_one.append(int(split[0]))
                list_two.append(int(split[1]))
    return (list_one, list_two)
