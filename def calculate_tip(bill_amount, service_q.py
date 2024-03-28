def calculate_tip(bill_amount, service_quality, num_people):
    tip_per_person = (bill_amount * (service_quality / 100)) / num_people
    return tip_per_person

# Test Case 1
bill_amount_1 = 500
service_quality_1 = 5
num_people_1 = 2
tip_1 = calculate_tip(bill_amount_1, service_quality_1, num_people_1)
print("Test Case 1: Bill $500, Service Quality: 5, Number of People: 2, Tip per Person: $", tip_1)

# Test Case 2
bill_amount_2 = 1000
service_quality_2 = 3
num_people_2 = 5
tip_2 = calculate_tip(bill_amount_2, service_quality_2, num_people_2)
print("Test Case 2: Bill $1000, Service Quality: 3, Number of People: 5, Tip per Person: $", tip_2)