def get_cheapest_fruit_id(data:str)->id:
    """
    This function returns the index of the cheapest fruit in the list

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
    count = 0
    
    # print(y)
    for item in y:
        data = float((item.split(","))[1])
        sum.append(data)
        z = max(sum)
        count += 1
    
    print("The cheapest fruit is " , z)
    print("The ID of the fruit is ",count)

get_cheapest_fruit_id('fruits.csv')