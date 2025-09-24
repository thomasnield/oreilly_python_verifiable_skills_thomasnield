while True:  
    try:  
        a = int(input("Please input a numerator: "))  
        b = int(input("Please input a denominator: "))  
        quotient = a / b  
  
        print(f"{a}/{b} = {quotient}")  
  
    except ValueError:  
        print("Error: Please enter valid integers for both numerator and denominator.")  
    except ZeroDivisionError:  
        print("Error: Division by zero is not allowed.")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  
        raise  # Re-raise unexpected errors to allow program to crash or escalate