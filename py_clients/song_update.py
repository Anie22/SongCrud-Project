import http
import requests

endpoint = "http://localhost:8000/music/song/1/update"

get_response = requests.get(endpoint)