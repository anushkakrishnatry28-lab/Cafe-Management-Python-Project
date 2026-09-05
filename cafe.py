print("Here....is the menu of our cafe....please feel free to order...")
print("pasta:200\nmaggi:60\ncold coffee:60\nchilli potato:70\ntea:30\nchowmein:50\nmomos:50\nmojito:80")
menu={
    "pasta":200,
    "maggi":60,
    "cold coffee":60,
    "chilli potato":70,
    "tea":30,
    "chowmein":50,  
    "momos":50,
    "mojito":80    
}
order_total=0
item1=input("Place you order...").lower()
if item1 in menu:
    order_total+=menu[item1]
else:
    print("Please order something fron the menu")
    
ans=input("want to order anything else...(Y/N)").upper()

if(ans=="Y"): 
    item2=input("Enter the item:-").lower()
    print("Thank you for the order")
    if item2 in menu:
        order_total+=menu[item2]
        
    else:
        print( 
            "order something available in the menu"
        )    

print(f"order placed...please proceed for the payment Rupees{order_total}")
              

        