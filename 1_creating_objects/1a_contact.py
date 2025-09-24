class Contact:
    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

# Example usage  
if __name__ == "__main__":  
	contact1 = Contact(1, "Alice", "Smith", "alice@example.com")  
	print(f"Contact: {contact1.first_name} {contact1.last_name}, Email: {contact1.email}")
	
	contact2 = Contact(2, "Bobby", "Raymond", "bob@example.com")  
	print(f"Contact: {contact2.first_name} {contact2.last_name}, Email: {contact2.email}")