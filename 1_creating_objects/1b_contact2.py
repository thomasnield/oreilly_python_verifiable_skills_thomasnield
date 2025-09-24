class Contact:  
    def __init__(self, id, first_name, last_name, email):  
        self.id = id  
        self.first_name = first_name  
        self.last_name = last_name  
        self.email = email  

if __name__ == "__main__":  
	contacts = [  
	    Contact(1,"Alice","Smith","alice@example.com"),  
	    Contact(2,"Bobby","Raymond","bob@example.com")  
	]  
	  
	for c in contacts:  
	    print(f"Contact: {c.first_name} {c.last_name}, Email: {c.email}")