import requests

respone = requests.get("https://api.github.com/users/octocat")

if respone.status_code == 200:
    user_data = respone.json()
    
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"bio: {user_data['bio']}")
    print(f"Public Repos: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
    print("failed to retrieve data: , {respone.status_code}")