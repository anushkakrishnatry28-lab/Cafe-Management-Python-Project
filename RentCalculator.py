#Rent Calculator 
rent=int(input("Enter the total flat/hostel rent:-"))
food=int(input("Enter the amount of food expenses sepent:-"))
electricity=int(input("Enter the amount of electricity spent:-"))
charge_per_unit=int(input("Enter the charge per unit:-"))
Number_of_person_living=int(input("Enter the number of persons:-"))
total_bill=electricity*charge_per_unit

total_amount_to_pay=((rent+food+total_bill)//(Number_of_person_living))

print("Total amount to pay by each person is Rupees",total_amount_to_pay)
