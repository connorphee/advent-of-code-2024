def columns_to_lists(file_name):
"""
    Reads a file where each line contains two integers separated by three spaces 
    and converts the columns into two separate lists.

    Args:
        file_name (str): The path to the file containing two columns of integers.

    Returns:
        tuple[list[int], list[int]]: A tuple containing two lists:
            - The first list contains the integers from the first column.
            - The second list contains the integers from the second column.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
    
    Example:
        File content (`example.txt`):
        123   456
        789   101

        >>> columns_to_lists("example.txt")
        ([123, 789], [456, 101])
"""
    list_one = []
    list_two = []

    with open(file_name) as file:
        for line in file:
            split = line.strip().split("   ")

            if(len(split) == 2): 
                list_one.append(int(split[0]))
                list_two.append(int(split[1]))

    return (list_one, list_two)
