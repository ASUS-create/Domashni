first_name=input("Enter a name: ")
if not  first_name.isalpha():
    raise ValueError("Name must contain only letters")  
else:
    print(f"Name: {first_name}")
last_name=input("Enter a surname: ")
if not last_name.isalpha():
    raise ValueError("Surname must contain only letters")
else:
    print(f"Surname: {last_name}")
age=int(input("Enter age: "))
if age < 0 or age > 120:
    raise ValueError("Age must be between 0 and 120")   
else:
    print(f"Age: {age}")    
gender=(input("enter gender (м/ж): "))
if gender not in ['м', 'ж']:
    raise ValueError ("Gender must be 'м' or 'ж'")
else:
    print(f"Gender: {gender}")
employee_id=int(input("Enter employee ID: "))
print(f"Employee ID: {employee_id}")