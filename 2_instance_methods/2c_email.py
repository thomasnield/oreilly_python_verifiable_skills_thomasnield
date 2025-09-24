class Contact:  
    def __init__(self, first_name, last_name, email):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.email = email  
  
    def send_email(self, message):  
        print(f"Sending email to {self.email}: {message}")  
        print("Done!")
  
if __name__ == "__main__":  
	contact = Contact("Alice", "Smith", "alice@example.com")  
	contact.send_email("Hello! Did you receive the gift I sent you?")