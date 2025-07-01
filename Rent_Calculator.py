#Rent Calculator 

#Objective : To calculate the amount ,which should be paid by everyone.
#Inputs :Total rent,Grocery order,Electricity unit spend,Charge per unit
#Outputs : Total amount you have to pay is

rent = int(input("Enter your hostel/flat rent = "))
grocery = int(input("Enter the amount of food/grocery ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (grocery + rent + total_bill) // persons

print("\n Each person will pay = ", output)


""" Output
Enter your hostel/flat rent = 12000
Enter the amount of food/grocery ordered = 8000
Enter the total of electricity spend = 144
Enter the charge per unit = 8
Enter the number of persons living in room/flat = 3

 Each person will pay =  7050"""


