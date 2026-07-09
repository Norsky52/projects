

    
while True:
    try:
        num1 = int(input("Please first number: "))
        num2 = int(input("Please second number: "))
        num3 = int(input("Please third number: "))
        total = num1 + num2 + num3
        print("The total is :", total)
        break  # Exit the loop if input is valid
    except ValueError:
        print("Nope! Please enter a valid NUMBER!.")


 