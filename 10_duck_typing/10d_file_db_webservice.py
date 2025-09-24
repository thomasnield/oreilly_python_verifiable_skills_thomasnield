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

class WebService:
    def read(self):
        return "Reading from a web service."
    def close(self):
        return "Web service connection closed."
    
def process_resource(resource):
    print(resource.read())   
    print(resource.close())  

text_file = TextFile()
db = Database()
web_service = WebService()

process_resource(text_file)
process_resource(db)
process_resource(web_service)