def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    data = open(data,mode='r').read()
    date1 = data.split("\n")
    sum = 0
    for item in date1:
        sum += float(item.split(",")[1])

    print(sum)

get_total_price('fruits.csv')

    
