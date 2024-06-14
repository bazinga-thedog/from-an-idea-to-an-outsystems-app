import csv
import requests

url_path = 'https://[your_environment_host]/PadelPersonalCoach/rest/v1/'
headers = { 'x-api-key' : '[Your_API_KEY]'}

url = url_path + 'matches'

input_file = csv.DictReader(open("source.csv"))

for row in input_file:
    response = requests.post(url, json=row, headers= headers)
    if response.status_code == 200:
        print("Match", row['match_type'],"successfully created")
