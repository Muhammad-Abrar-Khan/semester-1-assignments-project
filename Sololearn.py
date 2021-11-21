'''BMI CALCULATOR'''
height=float(input("Enter height in meter"))
weight=float(input("Enter weight in kg"))
BMI=weight/(height**2)
print(BMI)
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal")
elif BMI>=25 and BMI<30:
    print("Overweight")
else:
    print("Obesity")


