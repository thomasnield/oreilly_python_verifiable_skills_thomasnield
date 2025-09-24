while True:  
    try:   
        a = int(input("Please input a numerator: "))  
        b = int(input("Please input a denominator: "))  
        quotient = a / b  
      
        print(f"{a}/{b} = {quotient}")  
  
    except Exception as e:  
        print(f"Something bad happened: {e}")