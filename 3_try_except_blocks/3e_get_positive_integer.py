def get_positive_integer():  
    while True:  
        try:  
            user_input = int(input("Please enter a positive integer: "))  
            if user_input <= 0:  
                raise ValueError("Input must be a positive integer.")  
            return user_input  
        except ValueError as e:  
            print(f"Invalid input: {e}. Please try again.")  
        except Exception as e:  
            print(f"Unexpected error: {e}")  
            raise  
        finally: 
	        print("Positive integer received and returned! Ending loop.")
  
# Example usage  
number = get_positive_integer()  
print(f"You entered a valid positive integer: {number}")