total_cost = float(input("Total cost of dream house: "))
portion_down_payment = .25
down_payment= total_cost*portion_down_payment
current_savings=0.0
r = 0.04 #annual rate
mr = r/12.0
#when applied monthly r*current_saving/12
annual_salary = float(input("annual salary: "))
portion_saved = float(input("portion salary saved: ")) ## saved from salary for 
#how many months it will take
month = 1
semi_annual_raise = float(input("semi annual raise: "))

#rest = total_cost - down_payment
#monthly_salary = annual_salary/12
while (current_savings <= down_payment):
    if ((month) % 6 == 0):
        annual_salary = annual_salary*(1.0+semi_annual_raise)
    monthly_salary = annual_salary/12.0
    salary_saved = portion_saved * monthly_salary
    current_savings = current_savings * (1.0+mr)
    current_savings = current_savings + salary_saved
    month +=1
print(month)

