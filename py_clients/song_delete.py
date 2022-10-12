import requests

endpoint = "http://localhost:8000/music/song/1/delete"

get_response = requests.get(endpoint)