class Contact:  
    def __init__(self, first_name, last_name, email):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.email = email  
  
    def send_email(self):  
        print(f"Sending email to {self.email}")  
        print("Done!")

if __name__ == "__main__":  
	contact = Contact("Alice", "Smith", "alice@example.com")  
	contact.send_email()