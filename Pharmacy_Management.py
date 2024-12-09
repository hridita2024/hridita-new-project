item_dict = {
    "napa":[2500,1.75],
    "napa extra":[30,2.25],
    "napa extend":[350,3.25],
    "ace plus":[400,2.25],
    "monas 10mg":[450,9.25]
    }

def show_dict():
    print(30*"=") 
    print("Available Items and Quantity")
    print(30*"=")
    for x in item_dict:
        print(x,(15-len(x))*" ",
          (6-len(str(item_dict[x][0])))*" ",item_dict[x][0])
    print(30*"-") 

def dec_quant(key,val):
    item_dict[key][0]-=val

def inc_quant(key,val):
    item_dict[key][0]+=val
    
def receive_order():
    print("Order Received:")
    while True:
        item=input("Item (type 'x' to stop): ")
        if item=='x':
            break
        value=int(input("Quantity: "))
        if item not in item_dict:
            print ("new item found!")
            #unitprice
            uprice = float(input("unit price: "))
            item_dict[item] = [value,uprice]
            continue
        inc_quant(item,value)
    show_dict() 

def process_demand():
    print("Input Demand:")
    # demand_list =
    demand_list = []
    while True:
        item=input("Item (type 'x' to stop): ")
        if item=='x':
            break
        if item not in item_dict:
            print(f"The item '{item}' is not available!")
            continue
        value=int(input("Quantity: "))
        if value>item_dict[item] [0]:
            print(f"Total of {item_dict[item][0]} pcs are available!")
            continue
        dec_quant(item,value)
        demand_list +=[item,value,
                       item_dict[item][1],
                       value*item_dict[item][1]],

    #printing the payment receipt
    print(40*"=")
    print("**Payment Receipt**".center(40))
    print(40*"=")
    print("Item",7*" ","Quant."," ","U.Price",3*" ","S.Total")
    print(40*"-")
    for x in demand_list:
        print(x[0],(11-len(x[0]))*" ",
            (5-len(str(x[1])))*" ",x[1],
            (8-len(str(x[2])))*" ",x[2],
            (9-len(str(x[3])))*" ",x[3])
        print(x[0],x[1])
    print(40*"-")
    
    show_dict() 
    
