class TextFile:
    def read(self):
        return "Reading from a text file."
    def close(self):
        return "Text file closed."

class Database:
    def read(self):
        return "Reading from a database."
    def close(self):
        return "Database connection closed."

def process_resource(resource):
    print(resource.read())   # Expects a read method
    print(resource.close())  # Expects a close method

# Both work because they have read() and close() methods
text_file = TextFile()
db = Database()

process_resource(text_file)
process_resource(db)