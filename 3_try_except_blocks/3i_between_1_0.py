def get_number_between_zero_and_one():  
    while True:  
        try:  
            user_input = float(input("Please enter a number between 0 and 1: "))  
            if not 0 <= user_input <= 1:  
                raise ValueError("Input must be between 0 and 1.")  
            return user_input  
        except ValueError as e:  
            print(f"Invalid input: {e}. Please try again.")  
        except Exception as e:  
            print(f"Unexpected error: {e}")  
            raise  
        finally:  
            print("Number received and returned! Ending loop.")  
  
# Example usage  
number = get_number_between_zero_and_one()  
print(f"You entered a valid number between 0 and 1: {number}")