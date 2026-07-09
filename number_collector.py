    


def get_valid_number(prompt):
    #Repeats message to the user for a number until a valid number is entered.
    while True:
        try:
            #use float!
            return float(input(prompt))
        except ValueError:
            # This this message will print (e.g., if they typed "abc")
            print("Invalid input! Please enter a valid number.")

def main():
    print("--- Number Collector with Average ---")
    
    # 1. Collect the three numbers with error correction
    num1 = get_valid_number("Enter the first number: ")
    num2 = get_valid_number("Enter the second number: ")
    num3 = get_valid_number("Enter the third number: ")
    
    # 2. Get the sum and average
    total_sum = num1 + num2 + num3
    average = total_sum / 3
    
    # 3. Display the results
    print("--- Results ---")
    print(f"Numbers entered: {num1}, {num2}, {num3}")
    print(f"Sum: {total_sum}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()
        

 