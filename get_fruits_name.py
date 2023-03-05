def get_frutis_name(data:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """


    f = open(data,mode='r')
    x = f.read()
    y = x.split("\n")
    z = 0
    sum = []
    data = 0
    for item in y:
        print(item.split(",")[0])

        

get_frutis_name('fruits.csv')

    
