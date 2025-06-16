
# Creating a Calculator
# Calculate the Mean
patient_ages = [25, 32, 28, 81, 35, 28, 42]
add = sum (patient_ages)
print (add)
length = len(patient_ages)
print(length)
calculate_mean = sum(patient_ages) / len(patient_ages)
print (calculate_mean)
# Calculate the Median
patient_ages = [25, 32, 28, 81, 35, 28, 42]
new_ages = sorted(patient_ages)
middle_index = len(new_ages) // 2
median_age = new_ages[middle_index]
print(median_age)
# Calculate the mode
patient_ages = [25, 32, 28, 81, 35, 28, 42]
age_counts = {}
for age in patient_ages:
    if age in age_counts:
        age_counts[age] = age_counts[age] + 1
    else:
        age_counts[age] = 1
max_count = 0
mode_age = 0
for age, count in age_counts.items():
    if count > max_count:
        max_count = count
        mode_age = age
print (f"Mean age: {calculate_mean}")
print (f"Median age: {median_age}")
print (f"Mode age: {mode_age}")
