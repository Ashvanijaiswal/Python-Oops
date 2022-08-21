cost_of_bread=3.69
num_old_bread=int(input("Enter num of day old bread purchased:"))
total_cost=num_old_bread*cost_of_bread
cost_with_discount=total_cost*40/100
discount=total_cost*60/100
# print("discounted cost is %.2f and total cost is %.2f"%(cost_with_discount,total_cost ))
print("Regular price   :%5.2f"%(cost_of_bread*num_old_bread))
print("Discount Applied:%5.2f"%discount)
print("Total cost      :%5.2f"%cost_with_discount)
