filename = "numbers.txt"  
  
try:  
    with open(filename, 'r') as file:  
        total = 0  
        count = 0  
        for line in file:  
            number = float(line.strip())  
            total += number  
            count += 1  
        average = total / count  
        print(f"Average of numbers in {filename}: {average:.2f}")  
except FileNotFoundError:  
    print(f"Error: The file '{filename}' was not found.")  
except ValueError:  
    print("Error: File contains invalid data. All lines must be numbers.")  
except ZeroDivisionError:  
    print("Error: File is empty. Cannot compute average.")  
except Exception as e:  
    print(f"Unexpected error occurred: {e}")  
    raise  
finally:  
    print(f"File handling for {filename} completed.")