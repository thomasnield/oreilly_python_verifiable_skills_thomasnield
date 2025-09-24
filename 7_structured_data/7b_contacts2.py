import json  
  
class Contact:  
    def __init__(self, first_name, last_name, email):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.email = email  
  
contacts = [  
    Contact("John", "Doe", "john.doe@example.com"),  
    Contact("Jane", "Smith", "jane.smith@example.com"),  
    Contact("Bob", "Johnson", "bob.johnson@example.com"),  
    Contact("Alice", "Brown", "alice.brown@example.com"),  
    Contact("Charlie", "Davis", "charlie.davis@example.com"),  
    Contact("Emma", "Wilson", "emma.wilson@example.com"),  
    Contact("David", "Taylor", "david.taylor@example.com"),  
    Contact("Sarah", "Moore", "sarah.moore@example.com"),  
    Contact("Michael", "Lee", "michael.lee@example.com"),  
    Contact("Laura", "Clark", "laura.clark@example.com")  
]  
  
# Save contacts to JSON file  
with open('contacts.json', 'w', encoding='utf-8') as f:  
    json.dump([{  
        'first_name': c.first_name,  
        'last_name': c.last_name,  
        'email': c.email  
    } for c in contacts], f, indent=4)  
  
# Load contacts from JSON file  
contacts = []  
with open('contacts.json', 'r', encoding='utf-8') as f:  
    data = json.load(f)  
    for item in data:  
        contacts.append(Contact(item['first_name'], item['last_name'], item['email']))  
  
# Print to verify  
for c in contacts:  
    print(f"{c.first_name} {c.last_name}: {c.email}")