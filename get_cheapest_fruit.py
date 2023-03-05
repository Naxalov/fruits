def get_cheapest_fruit(data:str)->str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    f = open(data,mode='r')
    x = f.read()
    y = x.split("\n")
    z = 0
    sum = []
    data = 0
    
    for item in y:
        data = float((item.split(","))[1])
        sum.append(data)
        z = max(sum)
    print(z)
            

get_cheapest_fruit('fruits.csv')