import requests

# TODO: make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# store API response in a variable.

response_dict = r.json()

# process results.
print(response_dict.keys())

print(f"Total git repositories:  "
      f"{response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repository returned: {len(repo_dicts)}")

repo_dicts = repo_dicts[0]
print(f"\nKeys: {len(repo_dicts)}")

for key in sorted(repo_dicts.keys()):
    print(key)

# get git user details

print("\nSelected information about first repository: ")
print(f"Name: {repo_dicts['name']}")
print(f"Owner: {repo_dicts['owner']['login']}")
print(f"Stars: {repo_dicts['stargazers_count']}")
print(f"Repository: {repo_dicts['html_url']}")
print(f"Created: {repo_dicts['created_at']}")
print(f"Updated: {repo_dicts['updated_at']}")
print(f"Description: {repo_dicts['description']}")
print(f"Fork: {repo_dicts['forks_count']}")
