total_cost = float(input("Total cost of dream house: "))
portion_down_payment = .25
down_payment= total_cost*portion_down_payment
current_savings=0.0
r = 0.04 #annual rate
mr = r/12.0
#when applied monthly r*current_saving/12
annual_salary = float(input("annual salary: "))
monthly_salary = annual_salary/12.0
portion_saved = float(input("portion salary saved: ")) ## saved from salary for 
#how many months it will take
salary_saved = portion_saved * monthly_salary
month = 0
#rest = total_cost - down_payment
#monthly_salary = annual_salary/12
while (current_savings < down_payment):
    current_savings = current_savings * (1.0+mr)
    current_savings = current_savings + salary_saved
    month +=1
print(month)






