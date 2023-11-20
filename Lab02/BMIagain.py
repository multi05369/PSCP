"""BMIAgain"""
def main():
    """BMIAgain"""
    weight = int(input())
    tall = int(input())
    bmi = weight/((tall/100)**2)
    if bmi >= 30:
        print("Obese")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif bmi < 18.5:
        print("Underweight")

main()
