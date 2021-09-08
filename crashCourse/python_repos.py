import requests

# make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers= headers)
print(f"Status code: {r.status_code}")

# store API response in a variable.

response_dict = r.json()

# process results.
print(response_dict.keys())