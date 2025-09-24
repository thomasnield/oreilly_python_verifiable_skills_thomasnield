class Contact:  
    def __init__(self, first_name, last_name, email):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.email = email  
  
    def send_email(self, message, priority="Normal"):  
        print(f"Sending {priority} email to {self.email}: {message}")  
        print("Done!")  
  
    @property  
    def full_name(self):  
        return f"{self.first_name} {self.last_name}"  
  
    def __str__(self):  
        return f"Name: {self.full_name}: Email: {self.email}"  

if __name__ == "__main__":  
	contact = Contact("Alice", "Smith", "alice@example.com")  
	print(contact)