print(f"Total repositories:  "
      f"{response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repository returned: {len(repo_dicts)}")

repo_dicts = repo_dicts[0]
print(f"\nKeys: {len(repo_dicts)}")

for key in sorted(repo_dicts.keys()):
    print(key)