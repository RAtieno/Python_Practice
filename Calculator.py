# Simple Calculator Program

def format_number(num):
    """Format number to remove unnecessary decimal places"""
    if num == int(num):
        return str(int(num))
    return str(num)

def main():
    print("Simple Calculator")
    print("-" * 16)
    
    try:
        # Get input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
            print(f"{format_number(num1)} + {format_number(num2)} = {format_number(result)}")
        elif operation == '-':
            result = num1 - num2
            print(f"{format_number(num1)} - {format_number(num2)} = {format_number(result)}")
        elif operation == '*':
            result = num1 * num2
            print(f"{format_number(num1)} * {format_number(num2)} = {format_number(result)}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"{format_number(num1)} / {format_number(num2)} = {format_number(result)}")
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    main()