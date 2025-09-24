import random  
  
filename = "numbers.txt"  
num_lines = 10  
  
try:  
    with open(filename, 'w') as file:  
        for _ in range(num_lines):  
            number = random.randint(0, 100)  # Generate random float between 0 and 100  
            file.write(f"{number}\n")  
    print(f"Generated {num_lines} random numbers in {filename}")  
except IOError:  
    print(f"Error: Could not write to file '{filename}'.")  
except Exception as e:  
    print(f"Unexpected error occurred: {e}")  
    raise  
finally:  
    print("Done.")