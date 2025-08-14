# An introduction into the BMI calculator
print("Welcome to the BMI calculator/nPlease input the measurement")


# Classification of the BMI after calculation
def BMI_classification(BMI):
    if BMI < 18.5:
        return "underweight"
    elif 18.5 <= BMI < 25:
        return "a perfect weight"
    elif 25 <= BMI < 30:
        return "overweight!"
    else:
        return "obese!!"
    

# Prompt the user to input their weight and height and print the result   

  
def main():
    try:
        weight = int(input("Enter weight in kgs: "))
        height = float(input("Enter height in m: "))
        BMI = weight / (height**2)
        print(f"Your BMI is {BMI:.2f} and you are {BMI_classification(BMI)}")

    except ValueError: 
        print("Input not understood")           

main()
