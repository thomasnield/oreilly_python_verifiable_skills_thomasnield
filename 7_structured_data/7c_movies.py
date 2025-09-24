import requests  
import json  
  
url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"  
response = requests.get(url)  
movies = json.loads(response.text)  
  
# loop through the movies  
for m in movies:  
    print(m)