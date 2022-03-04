import requests

response = requests.get('https://opentdb.com/api.php?amount=30&category=11&type=boolean')
response.raise_for_status()
data = response.json()
question_data = data['results']
