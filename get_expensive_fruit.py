def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    f = open(data,mode='r')
    x = f.read()
    y = x.split("\n")
    z = 0
    sum = []
    data = 0
        
        # print(y)
    for item in y:
        data = float((item.split(","))[1])
        sum.append(data)
        z = min(sum)
    
    print(z)

get_expensive_fruit('fruits.csv')
