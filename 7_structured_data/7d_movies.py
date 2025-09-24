import csv  
  
import requests  
import json  
  
url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"  
response = requests.get(url)  
movies = json.loads(response.text)  
  
# loop through the movies  
with open('movies.csv', 'w', encoding='utf-8', newline='') as f:  
    writer = csv.writer(f)  
    writer.writerow(['title','year'])  
    for m in movies:  
        writer.writerow([m['title'], m['year']])