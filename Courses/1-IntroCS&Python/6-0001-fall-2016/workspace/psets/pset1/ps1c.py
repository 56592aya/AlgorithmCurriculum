total_cost = 1000000#float(input("Total cost of dream house: "))
portion_down_payment = .25
down_payment= total_cost*portion_down_payment
current_savings=0.0
r = 0.04 #annual rate
mr = r/12.0
#when applied monthly r*current_saving/12
annual_salary = float(input("annual salary: "))
#portion_saved = float(input("portion salary saved: ")) ## saved from salary for 
#how many months it will take
month = 1
semi_annual_raise = 0.07#float(input("semi annual raise: "))

#rest = total_cost - down_payment
#monthly_salary = annual_salary/12
def save(annual_salary, mr, semi_annual_raise,current_savings, portion_saved):
    current_savings = 0.0
    month = 1
    while month < 36:
        if (month % 6  == 0):
            annual_salary = annual_salary *(1.0 + semi_annual_raise)
        monthly_salary = annual_salary/12.0
        salary_saved = monthly_salary * portion_saved/10000
        current_savings *= (1.0+mr)
        current_savings += salary_saved
        month+=1
    
    return current_savings

low = 0
high = 10000
portion_saved = low
num_iter = 1
saved = 0
while (abs(saved - down_payment) > 100.0 and portion_saved != 10000):
    current_savings = 0.0 
    saved = save(annual_salary, mr, semi_annual_raise, current_savings, portion_saved)
    if saved < down_payment:
        low = portion_saved
    else:
        high = portion_saved
    portion_saved = (high+low)/2
    num_iter +=1

if portion_saved == 10000:
    print("not possible")
else:
    print(portion_saved/10000)
    print(num_iter)


