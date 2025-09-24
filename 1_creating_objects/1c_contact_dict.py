class Contact:  
    def __init__(self, id, first_name, last_name, email):  
        self.id = id  
        self.first_name = first_name  
        self.last_name = last_name  
        self.email = email  

if __name__ == "__main__":  
	contacts_dict = {
 	   1: Contact(1, "Alice", "Smith", "alice@example.com"),
 	   2: Contact(2, "Bob", "Jones", "bob@example.com")
	}

	contact = contacts_dict[1]
	print(f"Contact ID 1: {contact.first_name} {contact.last_name}")
	  